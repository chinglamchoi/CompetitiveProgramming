Program Clap7;

var n, i: integer;

begin

readln(n);
FOR i:= 1 TO 100 DO
    begin
    If i MOD 10 <> 0 then
       if (i MOD 10 = n) or (i MOD n = 0) or (i div 10 = n) then
        write('Clap ') else write(i,' ')

    else if (i MOD 10 = n) or (i MOD n = 0) or (i div 10 = n) then
        writeln('Clap') else writeln(i);

        end;


readln;

end.

