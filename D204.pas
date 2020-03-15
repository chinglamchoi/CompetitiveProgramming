Program DSE204;

var i, j, n : integer;

begin
readln(n);

for i := 1 to n do
    begin
    for j := 1 to abs((n+1) div 2 - i) do write(' ');

    If (i=1) or (i=n) then writeln('#') else
       begin
       write('#');

       if i<= ((n+1) div 2) then for j := 1 to 2*i-3 do write(' ')
              else for j := 1 to (n-i)*2-1 do write(' ');
       writeln('#');

       end;

    end;
readln;
end.
