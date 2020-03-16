program D309;

var S, T :string[100];  i : integer;

begin
readln(S);
readln(T);
for i := 1 to length(s) do if ord(s[i]) > 96 then s[i] := chr(ord(s[i])-32);
for i := 1 to length(t) do if ord(t[i]) > 96 then t[i] := chr(ord(t[i])-32);

if s = t then writeln('Equal') else
  if s < T then writeln('Smaller') else writeln('Greater');
  readln;
end.
