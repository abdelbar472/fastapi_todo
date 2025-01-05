from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[UUID]
    title: str
    description: str
    status: str = "pending"
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
