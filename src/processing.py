def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список отфильтрованный по ключу state"""
    list_by_status = []
    for one_dict in list_dict:
        if one_dict["state"] == state:
            list_by_status.append(one_dict)
    return list_by_status


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Функция сортирует список словарей по времени указанному в словаре"""
    list_by_date = sorted(list_dict, key=lambda one_dict: one_dict["date"], reverse=reverse)
    return list_by_date
