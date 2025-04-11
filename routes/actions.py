from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from services.storage import load_participants, save_participants, add_to_history
from datetime import datetime
import random

router = APIRouter()

@router.post("/add")
async def smartdraw_add(request: Request, name: str = Form(...)):
    participants = load_participants()
    name = name.strip()
    if name and name not in participants:
        participants.append(name)
        save_participants(participants)
    participants = load_participants()
    return request.app.state.templates.TemplateResponse(
        "partials/list.html", {"request": request, "participants": participants}
    )

@router.get("/list", response_class=HTMLResponse)
async def get_name_list(request: Request):
    participants = load_participants()
    return request.app.state.templates.TemplateResponse(
        "partials/list.html", {"request": request, "participants": participants}
    )

@router.get("/draw", response_class=HTMLResponse)
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

@router.delete("/remove/{name}", response_class=HTMLResponse)
async def smartdraw_remove(request: Request, name: str):
    participants = load_participants()
    participants = [p for p in participants if p != name]
    save_participants(participants)

    return request.app.state.templates.TemplateResponse(
        "partials/list.html", {"request": request, "participants": participants}
    )

@router.post("/clear", response_class=HTMLResponse)
async def smartdraw_clear(request: Request):
    save_participants([])
    return request.app.state.templates.TemplateResponse(
        "partials/draw.html", {"request": request, "participants": []}
    )