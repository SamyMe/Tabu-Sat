This is an implementation of the [Tabu Search](https://en.wikipedia.org/wiki/Tabu_search) algorithm for the [Boolean Satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) (more precisely [max-sat](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem)).

The principle is to move from a solution *S* to the best of it's neighboors, while this later is not **tabu**.

###Principle:
* We defined **tabu** concept using a Tabu Tenure list *tt*.
* *tt* is simply a list of the same lenght *nbC* (number of clauses) as a state *S*.
* *tt* is initialised to all zeros. 
* while at a state *S*, we can move to a neighboor *N* by changing one bit (*i*) value only if the coresponding Tenure value is equal to zero (*tt[i]==0*). We then set it to a constant value (*4* is the default) so that for the next (4) iterations we won't be allowed to change that bit (we avoid sicling on terms).
* At each iteration, we decrease all non zero elements of *tt* by one.

###Usage
The algorithm takes as input: 

**ts** *(clauses,nbL,nbC)*
- clauses:	list of clauses (list of lists). A clause being a list of literal instences.
- nbL:		number of literals.
- nbC:		number of clauses.

And returns a tuple (bestInstence, bestVal) of the best solution (literals instentiation) found, and the best satisfaction rate.

To use the algorithme:

```python
from tabu import readCnf, ts
clauses,nbL=readCnf(filePath)
ts(clauses,nbL,len(clauses))
```

###Datasets
You can download benchmarks from [http://www.cs.ubc.ca/~hoos/SATLIB/benchm.html](http://www.cs.ubc.ca/~hoos/SATLIB/benchm.html).

***

###License:
This is published under GNU GPL Lisence.
For more informations about the terms: https://www.gnu.org/licenses/gpl.html

![Image Alt](https://www.gnu.org/graphics/gplv3-127x51.png)

