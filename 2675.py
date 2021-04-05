#수만큼 각 단어 반복

repe = int(input()) #몇개 할 건지
for i in range(repe):
    count, word = input().split() #문자로 받고
    for j in word:
        print(j*int(count),end = ('')) #문자를 INT형으로 J는 단어
    print()