from fastapi import FastAPI, APIRouter, Depends, UploadFile
from Helper.confg import get_settings ,Settings
base_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)
@Data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):
    # validate file type and size
    if file.content_type not in app_settings.FILE_ALLOWED_EXTENSIONS:
        return {"error": "Invalid file type"}
    if file.size > app_settings.FILE_SIZE:
        return {"error": "File too large"}
