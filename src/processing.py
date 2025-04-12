def filter_by_state(list_dict: list, state: str="EXECUTED") -> list:
    """Функция фильтрует список задач по статусу их выполнения"""

    new_list_for_state = []
    for one_dict in list_dict:
        if one_dict["state"] == state:
            new_list_for_state.append(one_dict)
    return new_list_for_state
