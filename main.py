from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import pages, actions

app = FastAPI()

app.state.templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages.router, prefix="/smartdraw")

app.include_router(actions.router, prefix="/smartdraw")
