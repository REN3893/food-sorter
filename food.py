def by_rating(res):
    name, rating, minutes = res
    return (-rating,minutes)

def by_time(res):
    name, rating, minutes = res
    return (minutes,-rating)

RESTAURANTS = [
("Mango Rice", 4.2, 25),
("Pad Thai House", 4.8, 40),
("Chicken Rice", 4.6, 15),
("Som Tam Corner", 4.6, 25),
("Boat Noodles", 4.8, 30),
]

request = input('Sort by (rating/time): ').lower()
if(request  == 'rating'):
    sort_res = sorted(RESTAURANTS, key=by_rating)
    for i in range(len(sort_res)):
        print(f'{i+1}. {sort_res[i]}')
elif(request == 'time'):
    sort_res = sorted(RESTAURANTS, key=by_time)
    for i in range(len(sort_res)):
        print(f'{i+1}. {sort_res[i]}')
else:
    print('Unknown option')
