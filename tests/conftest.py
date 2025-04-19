import pytest


@pytest.fixture()
def invalid_values():
    return ["35155",
            "654564256546486565233",
            "6546 4568 6548 3215",
            "6546 6554 6554 6542 3254",
            "aaaabbbbccccdddd",
            "aaaa1111bbbb2222",
            ""
            ]


@pytest.fixture()
def invalid_types():
    return [1111222233334444,
            111122------3333]