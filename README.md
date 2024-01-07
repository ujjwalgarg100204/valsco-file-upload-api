# File Upload API

File Upload service for use in Valsco

## Usage

You need anaconda to run this project

### Clone the repo

```bash
git clone https://github.com/ujjwalgarg100204/valsco-file-upload-api
cd valsco-file-upload-api
```

### Create Conda environment

- Create env from provided env file
    ```bash
  conda env create -f enviornment.yml
    ```
- Activate the env
  ```bash
  conda activate file-upload-api
  ```

### Run the file

- For Development purposes
  ```bash
  uvicorn main:app --reload
  ```

## Docs for API

After you have successfully run the project, head to `/docs` endpoint which will all documentation of the project