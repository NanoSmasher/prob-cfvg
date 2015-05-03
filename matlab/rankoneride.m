rank = zeros(10,6);

n = 1-HGCC(49,4,5,0,'=')*HGCC(47,4,4,0,'=');
g = 1-HGCC(43,4,5,0,'=');

for a = 7:16
	for b = 7:16
		for c = 7:16
			if a+b+c == 33
				[ag,an] = MinOne(a-4,1);
				[bg,bn] = MinOne(b,2);
				[cg,cn] = MinOne(c,3);
				odd = n*cg + (1-n)*an*bg*cg + (1-n)*(1-an)*g*cg + (1-n)*(1-an)*(1-g)*HGCC(43,a-4,5,0,'>')*bg*cg;
				nodd = n*cn + (1-n)*an*bn*cn;
				if odd > rank(10)
					rank(10,:) = [odd,nodd,odd-nodd,a,b,c];
					rank = sortrows(rank,-1);
				end
			end
		end
	end
end

RankByAssist = table([1;2;3;4;5;6;7;8;9;10],rank(:,1),rank(:,2),rank(:,3),rank(:,4),rank(:,5),rank(:,6),'VariableNames',...
	{'Rank' 'G_Assisted' 'Normal' 'Difference' 'Grade_1' 'Grade_2' 'Grade_3'})
	
rank = sortrows(rank,-2);

RankByBase = table([1;2;3;4;5;6;7;8;9;10],rank(:,2),rank(:,1),-rank(:,3),rank(:,4),rank(:,5),rank(:,6),'VariableNames',...
	{'Rank' 'Normal' 'G_Assisted' 'Difference' 'Grade_1' 'Grade_2' 'Grade_3'})