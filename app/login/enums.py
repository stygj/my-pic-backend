from enum import Enum


class JWTokenStatus(Enum):
    SUCCESS: str = "authenticate success"
    EXPIRED: str = "expired token"
    INVALID_SIGNATURE: str = "invalid signature"
    INVALID_ALGORITHME: str = "invalid algorithme"
    DECODE_ERROR: str = "token decode error"