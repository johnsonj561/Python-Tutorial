### Levin-Cook Theorem:
1. SAT is in NP Complete
2. 3SAT is in NP Complete

Clearly, 3SAT can be reduced to SAT in polynomial time through the identify function, because 3SAT is already in instance of SAT

Claim: SAT can be reduced to 3SAT in polynomial time.
1. If a clause in SAT has less than 3 variables:
   Increase length of clause to 3 by adding disjunctive terms equivalent to 1st term
   (x) == (x OR x) == (x OR x OR x)
   (x OR y) == (x OR y OR x) 
1. If a clause in SAT has more than 3 variables:
   Recursively create clauses of size 3 from the long clause, i.e.
   (x OR y OR C) == (x OR y OR w) AND (!w OR C)
   The introduction of variable w and it's negation create an equivalent statement
   For any given assignment, let w = (!x AND !y)
   If x and y are both 0, allow w to be 1
   (x OR y OR w) AND (!w OR C) ==> TRUE AND (!w OR C)
   If x or y is 1, allow w to be 0
   (x OR y or W) AND (!w or C) ==> TRUE AND (0 OR C)
   Clearly, this mapping creates an equivalent boolean equation.
    
