from fastapi import HTTPException
from sqlmodel import Session, select
from ..db.models import SensorDB, SensorUpdate, DataDB, DataCreate

def updateSensorBase(data: DataCreate, session: Session, sensorID: str):
    _sID = session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).one().id
    _s = session.get(SensorDB, _sID)
    
    _sUpdate = _s
    _sUpdate.tempData.append(data)
    _sUpdate.model_dump(exclude_unset=True)
    _s.sqlmodel_update(_sUpdate)
    session.add(_s)
    session.commit()
    session.refresh(_s)

#luo uusi data
def create_data(session: Session, sensorID: str, tempData: str, dateData: str):
    if sensorID == None:
        raise HTTPException(status_code=406, detail="sensorID CANNOT be empty! Please insert a valid sensorID.")
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        raise HTTPException(status_code=404, detail=f"There is no sensor with sensorID: '{sensorID}' in the sensorDB!")
    
    newData = DataCreate
    DataCreate.sensor = sensorID
    DataCreate.temp = tempData
    DataCreate.date = dateData

    _dDB = DataDB.model_validate(newData)
    session.add(_dDB)
    session.commit()
    session.refresh(_dDB)

    updateSensorBase(newData, session, sensorID)

    return newData
