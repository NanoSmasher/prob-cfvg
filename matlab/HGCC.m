%%% Hyper Geometric Cumulative Calculator
function x = HGCC(a,b,c,d,find)
    %%% Calls HGC() multiple times, based on the 'find' modifier
    %%% Variables
    %%% 
    %%% a: Population size
    %%% b: Possible successes
    %%% c: Sample size
    %%% d: # of successes
    %%% find: modifies variable d. Available inputs; <, >, =.
	
	x = 0;
	if strcmp(find,'=')
		x = HGC(a,b,c,d);
	elseif strcmp(find,'<')
		for i = 0:d-1
			x = x + HGC(a,b,c,i);
		end
	elseif strcmp(find,'>')
		for i = d+1:smallernum(b,c)
			x = x + HGC(a,b,c,i);
		end
	end
end

function s = smallernum(a,b)
    if a < b
		s = a;
    else
		s = b;
	end
end

function o = Odds(a,b,d)
    if d == 1
		o = b./a;
    else
		o = (a-b)./a;
	end
end

function p = P(n, r)
    if r > n
		p = 0;
	else
		p = factorial(n)./factorial(n-r);
	end
end

function c = C(n, r)
    if r > n
		c = 0;
    else
		c = P(n,r)./factorial(r);
	end
end

function h = HGC(a,b,c,d)
    if b>a | c>a | d>a | d>c
		h = 0;
    elseif c == 1
		h = Odds(a,b,d);
    else 
		h = C(b,d).*C(a-b,c-d)./C(a,c);
	end
end