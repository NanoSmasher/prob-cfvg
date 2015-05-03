%%% Minimum one copy
function [g,nog] = MinOne(n,type)
	%%% Calculates probability at least one of a certain card, with and without g-assist.
    %%% Variables
	%%%
	%%% n: number of copies
	%%% type: 0 is for any card, while 1-3 are reserved for G-assist
	%%%
	%%%	Assumptions:
	%%%  - for types 1-3, 
	%%%	 - damage taken is negligible
	%%%	 - you only G-assist once
	%%%	 - hence the odds are slightly lower then actual values

	if nargin < 2 
		type = 0;
	end

    if n<1 | n>38 | type<0 | type>4
		g = NaN;
		nog = NaN;
		return
	end

    p = HGCC(49,n,5,0,'=')*HGCC(47,n,4,0,'=');
    
	if type == 1
		g = 1 - p*HGCC(43,n,5,0,'='); 
		nog = 1 - p;
		return
	end

	p = p*HGCC(43,n,1,0,'=');
	
	if type == 2
		g = 1 - p*HGCC(42,n,5,0,'='); 
		nog = 1 - p;
		return
	end

    p = p*HGCC(42,n,1,0,'=');
    p = p*HGCC(41,n,1,0,'=');

	if type == 3
		g = 1 - p*HGCC(40,n,5,0,'=');
		nog = 1 - p;
		return
	end

	g = 1-p;
	nog = g;
end