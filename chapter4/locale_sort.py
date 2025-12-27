import locale

my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale) # pt_BR.UTF-8
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits) # ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']
# not correct sorted, because using MacOS 
# but this is correct way, u need to change the locale when starting u script (app)


'''
import pyuca

coll = pyuca.Collator()
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)
'''

