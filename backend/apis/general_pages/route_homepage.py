from re import template
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})
