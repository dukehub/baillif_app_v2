from PySide6.QtCore import QObject, Signal
from typing import Dict, Any, List, Optional
from threading import Lock

class StateManager(QObject):
    """
    A singleton class that manages the application's state.
    Provides a centralized way to manage and access application state.
    """
    _instance = None
    state_changed = Signal(str, object)  # Signal emitted when state changes (key, new_value)
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            super().__init__()
            self._state: Dict[str, Any] = {}
            self._subscribers: Dict[str, List[callable]] = {}
            self._lock = Lock()  # Ensure thread safety
            self._initialized = True
    
    def set_state(self, key: str, value: Any) -> None:
        """Set a state value and notify subscribers."""
        with self._lock:
            self._state[key] = value
            self.state_changed.emit(key, value)
            self._notify_subscribers(key, value)
    
    def get_state(self, key: str, default: Any = None) -> Any:
        """Get a state value."""
        with self._lock:
            return self._state.get(key, default)
    
    def subscribe(self, key: str, callback: callable) -> None:
        """Subscribe to state changes for a specific key."""
        if key not in self._subscribers:
            self._subscribers[key] = []
        if callback not in self._subscribers[key]:
            self._subscribers[key].append(callback)
    
    def unsubscribe(self, key: str, callback: callable) -> None:
        """Unsubscribe from state changes for a specific key."""
        if key in self._subscribers and callback in self._subscribers[key]:
            self._subscribers[key].remove(callback)
    
    def _notify_subscribers(self, key: str, value: Any) -> None:
        """Notify all subscribers for a specific key."""
        if key in self._subscribers:
            for callback in self._subscribers[key]:
                callback(value)
    
    def clear_state(self, key: Optional[str] = None) -> None:
        """Clear state for a specific key or all state if no key provided."""
        with self._lock:
            if key is None:
                self._state.clear()
            elif key in self._state:
                del self._state[key]
    
    def get_all_state(self) -> Dict[str, Any]:
        """Get a copy of the entire state."""
        with self._lock:
            return self._state.copy()
    
    def update_state(self, key: str, value: Dict[str, Any]) -> None:
        """Update part of a state if it is a dictionary."""
        with self._lock:
            if key in self._state and isinstance(self._state[key], dict):
                self._state[key].update(value)
                self.state_changed.emit(key, self._state[key])
                self._notify_subscribers(key, self._state[key])


