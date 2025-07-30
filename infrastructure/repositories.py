from typing import Dict, List, Optional
from domain.models import User, UserCreatedEvent
import uuid

class InMemoryRepository:
    """
    Un repositorio simple en memoria para demostración.
    Simula el almacenamiento de eventos y el modelo de lectura de usuarios.
    """
    def __init__(self):
        # Almacena eventos como una lista (simulando un Event Store muy básico)
        self._events: List[UserCreatedEvent] = []
        # Almacena usuarios como un diccionario (simulando un Read Model)
        self._users: Dict[str, User] = {}

    async def save_event(self, event: UserCreatedEvent):
        """
        Guarda un evento en el "Event Store" en memoria.
        En un CQRS real, esto sería una base de datos de eventos.
        """
        self._events.append(event)
        print(f"Evento guardado: {event.event_type} para usuario {event.user_id}")
        # Aquí, en un sistema real, se publicaría el evento a un Message Broker
        # para que los proyectores actualicen los modelos de lectura.
        # Para simplificar, actualizamos el modelo de lectura directamente aquí.
        self._update_read_model(event)

    def _update_read_model(self, event: UserCreatedEvent):
        """
        Actualiza el modelo de lectura basado en el evento.
        En un CQRS real, esto lo haría un "proyector" o "listener"
        que escucha los eventos del Event Store.
        """
        if event.event_type == "UserCreated":
            user = User(
                id=event.user_id,
                name=event.name,
                email=event.email,
                created_at=event.timestamp # Usamos el timestamp del evento
            )
            self._users[user.id] = user
            print(f"Modelo de lectura actualizado para usuario: {user.id}")

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Obtiene un usuario del modelo de lectura.
        """
        return self._users.get(user_id)

    async def get_all_users(self) -> List[User]:
        """
        Obtiene todos los usuarios del modelo de lectura.
        """
        return list(self._users.values())
