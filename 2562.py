#최댓값 찾기
temp = []

for i in range(9):
    enter = int(input())
    temp.append(enter)
max_number = temp[0]

for j in range(9):
    if(max_number <= temp[j]):
        max_number = temp[j]
        max_count = j+1
        
print(max_number)
print(max_count)
    