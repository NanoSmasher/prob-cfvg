% Basic calculations
r = 4:16;
d = 49;
c20 = HGCC(d,r,2,0,'=');
c21 = HGCC(d,r,2,1,'=');
c22 = HGCC(d,r,2,2,'=');
c30 = HGCC(d,r,2,0,'=');
c31 = HGCC(d,r,3,1,'=');
c32 = HGCC(d,r,3,2,'=');
c33 = HGCC(d,r,3,3,'=');
h1 = HGCC(d,4,1,0,'=');
h2 = HGCC(d,4,2,0:1,'=');
h3 = HGCC(d,4,3,0:2,'=');
h4 = HGCC(d,4,4,0:3,'=');
c2 = HGCC(d,r,2,0,'>');
c3 = HGCC(d,r,3,0,'>');

% Weighted averages
c2a = c21+c22*2;
c3a = c31+c32*2+c33*3;

% Heal factor
t2a = c20*h1(1)+2*c21*h2(1)+c21*h2(2)+3*c22*h3(1)+2*c22*h3(2)+c22*h3(3) - 1;
t3a = c30*h1(1)+2*c31*h2(1)+c31*h2(2)+3*c32*h3(1)+2*c32*h3(2)+c32*h3(3)+4*c33*h4(1)+3*c33*h4(2)+2*c33*h4(3)+c33*h4(4) - 1;

%% plotting

figure('Name','Raw Drive Check Probabilities');
p1 = plot(r,[c2;c3;c21;c22;c31;c32;c33]);
p1(1).LineWidth = 2;
p1(2).LineWidth = 2;
legend('Top 2 > zero','Top 3 > zero','Top2 single','Top2 double','Top3 single','Top3 double','Top3 triple');
title('Raw Drive Check Probabilities');
ylabel('probability');
xlabel('number of copies');

figure('Name','Weighted Drive Check Probabilities');
p2 = plot(r,[c2a;c3a;c21;c22*2;c31;c32*2;c32*3]);
p2(1).LineWidth = 2;
p2(2).LineWidth = 2;
legend('Top2 average','Top3 average','Top2 single','Top2 double','Top3 single','Top3 double','Top3 triple');
title('Weighted Drive Check Probabilities');
ylabel('expected damage');
xlabel('number of copies');

figure('Name','Heal-adjusted Drive Check Probabilities');
p3 = plot(r,[c2a;c3a;t2a;t3a]);
p3(3).LineWidth = 2;
p3(4).LineWidth = 2;
legend('Top2 average','Top3 average','Top2 adjusted','Top3 adjusted');
title('Heal-adjusted Drive Check Probabilities');
ylabel('expected damage');
xlabel('number of copies');

figure('Name','Expected Effect of Heal Triggers');
plot(r,[c2a-t2a;c3a-t3a]);
legend('Top2 difference','Top3 difference')
title('Expected Effect of Heal Triggers');
ylabel('effective health regained');
xlabel('number of copies');

figure('Name','Twin Drive Constitution');
plot(r,[c21./c2a;c22*2./c2a]);
legend('Top2 single','Top2 double');
title('Twin Drive Constitution');
ylabel('percentage');
xlabel('number of copies');

figure('Name','Triple Drive Constitution');
plot(r,[c31./c3a;c32*2./c3a;c33*3./c3a]);
legend('Top3 single','Top2 double','Top3 triple');
title('Triple Drive Constitution');
ylabel('percentage');
xlabel('number of copies');