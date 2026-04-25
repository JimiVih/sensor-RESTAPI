#ANTURI CRUD
from fastapi import HTTPException
from sqlmodel import Session, select
from ..db.models import SensorDB, SensorCreate, SensorUpdate

#Lisää anturi()
def add_sensor(session: Session, sensor: SensorCreate):
    _s = SensorDB.model_validate(sensor)
    session.add(_s)
    session.commit()
    session.refresh(_s)
    return _s

#Muuta anturin tilaa()
def change_status(session: Session, sensorID: str, changeStatus: bool):
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        print("The row does not exist!")
        raise HTTPException(status_code=404, detail=f"No sensor with ID: '{sensorID}' was found in the database")
    _sID = session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).one().id
    _s = session.get(SensorDB, _sID)
    if _s.status == changeStatus:
        raise HTTPException(status_code=409, detail=f"sensor '{sensorID}' already has status set to '{changeStatus}'")
    
    #vaihda tilaa
    #_newStatus = statusUpdate.model_dump(exclude_unset=True)
    _sUpdate = _s
    _sUpdate.status = changeStatus
    _sUpdate.model_dump(exclude_unset=True)
    _s.sqlmodel_update(_sUpdate)
    session.add(_s)
    session.commit()
    session.refresh(_s)
    return _s.status

#Listaa anturit()
def list_all(session: Session):
    return session.exec(select(SensorDB)).all()
    
#Listaa anturin kaikki tiedot()
#Puuttuu mitta-arvot ja lohko
def list_info(session: Session, sensorID: str):
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        print("The row does not exist!")
        raise HTTPException(status_code=404, detail=f"No sensor with ID: '{sensorID}' was found in the database")
    _sID = session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).one().id
    print(f"ID: {_sID}")
    _s = session.get(SensorDB, _sID)
    
    return _s

#Poista anturi
def remove_sensor(session: Session, sensorID: str):
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        print("The row does not exist!")
        return
    _sID = session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).one()
    session.delete(_sID)
    session.commit()
    print(f"Sensor with id: '{sensorID}' successfully deleted")
    return {"message": f"Sensor with ID '{sensorID}' deleted!"}

#Listaa anturit tilan mukaan()
def list_status(session: Session, curStatus: bool):
    return session.exec(select(SensorDB).where(SensorDB.status==curStatus)).all()
#Listaa anturin tilamuutokset()

#Listaa virhetilanteet()