program D305;

var s, i : integer; H : string;

begin
readln(H);
if length(H) = 8 then
  begin
  s := 9*(ord(H[1])-55)+8*(ord(H[2])-55);
  for i := 1 to 6 do s := s + (8-i)*(ord(H[i+2])-48)
  end else
  begin
  s:= 9*36+8*(ord(H[1])-55);
  for i := 2 to 6 do s:= s + (8-i)*(ord(H[i+1])-48)
  end;

i := 0;
while ((s+i) mod 11 <> 0) do i := i+1;
if i = 10 then
writeln(H, '(A)') else
writeln(H, '(', i, ')');
readln;
end.
