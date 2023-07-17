function [x] = pcg (A,b,guess,M)
r0 = b - A*guess;
z0 = linsolve(M,r0);
rho0 = z0' * r0;
p0 = z0;
tol = 1e-10;
maxiter= 1000;
for k = 0:1:maxiter
    s0=A*p0;
    alpha0 = rho0/(p0' * s0);
    guess1 = guess + alpha0*p0;
    r1 = r0 - alpha0*s0;
    z1 = linsolve(M,r1);
    rho1 = z1' * r1;
    if (rho1 <tol)
        x = guess1;
        return;
    else
        beta = rho1/rho0;
        p1 = z1 + beta*p0;
        r0 = r1;
        guess = guess1;
        z0 = z1;
        rho0 = rho1;
        p0 = p1;
        
    end
end
x = 'No convergence';
end
