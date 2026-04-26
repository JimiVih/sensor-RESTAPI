from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session
from ..db.models import BlockDB, BlockBase, SensorDB, DataBase, DataDB
from ..crud import data_crud as crud
from ..db.database import get_session

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/new-data/temp-data={tempData}&date={dateData}&from-sensorID={sensorID}", response_model=DataBase, description="Adds new data to dataDB and to sensor's own data list")
def create_new_data(tempData: str, dateData: str, sensorID: str, session: Session = Depends(get_session)):
    #To have more security in the future, the path could also include password of somekind. Which if
    #there is none OR password is incorrect, data could not be created

    return crud.create_data(session, sensorID, tempData, dateData)