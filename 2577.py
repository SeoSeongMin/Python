#숫자 수 세기
str_list = []
tot = 1

for i in range(3):
    enter = int(input())
    str_list.append(enter)
    tot *= str_list[i]
    
tot = str(tot)

for j in range(10):
    print(tot.count(str(j)))

    
    
