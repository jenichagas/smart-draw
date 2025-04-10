from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import pages, actions
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages.router, prefix="/smartdraw")

app.include_router(actions.router, prefix="/smartdraw")
