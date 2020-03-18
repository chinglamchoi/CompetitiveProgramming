Program Enumeration;

var n, i, count: integer;

begin
readln(n);
i:= 0;
count := 0;
repeat
  i := i + 1;
  count:= count + 1;
  if (i mod n <>0)
  then write(4*count-3, ' ') else
  begin
  writeln(4*count-3);
  count :=count-1;
  end;


  until i = N*N;
  readln;

end.
