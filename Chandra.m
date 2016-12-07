R_constant = 0.02933*h^2/G/me/(mp)^(5/3)

c1 = -3/5*G;
c2 = 3/4/(2*mp)^(4/3) * h*c * (9/(16*pi^2))^1/3;
c3 = -c^2 * R_constant * me/mp;

x = 0:1e29:1e32;
y = c1 * x.^(4/3) + c2 * x.^(2/3) +c3;
y = abs(y);
[M,i] = min(y);
disp(x(i));

plot(x,y);

