import pytest


@pytest.fixture()
def invalid_values():
    return ["35155",
            "6546 4568 6548 3215",
            "aaaabbbbccccdddd",
            "aaaa1111bbbb2222",
            "",
            "654564256546486565233",
            "6546 6554 6554 6542 3254",
            "aaaabbbbccccddddeeee"
            "aaaa1111bbbb2222cccc"
            ]


@pytest.fixture()
def invalid_types():
    return [1111222233334444,
            111122------3333]