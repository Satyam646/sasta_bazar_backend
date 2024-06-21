from pydantic import BaseModel


class Data(BaseModel):
    name:str
    password:str
    age:int
    gender:str

class Check(BaseModel):      
    name:str
    password:str