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

### Identifieers
- case sensitive
- beginning with underscore _ denotes private
- beginning with 2 undercores __ denotes strongly private
- beginning with 2 underscores and ending with 2 underscores denotes language sdefined special name

-----

### Indentation
- python provides now braces to indicate blocks of code
- all statements within the block must be indented the same amount

-----

### Lines & Spaces
- line continuation char (\) denotes a continued line
	- total = item_one + \
		  item_two + \
 		  item_three
- triple quotes are used to span string across multi line
- semi colon can be used to place multiple statements on the same line

-----

### Suites
- group of individual statements which make a single bcode block
- if/while/def/class require a header line and a suite
	if expression:		# header
		suite		# suite
	elif expression:	# header
		suite		# suite
	else:			# header
		suite		# suite

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
	if (a === 5): print 'Hello'

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
-	left justification
+	display the sign
<sp>	leave a blank space before positive number
0	pad from left with zeros (instead of spaces)
m.n	m is the min total width and n is number of digits to display after decimal point

- normal strings stored internally as 8 bit ascii
- unicode strings stored as 16 bit unicode, larger set of characters
	denoted with a preceding letter u , ex) u'Hello World'

### Built in String methods
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


### Date & Time
- time module available; time.time() returns ticks since epoch (Jan 1 1970 12:00am)  
- date arithmetic is easy with ticks, but dates before epoch and in future can not be represented in this way  
- future cutoff for unix and windows is around 2038    
- TimeTuple cosists of 9 numbers  
	(4 digit year, month, day, hour, minute,  
	second, day of week, day of year, daylight savings)  
- struct_time structure is equivalent 9 numbers   
	(tm_year, tm_mon, tm_mday, tm_hour, tm_min,  
	tm_sec, tm_wday, tm_yday, tm_isdst)  
- we can format time using asctime()  
```python
import time

timeSinceEpoch = time.time()
localTime = time.localtime(timeSinceEpoch)
formattedTime = time.asctime(localTime)    // Fri Sep 

```

- calendar module has methods for yearly/monthly calendars
```python
import calendar

cal = calendar.month(2008, 1)

print cal
```

- output:
```python
    January 2008
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
```

### Time Functions  
altzone() returns offset of local DST timezone, in seconds west of UTC  
asctime([tupletime]) returns readable 24 character formatted time string  
clock() returns CPU time as floating point number of seconds, useful for measuring computation costs  
ctime() similar to asctime()  
gmtime([secs]) returns a time tuple with UTC time  
localtime([secs]) returns time tuple with local time  
mktime(tupletime) returns floating point value representing time since epoch  
sleep(secs) suspends the calling thread for seconds  
strftime(fmt[,tupletime]) returns string representation    
time() returns current time since epoch float  
tzset() resets the time conversion rules used by the library routines    

### Calendar Functions  
calender(year,w=2,l=1c=6) returns multiline string representing calendar  
firstweekday() returns current setting for weekday that starts each week, 0 = Monday  
isleap() returns true if year is leap year  
leapdays(y1,y2) returns total number of leap days in the years within range y1 - y2  
month(year, month,w=2,l=1) returns multiline string with calendar for month of year  
monthcalendar(year,month) returns list of lists of ints, denoting weeks of month  
monthrange(year, month) returns 2 ints - code of weekday for first day of month, 2nd is nuber of days in the month  
prcal(year,w=2,l=1,c=6) like calendar(year,w,l,c)  
prmonth(year,onth,w=2,l=1) like month(year,month,w,l)  
setfirstweekday(weekday)  
timegm(tupletime)  
weekday(year,month,day) return weekday code for date  

### Other Time Modules
- datetime module  
- pytz module  
- dateutil module  

### Functions
- all arguments in Python are passed by reference  
```python
def foo(name, age):
  print name + ' ' + str(age)

# keyword params, order does not matter
foo(age=20, name='Justin')

# argument age has default value 25
def bar(name, age=25):
  print name + ' ' + str(age)

# varible length arguments are denoted with asterik * placed before the variable name
# the variable is tuple that remains empty if no additional args are specified
def printDetails(detail, *additionalDetails):
  print detail
  for d in additionalDetails:
    print d 
```
- anonymous functions are not defined, but are created using keyword lambda in place
- lambda return just one value, cannot contain multiple expressions
- anonmyous function cannot be a direct call to print because lamda requires an expression
- lamda functions have their own local namespace and cannot access variables not in param list or not on global namespace
```python
sum = lamda arg1, arg2: arg1 + arg2;

print 'Result: ', sum(10, 20)
print 'Result: ', sum(100, 200)
```
- return statement optionally passes back an expression to caller  
- return statement with no arguments is same as return None  

----- 

### Variable Scope
- variables defined inside a function body have local scope
- variables defined outside of a function body have global scope

-----

### Modules
- grouping related code into modules improves reuseability  
- module is Python object with arbitrarily named attributes that can be referenced  
- keyword import is used to import modules  
- keyword from allows the import of specific attributes from a module  
- Python interpreter searches for the module in:  
	- current directory    
	- if not found, then each directory in shell variable PYTHONPATH  
	- else Python checks the default path (usr/local/lib/python)  
- module search path is stored in system module sys.path variable  

-----

### Namespaces
- namespace is a dictionary of variable names (keys) and their correspondign values  
- Python statement can access variables in local namespace and in global namespace  
- if local namespace and global namespace have same name, then local variable will shadow global variable  
- Python assumes any variable assigned a value in a function is local  
- dir() returns sorted list of strings containing the names defined by a module  
	- list contains names of all modules, variables, and functions defined within the module  
```python
import math

content = dir(math)

print content
```
- Outputs:  
```python
['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan', 
'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 
'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
'sqrt', 'tan', 'tanh']
```
- globals() and locals() return the names in the given namespace based on where function is evoked    
- reload(mod_name) used to re-execute the modules code, as module code is only executed once when loaded  

-----

### Packages
- package is hierarchical file directory structure that defines a single Python application environment  
- consists of modules, subpackages, sub-subpackages, etc    
- consider a directory with multiple python files named MyModules   
	- in root of directory, create a file __init__.py such that it imports all components to be exposed  
	- then, the directory MyModules can be imported as 'import MyModules' and all individual files/components in MyModules/ will be made available  






	

