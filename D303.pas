program D303;

var s: string; i, count, l: integer;

begin
readln(s);
l :=length(s);
for i := l downto 1 do write (s[i]);
writeln;
for i := 1 to (l div 2) do
  if s[i] = s[l-i+1] then count := count+1;
if count = (l div 2) then writeln('Yes') else writeln('No');

readln;

end.
