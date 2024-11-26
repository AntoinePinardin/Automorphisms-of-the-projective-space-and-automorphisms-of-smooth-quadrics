def AutP3(P0,P1,P2,P3,P4,Q0,Q1,Q2,Q3,Q4):
    var('a b c d');
    S1=solve([a*P1[0]+b*P2[0]+c*P3[0]+d*P4[0]==P0[0],a*P1[1]+b*P2[1]+c*P3[1]+d*P4[1]==P0[1],a*P1[2]+b*P2[2]+c*P3[2]+d*P4[2]==P0[2],a*P1[3]+b*P2[3]+c*P3[3]+d*P4[3]==P0[3]],a,b,c,d,solution_dict=true);
    M1=Matrix([S1[0][a]*P1,S1[0][b]*P2,S1[0][c]*P3,S1[0][d]*P4]);
    M1=M1.inverse();
    S2=solve([a*Q1[0]+b*Q2[0]+c*Q3[0]+d*Q4[0]==Q0[0],a*Q1[1]+b*Q2[1]+c*Q3[1]+d*Q4[1]==Q0[1],a*Q1[2]+b*Q2[2]+c*Q3[2]+d*Q4[2]==Q0[2],a*Q1[3]+b*Q2[3]+c*Q3[3]+d*Q4[3]==Q0[3]],a,b,c,d,solution_dict=true);
    M2=Matrix([S2[0][a]*Q1,S2[0][b]*Q2,S2[0][c]*Q3,S2[0][d]*Q4]);
    M=M2*M1;
    return M;    
    
def AutQuadSurf(M1,M2,s):
    M1=Matrix(M1);
    M2=Matrix(M2);
    var('a b c d');
    if s==0:
        g=vector((M1*vector([a,b])).list()+(M2*vector([c,d])).list());
    else:
        g=vector((M1*vector([c,d])).list()+(M2*vector([a,b])).list());
    Phi=vector([a*c,a*d,b*c,b*d]);
    PhiInv=vector([a+b,c+d,a+c,b+d]);
    gPhiInv=g(a=PhiInv[0],b=PhiInv[1],c=PhiInv[2],d=PhiInv[3]);
    g1=Phi(a=gPhiInv[0],b=gPhiInv[1],c=gPhiInv[2],d=gPhiInv[3]);
    P0=vector([2,8,1,4]);
    P1=vector([1,1,0,0]);
    P2=vector([1,0,1,0]);
    P3=vector([0,1,0,1]);
    P4=vector([0,0,2,1]);
    var('a b c d');
    S1=solve([a*P1[0]+b*P2[0]+c*P3[0]+d*P4[0]==P0[0],a*P1[1]+b*P2[1]+c*P3[1]+d*P4[1]==P0[1],a*P1[2]+b*P2[2]+c*P3[2]+d*P4[2]==P0[2],a*P1[3]+b*P2[3]+c*P3[3]+d*P4[3]==P0[3]],a,b,c,d,solution_dict=true);
    Q0=g1(a=P0[0],b=P0[1],c=P0[2],d=P0[3]);
    Q1=g1(a=P1[0],b=P1[1],c=P1[2],d=P1[3]);
    Q2=g1(a=P2[0],b=P2[1],c=P2[2],d=P2[3]);
    Q3=g1(a=P3[0],b=P3[1],c=P3[2],d=P3[3]);
    Q4=g1(a=P4[0],b=P4[1],c=P4[2],d=P4[3]);
    Mat=Matrix([P0,P1,P2,P3]);
    MatInv=Mat.inverse();

    M=AutP3(P0,P1,P2,P3,P4,Q0,Q1,Q2,Q3,Q4);
    return M;
    
def SGPGL4(Matrices):
    x=PolynomialRing(QQbar,'x').gen();
    for M in Matrices:
        M=Matrix(M);
        M=M/(x^4-det(M)).roots()[0][0];
    G=MatrixGroup(Matrices);
    Z=G.center();
    G=G.quotient(Z);
    return G;
    