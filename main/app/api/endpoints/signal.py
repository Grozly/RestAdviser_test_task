import logging

from fastapi import APIRouter, status

from app import schemas
from app import services


logger = logging.getLogger("RestAdviser")
router = APIRouter()


@router.post(
    "/generate_signal",
    tags=["signal"],
    response_model=schemas.SignalResponse,
)
def generate_signal(strategy_data: schemas.StrategyData):
    """
    Generate signal from strategy data.

    Args:
        strategy_data (schemas.StrategyRequest): strategy data
    Return:
        schemas.SignalResponse: signal number
    """
    use_case = services.GenerateSignalUseCase(strategy_data)
    current_signal = use_case.generate_signal()
    return current_signal
