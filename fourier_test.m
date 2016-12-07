x = linspace(-pi,pi,10);

y2 = zeros(1,10);
y2 = y2 + 1
for m=2:3000
    y2 = y2 + cos(m*x) * (4) * (-1)^m / (1-m^2)
end



plot(x,y2,x,x.*sin(x))