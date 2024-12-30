from .state_manager import StateManager
from .data_manager import DataManager
from .event_manager import EventManager
  # Then data_manager which uses state_manager

data_manager = DataManager()
state_manager = StateManager()
event_manager = EventManager() 
data_manager.set_state_manager(state_manager)

__all__ = ['data_manager', 'state_manager', 'event_manager']