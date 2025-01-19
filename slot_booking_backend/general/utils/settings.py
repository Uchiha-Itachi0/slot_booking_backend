import os

from .misc import yaml_coerce


def get_setting_from_environment(prefix):
    """
    Extracts and converts environment variables with a specified prefix into a dictionary.

    This function filters environment variables that start with the given `prefix`, removes
    the prefix from their names, and converts their values into appropriate Python types
    using the `yaml_coerce` function. The resulting dictionary contains the stripped names
    as keys and the coerced values as their respective values.

    Parameters:
    - prefix (str): The prefix to filter environment variables.

    Returns:
    - dict: A dictionary of environment variables with the prefix removed from their names
      and their values converted to appropriate Python types.

    Example:
    >>> import os
    >>> os.environ['MYAPP_PORT'] = '8080'
    >>> os.environ['MYAPP_DEBUG'] = 'true'
    >>> get_setting_from_environment("MYAPP_")
    {'PORT': 8080, 'DEBUG': True}
    """
    prefix_len = len(prefix)

    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
