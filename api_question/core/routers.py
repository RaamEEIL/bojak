"""
Routers
"""
from typing import Dict

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

from api_question.core.handler import Handler
from api_question.core.model import CustomModel

router: APIRouter = APIRouter()

@router.post('/process-json',
             status_code=HTTP_201_CREATED,
             response_model=Dict,
             summary='JWT Login',
             description='Does JWT login stuff'
             )
def post_process_json(fields: CustomModel):
    try:
        response: Dict[str, str] = Handler.process_fields(fields)
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__repr__())

    return response
