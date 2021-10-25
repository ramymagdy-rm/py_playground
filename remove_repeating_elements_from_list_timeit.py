import timeit
 
# code snippet whose execution time is to be measured
fromkeys_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
test_list = list(dict.fromkeys(test_list))
'''

for_iter_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
res = list()
for item in test_list:
    if item not in res:
        res.append(item)
'''

for_iter_one_line_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
res = list()
[res.append(item) for item in test_list if item not in res]
'''

list_set_code = '''
test_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
test_list = list(set(test_list))
'''
 
# timeit statement
print (timeit.timeit(stmt = fromkeys_code, number = 10000))
print (timeit.timeit(stmt = for_iter_code, number = 10000))
print (timeit.timeit(stmt = for_iter_one_line_code, number = 10000))
print (timeit.timeit(stmt = list_set_code, number = 10000))
