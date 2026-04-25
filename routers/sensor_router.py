from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session
from ..db.models import SensorDB, SensorCreate, SensorUpdate
from ..crud import sensor_crud as crud
from ..db.database import get_session


router = APIRouter(prefix="/sensors", tags=["sensors"])

#List sensor information with the id of the sensor
@router.get("/list-sensor-info/sensor-id={sensorID}", response_model=SensorDB, description="List sensor information with the id of the sensor")
def list_info(sensorID: str, session: Session = Depends(get_session)):
    return crud.list_info(session, sensorID)

@router.get("/list-all-sensors", response_model=list[SensorDB], description="List all sensors in the sensorDB")
def list_all(session: Session = Depends(get_session)):
    return crud.list_all(session)

@router.get("/list-by-status/where-status={curStatus}", response_model=list[SensorDB])
def list_by_status(session: Session = Depends(get_session), curStatus: bool | None = False):
    return crud.list_status(session, curStatus)

@router.post("", response_model=SensorDB, status_code=status.HTTP_201_CREATED)
def add_sensor(newSensor: SensorCreate, session: Session = Depends(get_session)):
    return crud.add_sensor(session, newSensor)

@router.patch("/sensor-status/sensor={sensorID}/set-status={setStatus}", response_model=bool, status_code=status.HTTP_202_ACCEPTED)
def change_status(setStatus: bool, sensorID: str, session: Session = Depends(get_session)):
    return crud.change_status(session, sensorID, setStatus)

@router.delete("/{sensorID}", status_code=status.HTTP_204_NO_CONTENT)
def remove_sensor(sensorID: str, session: Session = Depends(get_session)):
    return crud.remove_sensor(session, sensorID)
