"""
Modelo Base para Representar Objetos no Banco de Dados

Atributos:
    id: Identificador único do objeto

Métodos:
    __init__(self, **kwargs) - Construtor da classe
    to_dict(self) - Método para converter o objeto em um dicionário

Classes:
    BaseModel
"""

from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    """
    Todo Modelo Base terá um identificador único. 
    
    Atributos:
        id: Identificador único do objeto
    """
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),default=uuid4, nullable=False)