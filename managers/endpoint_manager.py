# codex/managers/endpoint_manager.py

import importlib

from typing import Union

from ..core import codex
from ..endpoints import ENDPOINTS
from .base_manager import BaseManager


class EndpointManager(BaseManager):
    def register_components(self):
        # Register endpoint modules dynamically
        for endpoint in ENDPOINTS:
            module = importlib.import_module(f'codex.endpoints.{endpoint}')
            client_class = getattr(module, 'Client')
            codex.register_endpoint(client_class())


def register_manager(manager: Union[BaseManager, None] = None):
    if not manager:
        manager = EndpointManager()
    manager.register_components()
