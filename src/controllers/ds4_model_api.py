import json
import requests
from src.config.settings import Setting
from fastapi import APIRouter, Depends, Response, status, HTTPException
from src.clients.auth import validate_jwt
from src.repositories.repository_prediction_forest import RandomForest
from src.repositories.repository_prediction_logit import LogitModel


ds4_model_api = APIRouter(
    prefix="/empowerment",
    dependencies=[Depends(validate_jwt)],
    responses={200: {"description": "Not found"}},
)

@ds4_model_api.get(
    "/status",
    tags=["Events"],
    status_code=status.HTTP_200_OK,
    summary="status server",
)
def test():
    return "status 200"


@ds4_model_api.get('/info')
async def model_info():
    return {
        'name': 'rando,_fores_ds4',
        'version': Setting.VERSION
    }


@ds4_model_api.post(
    "/prediction_forest",
    status_code=status.HTTP_200_OK,
    summary="endpoint for get symbols",
)
async def prediction(cod_granel, min, max, cod_product, num_period):
    prediction = RandomForest()
    data=[cod_granel,min,max,cod_product,num_period]
#    data={
#            'COD GRANEL': cod_granel,
#             'Minimo': min,
#             'Maximo': max,
#             'Código producto': cod_product,
#             'NumeroPeriodosToma': num_period
#    }
    response = prediction._prediction(medication_study=data)

    return json.dumps({'prediction': response[0]})


@ds4_model_api.post(
    "/prediction_logit",
    status_code=status.HTTP_200_OK,
    summary="endpoint for calculate the probability of passing a stability study",
)
async def prediction(month, ATC):
    prediction = LogitModel()
    response = prediction._prediction(mes=month, ATC=ATC)

    return json.dumps({'prediction': response})
