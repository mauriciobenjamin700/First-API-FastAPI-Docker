from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from api.configs.database import get_session


DataBaseDependecy: Annotated[AsyncSession, Depends(get_session)]