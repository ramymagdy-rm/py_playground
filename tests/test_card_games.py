# MIT License
#
# Copyright (c) 2021 Ramy Ezzat
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from playground.card_games import get_rounds, concatenate_rounds, list_contains_round, card_average


@pytest.mark.parametrize("data, expected", [
        (0, [0, 1, 2]),
        (1, [1, 2, 3]),
        (10, [10, 11, 12]),
        (27, [27, 28, 29]),
        (99, [99, 100, 101]),
        (666, [666, 667, 668]),
])
def test_get_rounds(data, expected):
    assert get_rounds(data) == expected


def test_concatenate_rounds():
    data = [
        (([], []), []),
        (([0, 1], []), [0, 1]),
        (([], [1, 2]), [1, 2]),
        (([1], [2]), [1, 2]),
        (([27, 28, 29], [35, 36]), [27, 28, 29, 35, 36]),
        (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
    ]
    for variant, ((rounds_1, rounds_2), rounds) in enumerate(data, start=1):
        assert concatenate_rounds(rounds_1, rounds_2) == rounds


def test_list_contains_round():
    data = [
        (([], 1), False),
        (([1, 2, 3], 0), False),
        (([27, 28, 29, 35, 36], 30), False),
        (([1], 1), True),
        (([1, 2, 3], 1), True),
        (([27, 28, 29, 35, 36], 29), True),
    ]
    for variant, ((rounds, round_number), contains) in enumerate(data, start=1):
        assert list_contains_round(rounds, round_number) is contains


@pytest.mark.parametrize("data, expected", [
    ([1], 1.0),
    ([5, 6, 7], 6.0),
    ([1, 2, 3, 4], 2.5),
    ([1, 10, 100], 37.0),
])
def test_card_average(data, expected):
    assert card_average(data) == expected


def test_invalid_division():
    with pytest.raises(ZeroDivisionError):
        card_average([])


@pytest.mark.xfail
def test_dev_by_zero():
    assert 1 / 0 == 1
