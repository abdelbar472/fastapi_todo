from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime
from .database import get_db_session
from .models import Task

router = APIRouter()


@router.post("/tasks/")
def create_task(task: Task):
    session = get_db_session()
    task_id = uuid4()
    created_at = updated_at = datetime.utcnow()

    query = """
    INSERT INTO tasks (id, title, description, status, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (task_id, task.title, task.description, task.status, created_at, updated_at))

    return {"message": "Task created", "task_id": task_id}


@router.get("/tasks/")
def get_tasks():
    session = get_db_session()
    query = "SELECT * FROM tasks"
    rows = session.execute(query)
    tasks = [dict(row._asdict()) for row in rows]
    return {"tasks": tasks}


@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):
    session = get_db_session()
    updated_at = datetime.utcnow()

    query = """
    UPDATE tasks SET title = %s, description = %s, status = %s, updated_at = %s
    WHERE id = %s
    """
    session.execute(query, (task.title, task.description, task.status, updated_at, task_id))

    return {"message": "Task updated"}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    session = get_db_session()

    query = "DELETE FROM tasks WHERE id = %s"
    session.execute(query, (task_id,))

    return {"message": "Task deleted"}
