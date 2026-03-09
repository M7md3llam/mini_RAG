from Controllers.BaseController import BaseController
from fastapi import FastAPI, APIRouter, Depends, UploadFile
from Models import ResponseStatus

class DataController(BaseController):

    def __init__(self):
        super().__init__()
    

    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False, {"error": ResponseStatus.FILE_TYPE_INVALID}
        if file.size > self.app_settings.FILE_SIZE:
            return False, {"error": ResponseStatus.FILE_SIZE_EXCEEDED}
        return True, {"message": ResponseStatus.FILE_VALIDATION_SUCCESS}