rank = zeros(10,6);

for a = 7:16
	for b = 7:16
		for c = 7:16
			if a+b+c == 33
				[ag,an] = MinOne(a,1);
				[bg,bn] = MinOne(b,2);
				[cg,cn] = MinOne(c,3);
				if ag*bg*cg > rank(10)
					rank(10,:) = [ag*bg*cg,an*bn*cn,ag*bg*cg-an*bn*cn,a,b,c];
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