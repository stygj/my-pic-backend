from typing import Optional, Any, Dict
from typing_extensions import Annotated, Doc

from fastapi.exceptions import HTTPException, RequestValidationError


class AuthenticationException(HTTPException):
    """Authentication Exception"""
    def __init__(
        self,
        detail: str
        ):
        super().__init__(
            status_code=101,
            detail=detail
        )