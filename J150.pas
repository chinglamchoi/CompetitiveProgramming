Program Enumeration;

var i, j, n, num: integer;

begin

readln(n);

num := 1;

For i:= 1 to n do

begin
    for j := 1 to (n-1) do

    begin
    write(num, ' ');
    num := num + 4;
    end;
    writeln(num);

end;
readln;
end.
