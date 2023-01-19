from dataclasses import dataclass
from typing import Any

from fastapi import HTTPException

from app import schemas
from app import adapters


class StrategyAdapter:
    """
    Global strategy interface adapter.
    """
    def predict(self, data: list) -> int: ...


class FrameworkAdapter:
    """
    Global framework interface adapter.
    """
    def http_exception_400(self, detail: str) -> HTTPException: ...


@dataclass
class GenerateSignalUseCase:
    """
    Signal generator business rules.
    """
    strategy_data: schemas.StrategyData
    sma_strategy: StrategyAdapter = adapters.SMAStrategy()
    lrb_strategy: StrategyAdapter = adapters.LRStrategy()
    framework_adapter: FrameworkAdapter = adapters.FastapiAdapter()

    def generate_signal(self) -> schemas.SignalResponse:
        """
        Generate signal from strategy data.

        Raises:
            self.framework_adapter.http_exception_400: http exception 400
        Returns:
            schemas.SignalResponse: signal result
        """
        strategy = self._find_strategy

        if not strategy:
            raise self.framework_adapter.http_exception_400(
                f"Not found strategy by id={self.strategy_data.strategy_id}!"
            )

        signal = strategy.predict(self.strategy_data.data)

        result = schemas.SignalResponse(signal=signal)
        return result

    @property
    def _find_strategy(self) -> Any:
        """
        A simple method for finding a strategy by id.

        Returns:
            Any: strategy object or None
        """
        statrgy_id = self.strategy_data.strategy_id

        if statrgy_id == 1:
            return self.sma_strategy
        elif statrgy_id == 2:
            return self.lrb_strategy
        else:
            return
