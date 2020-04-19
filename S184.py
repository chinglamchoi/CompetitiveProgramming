a = int(input())
corpus_a = []
corpus_b = []

for i in range(a):
    corpus_a.append(input())
    corpus_b.append(input())

d = int(input())
for j in range(d):
    lang_a = input().split(" ")
    pat_a = input()
    pat_b = input()
    
    cnt = len(pat_a)
    result = [str()]*cnt
    
    for i in range(cnt):
        if pat_a[i] == pat_b[i]:
            try:
                result[i] = corpus_b[corpus_a.index(lang_a[i])]
            except ValueError:
                result[i] = lang_a[i]
        else:
            try:
                result[pat_b.index(pat_a[i])] = corpus_b[corpus_a.index(lang_a[i])]
            except ValueError:
                result[pat_b.index(pat_a[i])] = lang_a[i]
    print(" ".join(result))
