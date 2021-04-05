product = int(input()) #과목 수 입력
score = list(map(int,input().split())) #정수를 list형으로 받기
M = max(score)
fake_score = []

for i in range(product):
    fake_score.append(score[i]/M*100) #리스트에 입력

print(sum(fake_score)/product)