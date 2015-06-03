###Graphs

##Basic Definitions

Tree in a connected graph G = (V,E,c)
Spanning tree of G
Every spanning tree of G with n vertices has n-1 edges (induction proof)

##Problem Formulation

Cost = sum of edge-costs
Given: undirected, connected graph G, with positive edge costs
Find: a tree T spanning V with the total cost minimized.

##Trivial algorithm
Select n-1 edges
If it's a tree spanning G compute its length and compare with the length of the best tree found so far.
Save if new tree is shorter

Repeat for another subset of n-1 edges
G can have to n(n-1)/2 edges
numer of subset of size n-1 is exp.
can tak exponential time

##Get an idea
Look at a solution for a small problem instance.

##Cuts
$C = {X, V-X}, Ø \in X \in V, $ is a cut of G
An edge crosses a cut if it has one endvertex in X and one endvertex in V-X
And edge crossing cut C is a light edge if it has minimum weight among all edges crossing C

##Basic property of light edges
Claim: A light edge e of any cut C = {C, V-X} belongs to some minimum spanning tree of G = (V,E,c)
Prof by contradiction: assume that e = (u, v) is a light edge of some cut C but it belongs to no MST.
Let T be an MST. It contains a path form u to v. At least one edge, denoted by f, on this path crosses C.

Remove f and add e to T. T '= T - f+ e is a tree spanning G. Since |e| <= |f| then |T'| <= |T|
T is a MST, hence |T'| = |T|. T' is therefore also a MST it contains e. This is a contradiction.
