from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal,engine
from .. import models,schemas,crud

models.Base.metadata.create_all(bind=engine)

router=APIRouter()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/",response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate,db:Session=Depends(get_db)):
    return crud.create_task(db=db, task=task)

@router.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)