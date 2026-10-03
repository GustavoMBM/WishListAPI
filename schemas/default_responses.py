from pydantic import BaseModel

class DefaultResponses(BaseModel):
    msg: str

#Qualquer mensagem genérica deve incluir o id na string usando uma string formatada