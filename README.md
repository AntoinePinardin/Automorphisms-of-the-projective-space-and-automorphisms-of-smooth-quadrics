# Automorphisms of the projective space and automorphisms of smooth quadrics

The function AutP3(points,images) returns the unique element of PGL_4 which sends the points in Points to points in Images. Images and Points must form two sets of points of P^3 in general linear position.

The function AutQuadSurf(M1,M2,s) takes an element g=(M1,M2,s) of PGL_2^2\rtimes\C_2 = Aut(P^1xP^1) and returns the matrix of PGL_4 defining the automorphism whose restriction on the Segre embedding of P1xP1 is the automorphism g.