from fastapi import FastAPI, APIRouter, Depends, UploadFile , status
from fastapi.responses import JSONResponse

from Helper.confg import get_settings ,Settings
from Models import ResponseStatus
from Controllers import DataController ,ProjectController

import aiofiles
import os

import logging


logger = logging.getLogger("uvicorn.error")


Data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)
@Data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):
    # validate file type and size
    is_valid, result = DataController().validate_file(file = file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
                            content={
                                "signal": result
                                                        }
                            )
    # get project path
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = DataController().generate_unique_filename(
        orig_file_name=file.filename,
          project_id=project_id
          )

    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseStatus.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
        content={
            "signal": ResponseStatus.FILE_UPLOAD_SUCCESS.value
        }
    )