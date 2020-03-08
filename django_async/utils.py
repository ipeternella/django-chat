"""
Module with utility functions for the django_chat project.
"""
import ast
import os
from typing import Any


def env2bool(env_var_name: str, default_var_value: Any) -> bool:
    """
    Evals env var strings as booleans. Accepts a default value.
    """
    env_var = os.getenv(env_var_name)

    if env_var is None:
        return default_var_value

    return ast.literal_eval(env_var)
