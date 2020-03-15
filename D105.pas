Program Date_Comparison;

var y1, m1, d1, y2, m2, d2 : integer;
    n1, n2 : longint;

begin
readln(y1, m1, d1);
readln(y2, m2, d2);
n1 :=y1*10000 + m1*100 + d1;
n2 :=y2*10000 + m2*100 + d2;
if n1< n2 then writeln('Before')
    else if n2< n1 then writeln('After')
                   else writeln('Same');
readln;


End.
