from typing import Any, Dict


class QueryBus:
    def __init__(self):
        self._handlers: Dict[str, Any] = {}

    def register_handler(self, query_type: type, handler: Any):
        if query_type in self._handlers:
            raise ValueError(
                f"Handler for command type '{query_type.__name__}' is already registered."
            )
        self._handlers[query_type] = handler

    async def dispatch(self, query: Any):
        handler = self._handlers.get(type(query))
        if not handler:
            raise ValueError(f"No handler registered for query type '{type(query).__name__}'.")
        return await handler.handle(query)
