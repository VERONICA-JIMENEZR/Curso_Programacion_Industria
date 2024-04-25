from pydantic import BaseModel
from typing import Optional

class datalikeDTO(BaseModel):
    Id: Optional[str]
    Nombre :str
    Apellido :str
    Celular : str
    Edad: int