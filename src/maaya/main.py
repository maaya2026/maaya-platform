from fastapi import FastAPI

from maaya import __version__
from maaya.api.router import api_router
from maaya.core.config import get_settings


def create_application() -> FastAPI:
    """Create and configure the MAAYA API application."""
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        summary="The intelligence behind everything.",
        description=(
            "MAAYA is an AI operations platform for small businesses. "
            "This API is currently in active development."
        ),
        version=__version__,
    )
    application.include_router(api_router)

    @application.get("/", tags=["system"])
    async def root() -> dict[str, str]:
        return {
            "name": settings.app_name,
            "message": "Welcome to MAAYA - the intelligence behind everything.",
            "version": __version__,
        }

    return application


app = create_application()
