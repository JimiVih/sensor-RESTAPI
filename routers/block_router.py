from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session
from ..db.models import BlockDB, BlockBase, SensorDB
from ..crud import block_crud as crud
from ..db.database import get_session

router = APIRouter(prefix="/blocks", tags=["blocks"])

@router.get("/list-sensors/from-blockID={blockID}", response_model=list[SensorDB], description="GETs list of all sensors in a specific Block")
def list_sensors(blockID: str, session: Session = Depends(get_session)):
    return crud.list_sensors(session, blockID)

@router.post("/add-block/sensorID={sensorID}&blockID={blockID}", response_model=BlockBase, description="Creates a new Block with manually created unique identification (or name), and adds manually given sensor with sensorID")
def add_block(sensorID: str, blockID: str, session: Session = Depends(get_session)):
    return crud.add_block(session, sensorID, blockID)

@router.post("/add-sensor/sensorID={sensorID}&blockID={blockID}", response_model=BlockBase, description="Adds sensor to block")
def add_sensor(sensorID: str, blockID: str, session: Session = Depends(get_session)):
    return crud.add_sensor(session, sensorID, blockID)
