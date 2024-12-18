from .state_manager import state_manager

class StateServices:
    @staticmethod
    def set_current_client(client_data):
        """Set the current selected client in the state"""
        state_manager.set_state('current_client', client_data)

    @staticmethod
    def get_current_client():
        """Get the current selected client from the state"""
        return state_manager.get_state('current_client')

    @staticmethod
    def set_current_dossier(dossier_data):
        """Set the current selected dossier in the state"""
        state_manager.set_state('current_dossier', dossier_data)

    @staticmethod
    def get_current_dossier():
        """Get the current selected dossier from the state"""
        return state_manager.get_state('current_dossier')

    @staticmethod
    def clear_current_selections():
        """Clear all current selections"""
        state_manager.remove_state('current_client')
        state_manager.remove_state('current_dossier')

    @staticmethod
    def get_app_language():
        """Get the current application language"""
        return state_manager.get_state('current_language', 'fr')

    @staticmethod
    def set_app_language(language: str):
        """Set the application language"""
        state_manager.set_state('current_language', language)

    @staticmethod
    def get_app_theme():
        """Get the current application theme"""
        return state_manager.get_state('current_theme', 'default')

    @staticmethod
    def set_app_theme(theme: str):
        """Set the application theme"""
        state_manager.set_state('current_theme', theme)
