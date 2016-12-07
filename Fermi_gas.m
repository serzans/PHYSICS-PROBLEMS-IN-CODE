x = linspace(0,2,10000);
y = x.^(-5)./(exp(1./x)-1);
[m, i] = max(y)
disp(x(i));
plot(x,y)
