from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_data_for_processing, expected_if_state_executed):
    assert filter_by_state(list_data_for_processing) == expected_if_state_executed


def test2_filter_by_state(list_data_for_processing, expected_if_state_canceled):
    assert filter_by_state(list_data_for_processing, state="CANCELED") == expected_if_state_canceled


def test_empty_list():
    assert filter_by_state([]) == []


def test_if_no_required_key(expected_if_state_canceled):
    assert filter_by_state(expected_if_state_canceled) == []


def test_error_key(list_data_for_processing):
    assert filter_by_state(list_data_for_processing, state="error") == []


def test_sort_by_date(list_data_for_processing, expected_for_sort_by_date):
    assert sort_by_date(list_data_for_processing) == expected_for_sort_by_date


def test_sort_by_date_revers(list_data_for_processing, expected_for_sort_by_date_revers_false):
    assert sort_by_date(list_data_for_processing, reverse=False) == expected_for_sort_by_date_revers_false