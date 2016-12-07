% n*n matrix s.t. n odd
n = 101;
M = zeros(n,n);

d = 0;

x = (n+1)/2;
y = (n+1)/2;
M(x,y) = 1;

c = 1;
for steps = 1:n
	for j = 1:2
		for i = 1:steps
			c++;
			x = x+(d==0)-(d==2);
			y = y+(d==1)-(d==3);
			M(x,y) = isprime(c);
		end
		d = mod((d + 1),4);
	end
end

spy(M);
