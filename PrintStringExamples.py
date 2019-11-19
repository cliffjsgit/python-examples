# Print formated string examples
#  https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# "Python 3's f-Strings: An Improved String Formatting Syntax (Guide)"
#  https://realpython.com/python-f-strings/ 

# 1. String Concatenation
# Traditional print string formating using String Concatenation:
# Difficult to read and easy to make a mistake, especially with missing spaces

print('1. String contactenation example:')
animals = "dogs"
population = 3
city = "Palo Alto"
print("There are " + str(population) + " " + animals + " in " + city + ".")

#Output:  There are 3 dogs in Palo Alto. 

# ----------------------------------------------------------------------------
# 2. Older String Substitution Operator
# String substition using the string "%" operator can help to reduce errors:
# Readable but using several longer strings and format parameters 
# quickly become much less readable. 

print()
print('3. String substitution operator(%) example:')
print('There are %s %s in %s.'%(population, animals, city))


# ----------------------------------------------------------------------------
# 3. Custom String Formatting with format() Method 
# Using newer str.format() method (Formatter class) added in Python 2.6
# Includes optional numbering (0 origin) or naming the data ,
# and multiple use of the same data. 

print()
print('2. Using str.format() method example:')
print('There are {}, {}, {}.'.format(population, animals, city))
print('In {2}, there are {0} {1}.'.format(population, animals, city))
      

# ----------------------------------------------------------------------------
# 4. Formatted String Literals (or f-strings for short))
# f-strings were introducted with Python 3.6 / 3.7
# https://docs.python.org/3/tutorial/inputoutput.html

print()
print('4. f-string format example:')
print(f'There are {population} {animals} in {city}.')





# -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -  - -  -  -  -
# 5. Python.org doc: Examples of Using format specifiers
# 
print()
print('5. Python.org Format Specifier string syntax examples: ')
print('https://docs.python.org/3.7/library/string.html#format-string-syntax')
print('https://docs.python.org/3.7/library/string.html#formatexamples')

import math
print()
print('Examples of using a format specifier:')
print('Without a format specifier:',
      '\n  The value of pi is ' + str(math.pi) + '.')
print('Old string concatenation with the format function:',
      '\n  The value of pi is approximately', format(math.pi, '.3f') + '.')
print('String substitution operator "%" with format:',
      '\n  The value of pi is approximately %.3f.' % (math.pi) )
print('String formating with string.format() method:',
      '\n  The value of pi is approximately {:.3f}.'.format(math.pi))
print('f-string with format:',
      f'\n  The value of pi is approximately {math.pi:.3f}.')
	  
