from fastapi import APIRouter, Body, status

from api.contrib.dependence import DataBaseDependecy
from api.schemas.atleta import AtletaInput

router = APIRouter()

@router.post("/", summary="Criar novo Atleta", status_code=status.HTTP_201_CREATED)
async def post(db_session: DataBaseDependecy, atleta_input: AtletaInput = Body(...)): # type: ignore
    pass
