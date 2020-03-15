Program HKOI207;

var n, M, HCF, count: integer;
    LCM: longint;

begin
readln(n, m);
count:=1;
repeat
  if (n mod count=0) and (m mod count = 0) then hcf := count;
  count := count +1;
  until (count > n) or (count > m);
    LCM := (n*m) div HCF;
    writeln(HCF);
    writeln(LCM);
    readln;

end.
