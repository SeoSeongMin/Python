#검증 수
enter = list(map(int,input().split()))
verification_list = []

for i in range(len(enter)):
    verification_list.append(enter[i]*enter[i])
verification = sum(verification_list)%10
print(verification)