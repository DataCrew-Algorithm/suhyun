# 삽질 1 -> 딕셔너리로 풀어보자. value가 여러개 나와버려서 결국 리스트로
# n = int(input())
# info = {'name' : ['day', 'month', 'year']}
# info = {}

# for i in range(n):
#     a, b, c, d = input().split()
#     info[a] = [b, c, d]

# for name in info.keys():
#     info[name][3]

# print(info)

# 삽질 2 : 본격적인 삽질의 시작
# ver2 - 리스트로 풀어보자
# n = int(input())
# name = []
# day = []
# month = []
# year = []

# for _ in range(n):
#     a, b, c, d = input().split()
#     name.append(a)
#     day.append(b)
#     month.append(c)
#     year.append(d)

# min_year, max_year = min(year), max(year)         
# min_month, max_month = min(month), max(month)
# min_day, max_day = min(day), max(day)

# # 순차적으로 year의 max들의 인덱스를 뽑고, 걔를 이용해서 month의 max, day의 max를 뽑아내는 방식

# print(day)
# def find_idx(list_, string_):
#     while True:
#         try:
#             result = []
#             tmp = list_.index(string_)
#             list_[tmp] = '*'
#             result.append(tmp)
            
#         except:
#             break

#     return result
# year_min_idx = find_idx(year, min_year)
# month_min_idx = find_idx(month, min_month)
# day_min_idx = find_idx(day, min_day)
# year_max_idx = find_idx(year, max_year)
# month_max_idx = find_idx(month, max_month)
# day_max_idx = find_idx(day, max_day)

# if len(year_min_idx) == 1:
#     print(name[year_min_idx[0]])        # 여기에서 인덱스 에러남..
# else:
#     if len(month_min_idx) == 1:
#         print(name[month_min_idx[0]])
#     else:
#         print(name[day_min_idx[0]])

# if len(year_max_idx) == 1:
#     print(name[year_max_idx[0]])
# else:
#     if len(month_max_idx) == 1:
#         print(name[month_max_idx[0]])
#     else:
#         print(name[day_max_idx[0]])

# # 삽질3 : 굳이 리스트로, 함수로 정의해서 해보겠다는 의지
# # ver.3 -> 
# n = int(input())
# name = []
# day = []
# month = []
# year = []

# for _ in range(n):
#     a, b, c, d = input().split()
#     name.append(a)
#     day.append(b)
#     month.append(c)
#     year.append(d)
# year = list(map(int, year))
# month = list(map(int, month))
# day = list(map(int, day))



# def min_idx(l):
#     result = []
#     tmp = min(l)
#     while True:
#         try:
#             idx = l.index(tmp)
#             l[idx] = '*'
#             result.append(idx)
#         except:
#             break

#     return result

# def max_idx(l):
#     result = []
#     tmp = max(l)
#     while True:
#         try:
#             idx = l.index(tmp)
#             l[idx] = '*'
#             result.append(idx)
#         except:
#             break

#     return result

# print(year)
# print(max_idx(year))
# print(max_idx(month))


# oldyear, oldmonth, oldday = min_idx(year), min_idx(month), min_idx(day)     # 여기서 타입에러가 계속남
# yo_year, yo_month, yo_day = max_idx(year), max_idx(month), max_idx(day)     # TypeError: '<' not supported between instances of 'str' and 'int'

# if len(oldyear) == 1:
#     print(name[oldyear[0]])

# else:   # 2명 이상이 같은해에 태어남
#     if len(oldmonth) == 1:
#         print(name[oldmonth[0]])

#     else:   # 2명 이상이 같은 달에 태어남
#         print(name[oldday[0]])

# if len(yo_year) == 1:
#     print(name[yo_year[0]])

# else:   # 2명 이상이 같은해에 태어남
#     if len(yo_month) == 1:
#         print(name[yo_month[0]])

#     else:   # 2명 이상이 같은 달에 태어남
#         print(name[yo_day[0]])


# # ver.4 문자열로 더해야 한다는 걸 깨달음
n = int(input())
names = []
birthdays = []     # 문자열로 합칠 거라서, 생년월일이 다 합쳐진 리스트 하나만 있으면 됨.

for _ in range(n):
    name, day, month, year= input().split()
    day = day.zfill(2)                      # day와 month는 한자리인 경우가 있으므로 빈자리는 0으로 채워줌
    month =month.zfill(2)                   # zfill은 str에만 있는 method이므로 int로 바꾸면 안됨
    birth = year+month+day
    names.append(name)
    birthdays.append(int(birth))            # 숫자로 바꿔줌

old = birthdays.index(min(birthdays))       # 최솟값이 있는 인덱스를 찾음
young = birthdays.index(max(birthdays))     # 최댓값이 있는 인덱스를 찾음
print(names[young])
print(names[old])






        


