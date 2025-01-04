from typing import Callable, Dict, List
from helpers.logger import logger

class EventManager:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Abonne une fonction callback à un événement"""
        logger.debug(f"EventManager: Nouvel abonnement à {event_name} depuis {callback.__self__.__class__.__name__}")
        if event_name not in self._subscribers:
            self._subscribers[event_name] = set()
        self._subscribers[event_name].add(callback)
        logger.debug(f"EventManager: Total abonnés pour {event_name}: {len(self._subscribers[event_name])}")

    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """Désabonne une fonction callback d'un événement"""
        if event_name in self._subscribers and callback in self._subscribers[event_name]:
            logger.debug(f"EventManager: Désabonnement de {event_name} pour {callback.__self__.__class__.__name__}")
            self._subscribers[event_name].remove(callback)
            logger.debug(f"EventManager: Total abonnés restants pour {event_name}: {len(self._subscribers[event_name])}")

    def get_subscribers_count(self, event_name: str) -> int:
        """Retourne le nombre d'abonnés pour un événement"""
        return len(self._subscribers.get(event_name, set()))

    def debug_subscribers(self) -> None:
        """Affiche les informations de débogage sur les abonnements"""
        for event_name, subscribers in self._subscribers.items():
            logger.debug(f"EventManager: Événement '{event_name}' a {len(subscribers)} abonné(s)")

    def emit(self, event_name: str, *args, **kwargs) -> None:
        """Émet un événement aux abonnés"""
        logger.debug(f"EventManager: Émission de {event_name}")
        if event_name in self._subscribers:
            subscribers = list(self._subscribers[event_name])  # Copie pour éviter les modifications pendant l'itération
            logger.debug(f"EventManager: {len(subscribers)} abonnés pour {event_name}")
            for callback in subscribers:
                try:
                    logger.debug(f"EventManager: Appel de {callback.__self__.__class__.__name__}.{callback.__name__}")
                    callback(*args, **kwargs)
                except Exception as e:
                    logger.error(f"EventManager: Erreur lors de l'appel de {callback.__self__.__class__.__name__}.{callback.__name__}: {e}")
        else:
            logger.warning(f"EventManager: Aucun abonné pour {event_name}")

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
