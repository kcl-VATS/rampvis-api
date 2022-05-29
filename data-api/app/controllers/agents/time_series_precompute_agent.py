from pathlib import Path
from fastapi import APIRouter
import pandas as pd
from app.algorithms.sim_search.precomputation import to_cube
from loguru import logger
from app.core.settings import DATA_PATH_LIVE

def precompute():
    """Run any kind of precomputation that is slow for real-time search.
    """
    try:
        df = pd.read_csv(Path(DATA_PATH_LIVE) / 'vtas/example_dnam_data.csv', index_col=0)
        #to_cube(df)
        logger.info("vtas done")

    except:
        logger.error('no correlation file')