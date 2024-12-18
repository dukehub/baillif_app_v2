
from core.state_manager import StateManager
from core.data_manager import DataManager

# Create single instances of managers
state_manager = StateManager()  # Create state_manager first
data_manager = DataManager()    # Then data_manager which uses state_manager



__all__ = ['data_manager', 'state_manager']