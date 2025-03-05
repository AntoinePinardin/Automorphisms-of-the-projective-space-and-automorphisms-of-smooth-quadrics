K:=AlgebraicClosure(Rationals());
R<x>:=PolynomialRing(K);
i:=Roots(x^2+1)[1,1];

//The following function takes a list of invertible matrices, and returns the subgroup of PGL they generate.

SGPGL:=function(matrices)
	dimension:=Nrows(matrices[1]);
   	matrices:=[M/Roots(x^dimension-R!Determinant(M))[1,1]:M in matrices];
	G:=sub<GL(dimension,K)|[GL(dimension,K)|M: M in matrices]>;
	D:=[M: M in Center(G) | IsScalar(M)];
	GP:=quo<G|D>;
	return(GP);
end function;

//Example with a group isomorphic to S_4

M1:=Matrix(K,4,[0,0,0,i,0,0,i,0,0,-i,0,0,-i,0,0,0]);
M2:=Matrix(K,4,[0,0,i,0,0,0,0,-i,-i,0,0,0,0,i,0,0]);
M3:=Matrix(K,4,[1,-3,-1,1,-3,-1,1,1,-1,1,-3,1,1,1,1,3]);
M4:=Matrix(K,4,[-3,-1,1,1,-1,1,-3,1,1,-3,-1,1,1,1,1,3]);

G:=SGPGL([M1,M2,M3,M4]);

GroupName(G);