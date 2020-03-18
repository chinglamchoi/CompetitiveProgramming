Program D801;

var N, Q, low, high, middle, i :longint;
    A, B: array[1..100000] of longint;
    found: boolean;

    begin
    readln(N, Q);
    for i := 1 to N do read(A[i]);
    readln;
    for i := 1 to Q do read(B[i]);
    readln;

    for i := 1 to Q do
      begin
      low := 1;
      high := N;
      found := false;
      repeat
      middle := (low+ high) div 2;
      if B[i] > A[middle] then low := middle + 1 else
        if b[i] < A[middle] then high := middle -1 else found := true;
        until (found = true) or (low > high);
        if (found = true) then writeln('Yes') else writeln('No');
        end;

    readln;

    end.
