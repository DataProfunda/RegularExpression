import re
import os

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900--555--1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

CAT 
MAT 
PAT
BAT
cat
mat
pat
bat


'''

ddelo = '''
C85
C123
B42
U36
C192
'''

pattern = re.compile(r'\d\d?\d?')

matches = pattern.finditer(ddelo)

for match in matches:
    print(match)


#Search for patterns in text

#1. Raw string

'''

print('\tHello World')

print(r'\tHello World') #Raw string

'''

#2.

'''

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
print(text_to_search[1:4])

'''

#3. MetaCharacters
'''

pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
pattern = re.compile(r'coreyms\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
pattern = re.compile(r'\.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
   
'''
    
#4. Numbers
'''
pattern = re.compile(r'\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
pattern = re.compile(r'\D')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
'''

#5. Boundary

'''

pattern = re.compile(r'\bHa')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)   
    
pattern = re.compile(r'\BHa')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
    
'''

#6. ^  and $

'''

sentence = 'This is sentence'
  
pattern = re.compile(r'^This')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)  
    
pattern = re.compile(r'^is')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)  
    

pattern = re.compile(r'sentence$')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)  
    
'''

#7. 

'''

pattern = re.compile(r'\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
    
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
  '''
  
  
  
#8.


path = r'C:\Users\koste\OneDrive\Pulpit\Korki\Korepetycje\Bibliotheki\Regular-Expressions'.replace('\\','/') 
#print(path)    
'''
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')

with open(os.path.join(path, 'data.txt'), 'r') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)  
    


'''

#9.

'''

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
'''
'''
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  

'''
'''
#10.

pattern = re.compile(r'[a-zA-Z]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  

pattern = re.compile(r'[^a-zA-Z]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  

'''

'''
#11.
pattern = re.compile(r'[^c]at')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
    
pattern = re.compile(r'(p|c|m|b")at')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
  '''  
    
#12.
'''
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
    
    '''
    
#13.
'''
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  
    
    '''    

'''

#12.



#pattern_regex = r'\d\d\d[*.]\d\d\d[*.]\d\d\d'

pattern_regex = r'M(r|rs)\.?\s[A-Z]\w*'
pattern = re.compile(pattern_regex)

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#print(text_to_search[1:4])

#with open('C:/Users/koste/OneDrive/Pulpit/Korki/code_snippets/Python-Regular-Expressions/data.txt', 'r', encoding='utf-8') as f:
 #   contents = f.read()
    
  #  matches = pattern.finditter(text_to_search)
    
   # for match in matches:
    #    print(match)    
    
'''

