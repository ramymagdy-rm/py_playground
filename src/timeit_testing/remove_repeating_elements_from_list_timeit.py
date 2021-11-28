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

import timeit

# code snippet whose execution time is to be measured
fromkeys_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is',
'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
test_list = list(dict.fromkeys(test_list))
'''

for_iter_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is',
'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
res = list()
for item in test_list:
    if item not in res:
        res.append(item)
'''

for_iter_one_line_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is',
'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
res = list()
[res.append(item) for item in test_list if item not in res]
'''.format()

list_set_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is',
'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
test_list = list(set(test_list))
'''

# timeit statement
print(timeit.timeit(stmt=fromkeys_code, number=10000))
print(timeit.timeit(stmt=for_iter_code, number=10000))
print(timeit.timeit(stmt=for_iter_one_line_code, number=10000))
print(timeit.timeit(stmt=list_set_code, number=10000))
