Program D403;

var s, t, s1 : string[10]; n, i, j : integer;

begin

readln(s);
readln(n);
s1 := s;

for i := 1 to n do
  begin
  readln(t);
    for j := 1 to length(t) do
      begin
      if pos(t[j], s) <> 0 then
      s:=copy(s, 1, pos(t[j],s)-1) + copy(s,pos(t[j], s) + 1, length(s)-pos(t[j],s));
        if length(s1) = length (s) + length(t) then writeln('Yes') else writeln('No');
        end;

        readln;
end;
end.
