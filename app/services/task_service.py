from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        title=task.title,
        description=task.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(db: Session, task_id: int, task: TaskUpdate):
    existing_task = get_task_by_id(db, task_id)
    if not existing_task:
        return None
    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.completed is not None:
        existing_task.completed = task.completed
    db.commit()
    db.refresh(existing_task)
    return existing_task

def delete_task(db: Session, task_id: int):
    existing_task = get_task_by_id(db, task_id)
    if not existing_task:
        return None
    db.delete(existing_task)
    db.commit()
    return existing_task