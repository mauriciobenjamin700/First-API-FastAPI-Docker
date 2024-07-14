"""
Modelo Base para Representar Objetos na API

Classes:
    BaseSchema - Classe base para modelos de API
"""
from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field

class BaseSchema(BaseModel):
    """
    Configurações para validação dos dados do modelo
    Attributs:
        - extra = "forbid" - Força a exclusão de atributos não mapeados
        - from_attributes = True - Permitir a criação de novos atributos do modelo
    """
    class config:
        extra = "forbid"
        from_attributes = True
        
class OutMix(BaseSchema):
    id: Annotated[UUID4, Field(description="Identificador")] 
    created_at: Annotated[datetime, Field(description="Data de Criação")]