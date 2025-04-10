from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from services.storage import load_participants, save_participants, add_to_history
from datetime import datetime
import random

router = APIRouter()

router.post("/add")
async def smartdraw_add(name: str = Form(...)):
    participants = load_participants()
    if name.strip():
        participants.append(name.strip())
        save_participants(participants)
    return RedirectResponse(url="smartdraw", status_code=303)


router.get("draw", response_class=HTMLResponse)
async def smartdraw_draw(request: Request):
    participants = load_participants()
    if participants:
        winner = random.choice(participants)
        add_to_history(
            {
                "winner": winner,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        return request.app.state.templates.TemplateResponse(
            "partials/result.html", {"request": request, "winner": winner}
        )
    return HTMLResponse("Nenhum participante foi adicionado!")

router.post("/clear")
async def smartdraw_clear():
    save_participants([])
    return RedirectResponse(url="/smartdraw", status_code=303)