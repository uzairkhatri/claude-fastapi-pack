from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.notifications.router import router as notifications_router
from app.projects.router import router as projects_router
from app.subscriptions.router import router as subscriptions_router
from app.users.router import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Sample App",
        description="Reference implementation built with claude-fastapi-pack.",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(users_router, prefix="/users", tags=["users"])
    app.include_router(projects_router, prefix="/projects", tags=["projects"])
    app.include_router(subscriptions_router, prefix="/subscriptions", tags=["subscriptions"])
    app.include_router(notifications_router, prefix="/notifications", tags=["notifications"])

    return app


app = create_app()
