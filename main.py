from fastapi import FastAPI, HTTPException, Depends
from typing import  List

from domain.models import User

from commands.user_commands import CreateUserCommand
from queries.user_queries import GetUserByIdQuery

from application.command_handlers import CreateUserCommandHandler
from application.query_handlers import GetUserByIdQueryHandler

from services.command_bus import CommandBus
from services.query_bus import QueryBus

from infrastructure.repositories import InMemoryRepository

app = FastAPI(title="App CQRS", description="Ejemplo", version="0.1.0")

in_memory_repo = InMemoryRepository()

create_user_handler = CreateUserCommandHandler(in_memory_repo)
get_user_by_id_handler = GetUserByIdQueryHandler(in_memory_repo)

query_bus = QueryBus()
query_bus.register_handler(GetUserByIdQuery, get_user_by_id_handler)
command_bus = CommandBus()
command_bus.register_handler(CreateUserCommand, create_user_handler)

def get_command_bus() -> CommandBus:
    return command_bus

def get_query_bus() -> QueryBus:
    return query_bus

@app.post("/users", response_model=User , status_code=201)
async def create_user(
    command: CreateUserCommand,
    cmd_bus: CommandBus = Depends(get_command_bus)
    ) -> User:
    try:
        user = await cmd_bus.dispatch(command)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@app.get("/users/{user_id}", response_model=User)
async def get_user_by_id(
    user_id: str,
    query_bus: QueryBus = Depends(get_query_bus)
) -> User:
    try:
        query = GetUserByIdQuery(user_id=user_id)
        user = await query_bus.dispatch(query)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users", response_model=List[User])
async def get_all_users(
    query_bus: QueryBus = Depends(get_query_bus)
) -> List[User]:
    try:
        users = await query_bus.dispatch(GetUserByIdQuery())
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


