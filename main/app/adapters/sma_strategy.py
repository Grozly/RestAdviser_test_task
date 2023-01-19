class SMAStrategy:
    """
    Simple moving average strategy
    """

    def __init__(self, short_term: int = 5, long_term: int = 20) -> None:
        self._short_term = short_term
        self._long_term = long_term

    def predict(self, data: list):
        sma_st = sum(data[-self._short_term:]) / self._short_term
        sma_lt = sum(data[-self._long_term:]) / self._long_term

        signal = int(sma_st > sma_lt)

        return signal
