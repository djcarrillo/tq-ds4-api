import json
import requests
from src.config import settings
from fastapi import APIRouter, Depends, Response, status, HTTPException
from src.clients.auth import validate_jwt
from src.repositories import repository_prediction_forest


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


@app.get('/info')
async def model_info():
    return {
        'name': 'rando,_fores_ds4',
        'version': settings.VERSION
    }


@ds4_model_api.get(
    "/prediction",
    status_code=status.HTTP_200_OK,
    summary="endpoint for get symbols",
)
async def prediction(cod_granel, min, max, cod_product, num_period):
    prediction = repository_prediction.random_forest()
    return json.dumps(prediction)
