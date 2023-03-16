# codex/managers/base_manager.py

import abc


class BaseManager(abc.ABC):
    @abc.abstractmethod
    def register_components(self):
        pass
