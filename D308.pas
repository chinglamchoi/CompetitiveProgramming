program D308;

var S, T, dummy : string; count1, count2 :integer;

begin
readln(S);
readln(T);
count1 := 0;
count2 := 0;
dummy := S;

while pos(T,S) <> 0 do
  begin
  count1 := count1 +1;
  S := copy(S, pos(T,S)+1, length(S)-pos(T,S));
  end;

while pos(T,dummy) <> 0 do
  begin
  count2 := count2 +1;
  dummy:= copy(dummy, pos(T,dummy)+length(T),length(dummy)-pos(T,dummy));

  end;
  writeln(Count1);
  writeln(Count2);

  readln;

end.
