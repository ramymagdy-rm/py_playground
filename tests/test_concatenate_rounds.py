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

from playground.card_games.card_games import concatenate_rounds


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
