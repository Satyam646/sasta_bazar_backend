from fastapi import APIRouter
from models import model
from database import db
router = APIRouter(
    tags=['PAGE']
)

@router.get('/home')
def homepage():
    return {"homepage"}

@router.post('/adddata')
def adddata(obj:model.Data):
    check = db.insertData(obj.model_dump())
    if(check):
        return {"response": "OK"}
    else:
        return {"response" : "ERROR"}
    

@router.get('/viewdata')
def getdata():
    return db.viewData()


@router.post('/signin')
def singin(obj:model.Check):
    check = db.checkData(obj.model_dump())
    if(check):
        return {"response": "valid creds"}
    else:
        return {"response":"invalid"}