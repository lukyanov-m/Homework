def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей с процессами по состоянию их выполнения"""
    list_by_status = []
    for one_dict in list_dict:
        if one_dict["state"] == state:
            list_by_status.append(one_dict)
    return list_by_status


def sort_by_date(list_dict: list, rev_sort: bool = True) -> list:
    """Функция сортирует список словарей с процессами по времени"""
    list_by_date = sorted(list_dict, key=lambda one_dict: one_dict["date"], reverse=rev_sort)
    return list_by_date
