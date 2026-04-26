from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session
from ..db.models import BlockDB, BlockBase
from ..crud import block_crud as crud
from ..db.database import get_session

router = APIRouter(prefix="/blocks", tags=["blocks"])

@router.post("/add-block/sensorID={sensorID}&blockID={blockID}", response_model=BlockBase, description="")
def add_block(sensorID: str, blockID: str, session: Session = Depends(get_session)):
    return crud.add_block(session, sensorID, blockID)

@router.post("/add-sensor/sensorID={sensorID}&blockID={blockID}", response_model=BlockBase, description="")
def add_sensor(sensorID: str, blockID: str, session: Session = Depends(get_session)):
    return crud.add_sensor(session, sensorID, blockID)