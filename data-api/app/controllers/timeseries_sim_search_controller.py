from os import lstat
from pathlib import Path
import pandas as pd
from loguru import logger
from fastapi import APIRouter
from app.core.settings import DATA_PATH_LIVE
from app.algorithms.sim_search.firstrunfunctions import firstRunOutput,continentTransformer
from app.algorithms.sim_search.comparefunction import compareOutput
from app.utils.jwt_service import validate_user_token
from pydantic import BaseModel
from typing import List,Dict
from datetime import date
from app.algorithms.sim_search.predictfunctions import predictOutput
from app.algorithms.vats.corr_mat_gen import cor_mat
import json
timeseries_sim_search_controller = APIRouter()

class HeatMapInputs(BaseModel):
    method: str

class ManhattanInputs(BaseModel):
    dummy: int

class SankeyInputs(BaseModel):
    dummy: int 




    
@timeseries_sim_search_controller.post("/dnam_corr_generate/")
async def heatmap_input(inputs:HeatMapInputs):
    df = pd.read_csv(Path(DATA_PATH_LIVE) / 'vtas/example_dnam_data.csv', index_col=0)
    method = inputs.method
    ids,data = cor_mat(df,method)
    output = {"id":ids,"data":data}
    return output

     
@timeseries_sim_search_controller.post("/manhattan_generate/")
async def manhattan_input(inputs:ManhattanInputs):
    df = pd.read_csv(Path(DATA_PATH_LIVE) / 'vtas/example_manhattan_input.csv', index_col=0) 
    return df.to_dict('records')

@timeseries_sim_search_controller.post("/sankey_generate/")
async def sankey_input(inputs:SankeyInputs):
    with open(Path(DATA_PATH_LIVE)/'vtas/sankey.json') as json_file:
        data = json.load(json_file)
    return data

