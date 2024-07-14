from api.contrib.schemas import OutMix
from api.schemas.main import Atleta

class AtletaInput(Atleta):
    pass

class AtletaOutput(AtletaInput, OutMix):
    pass