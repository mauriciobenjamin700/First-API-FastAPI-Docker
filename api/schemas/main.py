"""
Classes:
    - Atleta: Modelo de dados para representar um atleta na API.
    - Categoria: Modelo de dados para representar uma categoria na API.
    - CentroTreinamento: Modelo de dados para representar um centro de treinamento na API.
"""

from typing import Annotated
from pydantic import Field
from api.contrib.schemas import BaseSchema
from pydantic import PositiveFloat


class Atleta(BaseSchema):
    """
    Fields:
        - name: Nome do Atleta
        - cpf: CPF do Atleta
        - idade: Idade do Atleta
        - peso: Peso do Atleta
        - altura: Altura do Atleta
        - sexo: Sexo do Atleta [M|F]
    """
    nome: Annotated[str, Field(description="Nome do Atleta", examples="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", examples="11122233344", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples="25")]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", examples=1.70)]
    sexo: Annotated[str, Field(description="Sexo do Atleta [M|F]", examples='M', max_length=1)]

class Categoria(BaseSchema):
    """
    Fields:
        - nome: Nome da Categoria
    
    """
    nome: Annotated[str, Field(description="Nome da Categoria", examples="Scale", max_length=10)]
    

class CentroTreinamento(BaseSchema):
    """
    Fields:
        - nome: Nome do centro de treinamento
        - endereco: Endereco do centro de treinamento
        - proprietario: Proprietario do centro de treinamento
    
    """
    nome: Annotated[str, Field(description="Nome do centro de treinamento", examples="CT King", max_length=20)]
    endereco: Annotated[str, Field(description="Endereco do centro de treinamento", examples="Rua X, Q02", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietario do centro de treinamento", examples="Marcos", max_length=30)]