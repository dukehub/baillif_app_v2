from core.data_manager import DataManager
from core.state_manager import StateManager

# Create single instances of managers
_state_manager = StateManager()  # Create state_manager first
_data_manager = DataManager()    # Then data_manager which uses state_manager

# Export the instances
state_manager = _state_manager
data_manager = _data_manager

__all__ = ['data_manager', 'state_manager']