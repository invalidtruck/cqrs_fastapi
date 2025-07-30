from typing import Any, Dict


class CommandBus:
    def __init__(self):
        self._handlers: Dict[str, Any] = {}

    def register_handler(self, command_type: str, handler: Any):
        if command_type in self._handlers:
            raise ValueError(
                f"Handler for command type '{command_type}' is already registered."
            )
        self._handlers[command_type] = handler

    async def dispatch(self, command: Any):
        handler = self._handlers.get(type(command))
        if not handler:
            raise ValueError(
                f"No handler registered for command type '{type(command).__name__}'."
            )
        return await handler.handle(command)
