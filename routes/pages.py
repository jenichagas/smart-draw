from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.storage import save_participants
import random

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def smartdraw_home(request: Request):
    save_participants([])
    return templates.TemplateResponse(
        "app/smartdraw.html", {"request": request, "participants": []}
    )
