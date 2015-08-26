# -*- coding: utf-8 -*-
import sys , os
from copy import deepcopy
from random import randint, choice, random

#--------------------------- READ CNF FILE ----------------------------------
def readCnf(cnfFile):
	clauses=[]
	nbL=0
	with open(cnfFile) as f:
 		for clause in enumerate(f):
			c=clause[1].strip('\n').strip('\r').strip('\n').split(" ")
			c = filter(None,c)
			if 'p' in c :
				nbL=int(c[-2])
			elif not ( 'c' in c) and len(c)>1:
				clauses.append(map(int,(c[:-1])))

	return clauses, nbL

#----------------------------- RANDOM SOLUTION -------------------------------------------
def random_sol(nbL):
	l = []
	for x in range(1,nbL+1):
		sign = randint(0,1)
		if sign:
			l.append(x)
		else :
			l.append(-x)

	return l

#------------------------------- CHECK ---------------------------------
def check_all(clause,etat):
	clauses = deepcopy(clause)
	# print etat
	for l in etat:
		i=0
		while i < len(clauses):
			if l in clauses[i]:
				clauses.remove(clauses[i])
			else:
				i=i+1
	return len(clauses)

#----------------------------- TS ---------------------------------------
	
def ts(clauses,nbL,nbC):
	l=random_sol(nbL)
	val = check_all(clauses[:],l)
	bestL = l
	bestVal = val

	a = 1
	tt=[0]*nbL

	for iteration in range(100):
		ameliorant=False
		if (val==0):
			print "SOLUTION FOUND"
			print bestVal
			print bestL
			return bestVal, bestL

		k = (nbC-val)/float(nbC)

			
		x = 0

		val=1000000

		while x < nbL and val != 0:
			neighbor = deepcopy(l)
			neighbor[x] = neighbor[x] * (-1)
			new_val = check_all(clauses[:],neighbor)

			if not(tt[x]>0):
				if (new_val < val):
					pos = x
					val = new_val
			x = x+1

		if tt[pos]==0:
			tt[pos]=4
			l[pos] = l[pos] * (-1)
			val=check_all(clauses[:],l)


		for i in range(nbL):
			if tt[i]>0:
				tt[i]=tt[i]-1
		
		if val<bestVal:
			bestL=l
			bestVal=val


	print bestVal
	print bestL
	return bestVal, bestL


