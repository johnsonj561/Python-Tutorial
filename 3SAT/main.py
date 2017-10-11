# Justin J
# Fall 2017
# Computational Complexity 
# Mapping SAT -> 3SAT


# Clause helper class
class Clause:

  def __init__(self, a, b, c):  
     self.a = str(a)
     self.b = str(b)
     self.c = str(c)
  
  def toString(self):
    return '( ' + self.a + ' + ' + self.b + ' + ' + self.c + ')'

# Convert any given clause, convert it to string of clauses with length 3
# Recursively calls itself until 3CNF is satisfied
def convertTo3SAT(clauseArray, wCount):
  # if clause has 3 variables, return its string representation
  if len(clauseArray) == 3:
    return Clause(clauseArray[0], clauseArray[1], clauseArray[2]).toString()  
  # if clause has more than 3 variables
  # introduce new variable w s.t w = 1 iff c[0] and c[1] both equal 0
  elif len(clauseArray) > 3:
    c1 = clauseArray[0]
    c2 = clauseArray[1]
    w = 'w' + str(wCount)
    # create a new clause with c1, c2, and our new w
    clauseToAdd = Clause(c1, c2, w)
    # insert !w into front of clauseArray
    clauseArray = ['!w' + str(wCount)] + clauseArray[2:]
    # return 3CNF as string and recurse on the long clauseArray
    return clauseToAdd.toString() + convertTo3SAT(clauseArray, wCount + 1)
  # if clause has less than 3 variables, add 1 or 2 variables until length 3 met
  while len(clauseArray) < 3:
    clauseArray.append(clauseArray[0])
  return clauseArray.toString()
  
# For simplification, let our long clause be represented in an array
longClause = ['x', 'y', '!r', 's', '!t', 'a', '!f', '!d', 'q']

result = convertTo3SAT(longClause, 1)

print'\nConverting instance of SAT into instance of 3SAT recursively...\n'
print '\nOriginal disjunctive clause variables:\n ' + str(longClause)
print '\n3SAT Result: \n' + result + '\n'
