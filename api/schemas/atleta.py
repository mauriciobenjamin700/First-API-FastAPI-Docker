from typing import Annotated
from pydantic import Field
from pydantic import PositiveFloat

from api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Atleta", examples="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", examples="11122233344", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples="25")]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", examples=1.70)]
    sexo: Annotated[str, Field(description="Sexo do Atleta [M|F]", examples='M', max_length=1)]