import pathlib
import shutil
import uuid

from fastapi import UploadFile

from definitions import ROOT_DIR


class InvalidFileException(Exception):
    """
    Exception raised for invalid file types.
    """

    def __init__(self, message: str):
        super().__init__(message)


class FileSaveException(Exception):
    """
    Exception raised when there is an error saving a file.
    """

    def __init__(self, message: str):
        super().__init__(message)


UPLOAD_DIRECTORY = pathlib.Path(ROOT_DIR) / "files"
UPLOAD_DIRECTORY.mkdir(exist_ok=True)


class FileUploadService:
    """
    Service class for handling file upload operations.
    """

    ALLOWED_EXTENSIONS = "txt", "pdf"
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    def __init__(self, file: UploadFile):
        self.file = file

    def validate_file(self) -> bool:
        """
        Validates the uploaded file.
            - valid file extensions
            - valid file size

        Returns:
            bool: True if the file is valid, False otherwise.
        
        Raises:
            InvalidFileException: If the file extension is not allowed or if the file size exceeds the limit.
        """
        file_extension = self.file.filename.split(".")[-1]
        if file_extension.lower() not in FileUploadService.ALLOWED_EXTENSIONS:
            raise InvalidFileException(
                f"Only allowed file extensions are: {', '.join(FileUploadService.ALLOWED_EXTENSIONS)}'")

        if self.file.size > FileUploadService.MAX_FILE_SIZE:
            raise InvalidFileException(f"File size must be less than {FileUploadService.MAX_FILE_SIZE} Bytes")

        return True

    @staticmethod
    def __get_new_file_path(file_extension: str) -> pathlib.Path:
        """
        Generates a new file path with a unique filename based on the given file extension.

        Args:
            file_extension (str): The file extension.

        Returns:
            pathlib.Path: The new file path.
        """
        return UPLOAD_DIRECTORY / (str(uuid.uuid4()) + "." + file_extension)

    async def save_file(self) -> None:
        """
        Saves the uploaded file to the server.

        Raises:
            FileSaveException: If there is an error while saving the file.
        """
        file_extension = self.file.filename.split(".")[-1].lower()
        new_file_path = self.__get_new_file_path(file_extension)

        with open(new_file_path, "wb") as out_file:
            try:
                shutil.copyfileobj(self.file.file, out_file)
            except Exception as err:
                print(err)
                raise FileSaveException("Unable to save file")
            finally:
                out_file.close()
