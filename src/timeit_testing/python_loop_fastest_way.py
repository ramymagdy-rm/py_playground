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

import numpy as np
import timeit


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += 1
        i += 1
    return s


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s


def for_loop_with_increment(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s


def for_loop_with_test(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n:
            pass
        s += i
    return s


def for_loop_with_test_and_increment(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n:
            pass
        i += 1
        s += i
    return s


def sum_range(n=100_000_000):
    return sum(range(n))


def sum_numpy(n=100_000_000):
    """
    external C executon
    :param n:
    :return:
    """

    return np.sum(np.arange(n), dtype=np.int64)     # datatype can affect the value


def sum_math(n=100_000_000):
    """
    mathematical equations
    :param n:
    :return:
    """

    return (n * (n - 1)) // 2


def main():
    # print("while loop\t\t", timeit.timeit(while_loop, number=1))                            # ~ 8.747103
    # print("pure for loop\t", timeit.timeit(for_loop, number=1))                             # ~ 5.339370
    # print("for inc\t\t\t", timeit.timeit(for_loop_with_increment, number=1))                # ~ 8.423486
    # print("for test\t\t", timeit.timeit(for_loop_with_test, number=1))                      # ~ 7.132444
    # print("for inc+test\t", timeit.timeit(for_loop_with_test_and_increment, number=1))      # ~ 10.07446
    # print("sum range\t\t", timeit.timeit(sum_range, number=1))                              # ~ 3.812655
    print("sum numpy\t\t", timeit.timeit(sum_numpy, number=1))                              # ~ 0.195402
    print("sum math\t\t", timeit.timeit(sum_math, number=1))                                # ~ 1.4000000000125024e-06


if __name__ == '__main__':
    main()
