def deep_update(base_dict, update_with):
    """
    Recursively updates the `base_dict` with values from `update_with`.

    If a key in both dictionaries contains a dictionary as its value, the function
    recursively updates the nested dictionaries. Otherwise, it replaces the value in
    `base_dict` with the value from `update_with`.

    Parameters:
    - base_dict (dict): The dictionary to be updated.
    - update_with (dict): The dictionary with updates to apply to `base_dict`.

    Returns:
    - dict: The updated dictionary.

    Example:
    >>> base_dict = {'a': 1, 'b': {'c': 2, 'd': 4}, 'e': 5}
    >>> update_with = {'b': {'c': 3, 'f': 6}, 'g': 7}
    >>> result = deep_update(base_dict, update_with)
    >>> print(result)
    {'a': 1, 'b': {'c': 3, 'd': 4, 'f': 6}, 'e': 5, 'g': 7}
    """
    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value

    return base_dict
