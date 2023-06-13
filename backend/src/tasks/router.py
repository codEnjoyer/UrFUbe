from fastapi import APIRouter, Depends

from auth.base_config import current_user

from .tasks import send_welcome_email

# TODO:снести всё
router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_welcome_email(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
