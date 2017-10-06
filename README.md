-----
## Python Tutorial Notes Summarizing Content From Tutorials Point
- https://www.tutorialspoint.com/python/
- Justin Johnson
-----

### Overview
- interpreted
- interactive
- object oriented
- high level
- created by Guido Rossum between 1985 - 19990
- available under GNU GPL

-----

### Identifiers
- case sensitive
- beginning with underscore _ denotes private
- beginning with 2 undercores __ denotes strongly private
- beginning with 2 underscores and ending with 2 underscores denotes language defined special name
```python
_fname		# private
__lname		# strongly private, achieves privacy by mangling name
__init__	# language defined special name

-----

### Indentation
- python provides now braces to indicate blocks of code
- all statements within the block must be indented the same amount

-----

### Lines & Spaces
- line continuation char (\\) denotes a continued line
```python
total = item_one + \
	item_two + \  
 	item_three  
```
- triple quotes are used to span string across multi line
- semi colon can be used to place multiple statements on the same line

-----

### Suites
- group of individual statements which make a single code block  
- if/while/def/class require a header line and a suite  
```python
	if expression:		# header  
		suite		# suite  
	elif expression:	# header  
		suite		# suite  
	else:			# header  
		suite		# suite  
```

-----

### Standard Data Types
- Numbers  
	- supports int, long, float, complex
- String  
- List  
	- similar to array, but each item of list can be of different data type
- Tuple  
	- sequential data type, # of values separated by commas, enclosed with parenthesis
	- considered as a 'read only list'
- Dictionary  
	- key value pairs, similar to associative array or hash table
	- unordered

- you can delete reference to a number object using the del statement
	del var1[,var2[,...,varN]]

-----

### Data Type Conversion
- use type name as a function to perform cast, ex) int(x) converts x to int
- repr(x) converts x to an expression string
- eval(str) evaluates string and returns an object
- set(s) converts x to a set
- frozenset(x) converts x to frozen set
- chr(x) converts x to character
- unichr(x) converts x to unicode character
- ord(x) converts single char to its integer value

-----

### Truthy/Falsey
- any non-zero and non-null values are considered as True
- zero or null are assumed as False

-----

### If statement
- if suite of if clause is single line it may go on same line as header
```python
if (a === 5): print 'Hello'
```
-----

### Loop Control
- break statement - terminates loop
- continue statement - skips remainder of loop body and return to conditional of next iteration
- pass statement - used when statement is required byt you do not want any command or code to execute

-----

### Math Functions
- abs(x)
- ceil(x)
- cmp(x,y) -1 if x < y, 0 if x == y, or 1 if x > y
- exp(x)
- fabs(x) absolute value of x
- floor(x)
- log(x)
- log10(x)
- max(x, y)
- min(x, y)
- modf(x) fractional and integer parts of x in a two item tuple
- pow(x,y)
- round(x, [,n]) x rounded to n digits from decimal point
- sqrt(x)

-----

### Random Numbers
- choice(seq) returns random item from list, tuple, or string
- randrange([start,] stop [,step]) randomly selected element from range(start, stop, step)
- random() a random float r such that 0 <= r <= 1
- seed([x]) sets integer starting value used in generating random numbers
- shuffle(lst) randomizes the items of a list in place
- uniform(x, y) random float r such that x is less than or equal to r and r is less than y


### Escape Characters
\a	bell or alert  
\a	backspace  
\cx	control-x  
\e	escape  
\f	formfeed  
\n 	newline  
\r	cariage return  
\s	space  
\t	tab  
\v	vertical tab  
r/R	raw string - supresses actual meaning of escaped characters	  
	ex) print r'\n' prints \n , not a new line  

### String Formatting
%	string format operator  
%c	character  
%s	string conversion  
%i	signed int  
%d	signed int  
%u	unsigned int  
%o	octal  
%e	exponential notation  
%f	floating point real  
<sp>	leave a blank space before positive number   
0	pad from left with zeros (instead of spaces)  
m.n	m is the min total width and n is number of digits to display after decimal point  

- normal strings stored internally as 8 bit ascii  
- unicode strings stored as 16 bit unicode, larger set of characters  
	denoted with a preceding letter u , ex) u'Hello World'  

### Built in String Methods
capitalize()  
center(width, fillchar) - returns a space padded string with original string centered to a total of width columns  
count(str, beg=0, end=len(str)) - returns total occurences of str within substring  
decode(encoding)  
encode(encoding)   
endswith(suffic, beg=0, end=len(str)) - returns true if substring ends with suffix  
expandtabs(tabsize=8) - expands tabs in string to multiple spaces  
find(str, beg=0, end=len(str)) - returns starting index of str, or -1 if does not exist  
isalnum() - returns true if string has at least 1 character and all characters are alphanumeric  
isalpha() - returns true if string has at least 1 character and all characters are alphabetic  
isdigit()  
islower()  
isnumeric()  
isspace()  
istitle()  
isupper()  
join(seq) - merge string representations of elements in a sequence into a string  
len(string)  
ljust(width[, fillchar]) - returns space padded string with orig string left justified  
lower()  
lstrp() - removes leading whitespace in string  
maketrans() - returns translation table to be used in translate function  
max(str) - returns max alphabetical char from string  
min(str) - returns min alpha char  
replace(old, new [, max]) - replaces all occureneces of old with new, or at most max occurences if max deined  
rfind(str, beg=0, end=len(str)) - same as find, but searches backwards  
rjust(width [, fillchar])  
rstrip()  
split(str="", num=string.count(str)) - splits string according to delimeter str (or space), returns list of substrings, split inti at most num substrings  
splitlines(num=string.count('\n')) - splits string at all newlines  
startswith(str, beg=0, end=len(str))  
strip([chars])  
swapcase()  
title() - returns titlecased version of string  
upper()  
zfill(width) - intended for numbers, returns leftpadded original string  
isdecimal()  

### List Operations
len(list) - length  
[1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]  
['hi'] * 2 = ['hi', 'hi']  
3 in [1, 2, 3] = true  
for x in [1, 2, 3] - iterates list  
cmp(list1, list2)  
max(list)  
min(list)  
list(seq) - converts tuple into list  

### List Methods
append(obj) - appends object to list  
count(obj) - returns count of how many time obj occurs in list  
extend(seq) - appends contents to list  
index(obj) - returns lowest index in list that obj appears  
pop(obj=list[-1]) - removes and returns last object from list  
remove(obj) - removes object from list  
reverse()  
sort([func]) - sorts objects of list, use compare func if given  

### Tuples
- sequence of immutable python objects, wrapped in parenthesis instead of brackets  
- any set of multiple objects that are comma separated and have no identifying symbols, default to tuples  
  ex) 'abc', 1, 5.56, 'hello', 'world will default to a tuple  

### Tuple Functions
cmp(tuple1, tuple2)  
len(tuple)  
max(tuple)  
min(tuple)  
tuple(seq) converts list into a tuple  

### Dictionary
- unique keys map to values  
- dictionary values have no restriction, may be any python value  

### Dictionary Methods
clear() - removes all elements  
copy() - returns shallow copy  
fromekeys() - creates new dictionary with keys from seq and values set to value  
get(key, default=None)  
has_key(key)  
items() - returns list of dict's key,value tuple pairs  
keys()  
setdefault(key, default=None)  
update(dict2) - adds dict2s key value pairs to dict1  
values()   
