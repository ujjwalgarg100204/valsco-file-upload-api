from fastapi import APIRouter, UploadFile, HTTPException

from services.file_upload_service import FileUploadService

controller = APIRouter()


@controller.post("/upload")
async def upload_file(file: UploadFile):
    file_upload_service = FileUploadService(file)

    try:
        # validate the file
        file_upload_service.validate_file()

        # save the file in system
        await file_upload_service.save_file()

        return {
            "success": True
        }
    except Exception as err:
        raise HTTPException(
            status_code=400,
            detail=str(err)
        )
