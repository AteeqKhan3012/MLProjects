word_count={'hello':3,'world':5,'python':10}
print(word_count)
word_count.update({'programming':7})
print(word_count)
word_count['python']=2
print(word_count)
word_count.pop('world')
print(word_count)
print('hello' in word_count)
print(word_count)
