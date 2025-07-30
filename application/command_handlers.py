from datetime import datetime
from commands.user_commands import CreateUserCommand
from domain.models import User, UserCreatedEvent
from infrastructure.repositories import InMemoryRepository
import uuid


class CreateUserCommandHandler:
    
    
    
    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    async def handle(self, command: CreateUserCommand):
        user_id = str(uuid.uuid4())
        current_time= datetime.now()
        event = UserCreatedEvent(
            event_id=str(uuid.uuid4()),
            user_id=user_id,
            name=command.name,
            email=command.email,
            timestamp=current_time,
        )
        await self.repository.save_event(event)
        return User(
            id=user_id,
            name=command.name,
            email=command.email,
            created_at=event.timestamp,
        )
