from queries.user_queries import GetUserByIdQuery
from domain.models import User
from infrastructure.repositories import InMemoryRepository
from typing import Optional, List

class GetUserByIdQueryHandler:
    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    async def handle(self, query: GetUserByIdQuery) -> Optional[User]:
        if  query.user_id:
            return await self.repository.get_user_by_id(query.user_id)
        else:
            return await self.repository.get_all_users()
        
        
        