Program HKOI302;

var n: shortstring;
    m, l, count: integer;

begin
  readln(n);
  writeln(length(n));
  count:= 0 ;
  for m := 1 to length(n) do
    if n[m] = ' ' then count := count + 1;
    writeln(count+1);
    readln;


end.
