Program HKOI206;

var N: longint;
begin
    readln(N);
    while (N<>1) do
      begin
      writeln(N);
      if (N mod 2 = 0) then N:= N div 2 else N:=N*3+1;
      end;
    writeln('1');
    readln;
end.
