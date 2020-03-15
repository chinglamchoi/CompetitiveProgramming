Program Ordinal_Number;

var N :integer;

begin

readln(n);
write(n);

If (n mod 100=11) or (n mod 100 = 12) or (n mod 100 = 13)
then writeln('th') else

case n mod 10 of
1: writeln('st');
2: writeln('nd');
3: writeln('rd');

else writeln('th');
end;

readln;

end.
