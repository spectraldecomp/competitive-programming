


# n and d are the number of days and the number of visits respectively
n, d = map(int, input().split())

days = []
for _ in range(n):
    # m is the mess generated each day and c is the cleaning units of each day
    m, c = map(int, input().split())
    days.append((m, c))
    
visits = []
for _ in range(d):
    # v is the day of the visit
    v = int(input())
    visits.append(v)
    

# Reverse the days list so that we can use the last day first
days.reverse()

# Reverse the visits list so that we can use the last visit first
visits.reverse()

for i in range(len(visits)):

    day = days[i]
    if day[1] == 0:
        continue
    
    # If the mess is greater than the cleaning units, then we can't clean the mess before
    # the family visits and we return -1
    if day[0] > day[1]:
        print(-1)
        exit()

    # Temp variable to store cleaning units
    temp = day[1]

    day[1] -= day[0]
    day[0] = max(0, day[0] - temp)

    j = 0
    while day[1] > 0:
        # Get the next day
        j+=1
        next_day = days[i+j]
        
        temp_mess = next_day[0]
        temp_cleaning_units = day[1]
        
        if (day[1] - next_day[0] >= 0):
            day[1] -= next_day[0]
            next_day[0] = max(0, next_day[0] - temp_cleaning_units)
        else:
            next_day[0] -= day[1]
            day[1] = 0
    