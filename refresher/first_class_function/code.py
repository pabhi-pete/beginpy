from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find the element with {expected!r}')
    
friends = [
    {"name": "Pete", "age": 32},
    {"name": "Moosom", "age": 15},
    {"name": "Fon", "age": 33}
]

# def get_friend_name(friend):
#     return friend['name']
# print(search(friends, "Fon", get_friend_name))

# try another way around using lambda function for looking more nicer
print(search(friends, "Pete", lambda friend: friend['name']))
print(search(friends, "Pete", itemgetter('name')))