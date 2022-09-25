from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router


def include_router(app):
    app.include_router(general_pages_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  debug=settings.DEBUG, version=settings.VERSION)
    include_router(app)
    return app


app = start_application()
