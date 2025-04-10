from fastapi import APIRouter, Request, Form 
from datetime import datetime
from services.storage import load_participants, save_participants, add_to_history


router.post("/add")
async def smartdraw_add(name: str = Form(...)):
    participants = load_participants()
    if name.strip(): 
        participants.append(name.strip())
        save_participants(participants)
    return RedirectResponse(url="smartdraw", status_code=303)