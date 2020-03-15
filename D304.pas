Program Hangman;

var l, count, i:integer; h, s: string; a: char;

begin
readln(h);
for i:= 1 to 30 do writeln;
l := length(h);
s :='';     (*null string*)
count := 0;
for i := 1 to l do s:= s+ '_'; // prepare answer string
while count < l do // keep trying while all the letters are not guessed yet
begin
readln(a);
for i:= 1 to l do
  if (h[i]=a) and (s[i] = '_') then
    begin
    s[i] := a;
    count := count+1;
    end;
writeln(s);
end;
readln;
end.
