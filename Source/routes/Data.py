from fastapi import FastAPI, APIRouter, Depends, UploadFile
from Helper.confg import get_settings ,Settings
from Controllers import DataController

data_controller = DataController()

Data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)
@Data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):
    # validate file type and size
    is_valid, result = data_controller.validate_file(file = file)
    
    return result

