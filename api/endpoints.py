from fastapi import APIRouter, Depends

from api.dependencies import verify_token
from api.service.checker import imei_check


router = APIRouter(prefix="/api")

@router.post(
    "/check-imei",
          summary="Проверка IMEI устройства",
          response_description="Результат проверки IMEI",
        )
async def check_imei(
        imei: str,
        _: bool = Depends(verify_token)
):
    result = await imei_check(imei)
    return result



