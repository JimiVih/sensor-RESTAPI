#LOHKO CRUDE
from fastapi import HTTPException
from sqlmodel import Session, select
from ..db.models import BlockDB, BlockBase, SensorDB


#Luo lohko()
def add_block(session: Session, sensorID: str, blockID: str):
    if sensorID == None:
        raise HTTPException(status_code=406, detail="sensorID CANNOT be empty! Please insert a valid sensorID.")
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        raise HTTPException(status_code=404, detail=f"No sensor with ID: '{sensorID}' was found in the database")
    if session.exec(select(BlockDB)).all().__len__() == 0:
        #_sID = session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).one().id
        newBlock = BlockBase
        newBlock.blockID = blockID
        newBlock.sensorID = sensorID
        newBlock.id = None
        _b = BlockBase.model_validate(newBlock)
        _bDB = BlockDB.model_validate(_b)
        session.add(_b)
        session.commit()
        session.refresh(_b)

        session.add(_bDB)
        session.commit()
        session.refresh(_bDB)

        return _b
    else:
        if session.exec(select(BlockDB).where(BlockDB.blockID==blockID)).first():
            raise HTTPException(status_code=406, detail=f"Block with blockID: '{blockID}' already exist in the database! Please use free blockID.")
        else:

            _list = session.exec(select(BlockBase)).all()
            for x in _list:
                if x.sensorID == sensorID:
                    raise HTTPException(status_code=406, detail=f"Sensor with id: '{sensorID}' already has a block attached to it. Try a different sensor.")
                    continue
            newBlock = BlockBase
            newBlock.blockID = blockID
            newBlock.sensorID = sensorID
            newBlock.id = None
            _b = BlockBase.model_validate(newBlock)
            _bDB = BlockDB.model_validate(_b)
            session.add(_b)
            session.commit()
            session.refresh(_b)

            session.add(_bDB)
            session.commit()
            session.refresh(_bDB)

            return _b
        
#Lisää anturi lohkoon()
def add_sensor(session: Session, sensorID: str, blockID: str):
    if sensorID == None:
        raise HTTPException(status_code=406, detail="sensorID CANNOT be empty! Please insert a valid sensorID.")
    if not session.exec(select(SensorDB).where(SensorDB.sensorID==sensorID)).first():
        raise HTTPException(status_code=404, detail=f"No sensor with ID: '{sensorID}' was found in the database")
    if not session.exec(select(BlockDB).where(BlockDB.blockID==blockID)).first():
        raise HTTPException(status_code=404, detail=f"There is no block with blockID: '{blockID}' in the database! Maybe try adding new block with that blockID.")
    
    _list = session.exec(select(BlockBase)).all()
    for x in _list:
        if x.sensorID == sensorID:
            raise HTTPException(status_code=406, detail=f"Sensor with id: '{sensorID}' already has a block attached to it. Try a different sensor.")
        continue
        
    
    newBlock = BlockBase
    newBlock.sensorID = sensorID
    newBlock.blockID = blockID
    newBlock.id = None

    _b = BlockBase.model_validate(newBlock)
    session.add(_b)
    session.commit()
    session.refresh(_b)

    return _b

#Listaa lohkon anturit()
def list_sensors(session: Session, blockID: str):
    if not session.exec(select(BlockDB).where(BlockDB.blockID==blockID)).first():
        raise HTTPException(status_code=404, detail=f"There is no block with blockID: '{blockID}' in the database! Maybe try adding new block with that blockID.")
    _sensors = session.exec(select(BlockBase).where(BlockBase.blockID==blockID)).all()
    result = []
    _sDB = session.exec(select(SensorDB)).all()
    for _s in _sensors:
        for _db in _sDB:
            if _db.sensorID == _s.sensorID:
                result.append(_db)
                break
            else:
                continue
    return result