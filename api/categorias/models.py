from datetime import datetime
from sqlalchemy import Integer, String
from api.atleta.models import AtletaModel
from api.contrib.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CategoriaModel(Base):
    __tablename__ = "categorias"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="categoria")