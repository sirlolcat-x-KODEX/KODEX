# CODEX/endpoints/__init__.py

import os
import importlib.util

# Define list of endpoint modules
ENDPOINTS = [
    'telegram_endpoint',
]

# Import all endpoint modules dynamically
for endpoint in ENDPOINTS:
    spec = importlib.util.spec_from_file_location(endpoint, os.path.join(os.path.dirname(__file__), f'{endpoint}.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
