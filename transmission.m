function T = transmission(a,step, mode)
% Generates the transmission function with paramater a.
    if mode == 1
        x = 0:step:2*a;
        f1 = x <= a;
        f2 = x > a;
        f1 = f1 .* (1/a^2 * x);
        f2 = f2 .* (2/a - 1/a^2 * x);
        T = f1 + f2;
    end
    if mode == 2
        x = -2*a:step:2*a;
        f1 = x <= -a;
        f1 = f1 .* (2/a + 1/a^2 * x);
        f2 = (x > -a) & (x <= 0);
        f2 = f2 .* (-1/a^2 * x);
        f3 = (x > 0) & (x <= a);
        f3 = f3 .* (1/a^2 * x);
        f4 = x > a;
        f4 = f4 .* (2/a - 1/a^2 * x);
        T = f1 + f2 + f3 + f4;
    end
end


