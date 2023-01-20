from typing import List

from pydantic import BaseModel, root_validator


class StrategyData(BaseModel):
    strategy_id: int
    data: List[int]

    @root_validator(pre=True)
    def check_len_data_for_second_strategy(cls, values):
        if values["strategy_id"] == 2 and len(values["data"]) > 10:
            raise ValueError(f"Strategy 2 cannot accept more than 10 values")
        return values
