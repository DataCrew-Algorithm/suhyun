# n = int(input())
# info = {'name' : ['day', 'month', 'year']}
# info = {}

# for i in range(n):
#     a, b, c, d = input().split()
#     info[a] = [b, c, d]

# for name in info.keys():
#     info[name][3]

# print(info)

# ver2
n = int(input())
name = []
day = []
month = []
year = []

for _ in range(n):
    a, b, c, d = input().split()
    name.append(a)
    day.append(b)
    month.append(c)
    year.append(d)

min_year, max_year = min(year), max(year)
min_month, max_month = min(month), max(month)
min_day, max_day = min(day), max(day)

print(day)
def find_idx(list_, string_):
    while True:
        try:
            result = []
            tmp = list_.index(string_)
            list_[tmp] = '*'
            result.append(tmp)
            
        except:
            break

    return result
year_min_idx = find_idx(year, min_year)
month_min_idx = find_idx(month, min_month)
day_min_idx = find_idx(day, min_day)
year_max_idx = find_idx(year, max_year)
month_max_idx = find_idx(month, max_month)
day_max_idx = find_idx(day, max_day)

if len(year_min_idx) == 1:
    print(name[year_min_idx[0]])
else:
    if len(month_min_idx) == 1:
        print(name[month_min_idx[0]])
    else:
        print(name[day_min_idx[0]])

if len(year_max_idx) == 1:
    print(name[year_max_idx[0]])
else:
    if len(month_max_idx) == 1:
        print(name[month_max_idx[0]])
    else:
        print(name[day_max_idx[0]])




        


