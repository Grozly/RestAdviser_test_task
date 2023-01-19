import pathlib
import warnings

import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

from app.config.settings import settings


warnings.filterwarnings(action='ignore')  # joblib is unsecure


class LRStrategy:
    """
    Logistic Regression model
    """

    def __init__(self) -> None:
        self.scaler = StandardScaler()
        self.model = None
        self._model_init()

    def _model_init(self) -> None:
        self.model = joblib.load(settings.STRATEGY_DATA_DIR.joinpath("model.sav"))

    def predict(self, data: list):
        proc_data = self.scaler.fit_transform(np.array(data).reshape(1, -1))
        pred_proba = self.model.predict_proba(proc_data)[0][1] # Only 10 features as input.

        if pred_proba <= 0.5:
            signal = 0
        else:
            signal = 1

        return signal
