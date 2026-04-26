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

#Listaa lohkon anturit()