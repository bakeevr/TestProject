from fastapi import Header, HTTPException, status

import config

async def verify_token(token: str = Header(..., alias="Token")):
    if token != config.API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверный токен авторизации"
        )
    return True