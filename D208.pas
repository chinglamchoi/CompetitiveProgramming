Program D208;

var n, i, count : integer; a : array[1..10] of longint; max1, max2 : longint;

begin
readln(n);
for i := 1 to n do read(a[i]);
readln;

max1 := -2147483648;
max2 := -2147483648;
for i := 1 to n do
  if a[i] > max1 then max1 := a[i];


count := 0;
for i := 1 to n do
  if a[i] = max1 then count := count + 1;

if count > 1 then max2 := max1 else
  begin
  for i := 1 to n do
    if a[i] < max1 then
      if a[i] > max2 then max2 := a[i];
  end;

writeln(max1);
writeln(max2);
readln;

end.
