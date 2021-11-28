a = {
    'name': 'a',
    'path': ['b', 'e', 'd'],
    'val': [2, 1, 1]
}

b = {
    'name': 'b',
    'path': ['a', 'c'],
    'val': [2, 2]
}
c = {
    'name': 'c',
    'path': ['b', 'e', 'd'],
    'val': [2, 1, 2]
}
d = {
    'name': 'd',
    'path': ['c', 'a'],
    'val': [2, 1]
}
e = {
    'name': 'e',
    'path': ['a', 'c'],
    'val': [1, 1]
}


def map(start, goal):
    try:
        print('start')
        print(start['path'], start['val'])
        print('goal')
        print(goal['path'], goal['val'])

        end = goal['name']
        if end in start['path']:
            index = start['path'].index(end)
            value = start['val'][index]
            print(f'your route is {end}, value is {value}')
        else:
            print(b['path'])
    except Exception as e:
        raise e


print(map(a, c))
