from enum import Enum


class ResponseStatus(Enum):
    
    FILE_VALIDATION_SUCCESS = "File validation successful"
    FILE_VALIDATION_ERROR = "File validation error"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_TYPE_INVALID = "File type invalid"
    FILE_UPLOAD_SUCCESS = "File upload successful"
    FILE_UPLOAD_ERROR = "File upload error"
