from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoUpdate(BaseModel):  
    title: str | None = None  
    completed: bool | None = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    class Config:
        orm_mode = True