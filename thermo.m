% x = 0.01:0.01:1;
% 
% y = (1-exp(-x))/(1-exp(-6*x))*(1+2*exp(-x)+3*exp(-2*x)+4*exp(-3*x)+5*exp(-4*x)+6*exp(-5*x))-3.667;
% 
% plot(x,y)

fun = @(x) (1-exp(-x))/(1-exp(-6*x))*(1+2*exp(-x)+3*exp(-2*x)+4*exp(-3*x)+5*exp(-4*x)+6*exp(-5*x))-3.667; % function
x0 = 1; % initial point
x = fzero(fun,x0);

disp(x)

c = 0.01:0.01:1;
plot(c, fun(c))
    
fun(-0.0574)
