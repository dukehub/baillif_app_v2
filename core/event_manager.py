from typing import Callable, Dict, List
from helpers.logger import logger

class EventManager:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Abonne une fonction callback à un événement"""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)
        logger.debug(f"Abonnement à l'événement {event_name}")

    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """Désabonne une fonction callback d'un événement"""
        if event_name in self._subscribers and callback in self._subscribers[event_name]:
            self._subscribers[event_name].remove(callback)
            logger.debug(f"Désabonnement de l'événement {event_name}")

    def emit(self, event_name: str, *args, **kwargs) -> None:
        """Émet un événement avec les arguments donnés"""
        if event_name in self._subscribers:
            for callback in self._subscribers[event_name]:
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Erreur lors de l'exécution du callback pour {event_name}: {str(e)}")
        logger.debug(f"Émission de l'événement {event_name}")

# Instance singleton
_instance = EventManager()

def subscribe(event_name: str, callback: Callable) -> None:
    """Abonne une fonction callback à un événement"""
    _instance.subscribe(event_name, callback)

def unsubscribe(event_name: str, callback: Callable) -> None:
    """Désabonne une fonction callback d'un événement"""
    _instance.unsubscribe(event_name, callback)

def emit(event_name: str, *args, **kwargs) -> None:
    """Émet un événement avec les arguments donnés"""
    _instance.emit(event_name, *args, **kwargs)
