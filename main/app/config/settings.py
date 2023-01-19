import pathlib

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Global project settings.
    """
    # Dirs
    BASE_DIR: pathlib.PosixPath = pathlib.Path(__file__).resolve().parent.parent
    STRATEGY_DATA_DIR: pathlib.PosixPath = BASE_DIR.joinpath("adapters/strategy_data")


settings = Settings()
