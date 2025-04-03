from sqlalchemy.orm import Session
from . import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    new_task = models.Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    return db.query(models.Task).all()

from fastapi import HTTPException

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")  # Return proper error
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}  # Return a success message
