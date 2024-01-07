from fastapi import FastAPI

from controllers import chat_controller, file_upload_controller

app = FastAPI()

# add all routers
app.include_router(chat_controller.controller)
app.include_router(file_upload_controller.controller)
