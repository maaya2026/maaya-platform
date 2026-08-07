from datetime import UTC, datetime

from fastapi import APIRouter
from pydantic import BaseModel

from maaya import __version__
from maaya.core.config import get_settings

router = APIRouter(tags=["system"])


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    timestamp: datetime


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Report whether the API process is alive."""
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        service=settings.app_name,
        version=__version__,
        timestamp=datetime.now(UTC),
    )


@router.get("/ready", response_model=HealthResponse)
async def readiness_check() -> HealthResponse:
    """Report whether the API is ready to receive traffic."""
    settings = get_settings()
    return HealthResponse(
        status="ready",
        service=settings.app_name,
        version=__version__,
        timestamp=datetime.now(UTC),
    )
