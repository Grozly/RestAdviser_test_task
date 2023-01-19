from typing import List

from pydantic import BaseModel


class StrategyData(BaseModel):
    strategy_id: int
    data: List[int]
