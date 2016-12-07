% n*n matrix s.t. n odd
n = 5;
M = zeros(n,n);

d = 0;

x_central = (n+1)/2;
y_central = (n+1)/2;

Gaussian_primes=[];

% Populate the matrix with complex numbers
for k=1:5
	for l=1:5
		M(k,l)=1.0*(k-y_central)+1.0i*(l-x_central);
	end
end

for g=1:n^2
% Define spiral loop
end


disp(M');