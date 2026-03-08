from fastapi import FastAPI, APIRouter, Depends
from Helper.confg import get_settings ,Settings
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    #using dependency injection to get the settings from the .env file and this more secure than importing the settings directly from the config file because it allows us to easily switch between different settings for different environments (development, staging, production) without changing the code. We can simply set the environment variables or use different .env files for each environment. This also helps to keep sensitive information like API keys out of the codebase and makes it easier to manage configurations in a centralized way.
    # app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version,
    }