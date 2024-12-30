from typing import Callable, Dict, List

class EventManager:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable) -> None:
        """
        Abonne une fonction callback à un type d'événement spécifique
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable) -> None:
        """
        Désabonne une fonction callback d'un type d'événement
        """
        if event_type in self._subscribers:
            self._subscribers[event_type].remove(callback)

    def emit(self, event_type: str, *args, **kwargs) -> None:
        """
        Émet un événement et appelle tous les callbacks associés
        """
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                callback(*args, **kwargs)
