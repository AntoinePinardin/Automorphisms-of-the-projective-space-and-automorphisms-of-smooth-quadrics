# Automorphisms of the projective space and automorphisms of smooth quadrics

The function AutP3(P0,P1,P2,P3,P4,Q0,Q1,Q2,Q3,Q4) returns the unique element of PGL_4 which sends P0,P1,P2,P3,P4 to Q0,Q1,Q2,Q3,Q4, respectively, where P0, P1, P2, P3, P4 and Q0, Q1, Q2, Q3, Q4 form two sets of points of P^3 in general position.

The function AutQuadSurf(M1,M2,s) takes an element g=(M1,M2,s) of PGL_2^2\rtimes\C_2 = Aut(P^1xP^1) and returns the matrix of PGL_4 defining the automorphism whose restriction on the Segre embedding of P1xP1 is the automorphism g.