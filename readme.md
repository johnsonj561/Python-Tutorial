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


