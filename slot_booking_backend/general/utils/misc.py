import yaml


def yaml_coerce(value):
    """
    Coerces a string value into its appropriate Python type using YAML parsing.

    This function takes a string input and attempts to convert it to its corresponding
    Python type (e.g., integer, float, boolean) by parsing it through YAML. If the input
    is not a string, it returns the input as is.

    Parameters:
    - value (str or any): The value to be coerced. If it is a string, it will be
      parsed using YAML to determine its actual type.

    Returns:
    - any: The coerced value with the appropriate Python type if the input was a string,
      otherwise returns the input unchanged.

    Example:
    >>> yaml_coerce("123")
    123
    >>> yaml_coerce("true")
    True
    >>> yaml_coerce("3.14")
    3.14
    >>> yaml_coerce(123)
    123
    >>> dict_str = "{'key1': '10', 'key2': 'true', 'key3': '3.14'}"
    >>> coerced_dict = yaml_coerce(dict_str)
    >>> print(coerced_dict)
    {'key1': 10, 'key2': True, 'key3': 3.14}

    """
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
