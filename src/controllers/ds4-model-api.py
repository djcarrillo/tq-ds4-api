import requests
from fastapi import APIRouter, Depends, Response, status, HTTPException
from src.clients.auth import validate_jwt
from src.repositories import business_logical


empowerment_router = APIRouter(
    prefix="/empowerment",
    dependencies=[Depends(validate_jwt)],
    responses={200: {"description": "Not found"}},
)

@empowerment_router.get(
    "/test",
    tags=["Events"],
    status_code=status.HTTP_200_OK,
    summary="endpoint for test server",
)
def test():
    return "Un exito"


@empowerment_router.get(
    "/symbols",
    status_code=status.HTTP_200_OK,
    summary="endpoint for get symbols",
)
def symbols():
    return business_logical.available_companies()