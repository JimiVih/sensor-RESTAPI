from sqlmodel import SQLModel, Field


class SensorBase(SQLModel):
    sensorID: str
    status: bool | None = Field(default=False) #Tulisi kysyä jotenkin anturilta
    #Anturilla on oma kuuntelu ja on samassa verkossa servun kanssa
    #Servu (eli tämä restAPI servu), voi kysyä statusta:
    #GET anturin-osoite/status
    #Anturinosoite on joko IP muodossa: 192.168.x.x/172.16.x.x
    #Tai sitten verkossa on oma DNS serveri ja anturin-osoite voi olla
    #Anturintunniste(esim. anturi_1 tai jokin merkkisarja)/status
class SensorDB(SensorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
class SensorCreate(SensorBase):
    pass
class SensorUpdate(SQLModel):
    status: bool | None = Field(default=False)

class DataBase(SQLModel):
    temp: float | None = Field(default=None)
    date: str | None = Field(default=None)
class DataDB(DataBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
class DataCreate(DataBase):
    pass

class BlockBase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    blockID: str
    sensorID: str
class BlockDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    blockID: str
    