from tabu import readCnf, ts

filePath = 'example.cnf'
clauses,nbL=readCnf(filePath)
ts(clauses,nbL,len(clauses))
