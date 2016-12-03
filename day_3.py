with open('day3input.txt', "r") as data:
    read_data = data.read()

array = read_data.split('\n')
array = list(map(lambda k: k.split(' '), array))

def is_triangle(array):
    try:
        if len(array) == 3:
            array = sorted(list(map(int, array)))
            if array[0] + array[1] > array[2]:
                return True
        return False
    except:
        return False

# array = [["1", "2", "3"], ["3", "4", "5"], ["5", "5", "4"]]
# array = [
#     [101, 301, 501],
#     [102, 302, 502],
#     [103, 303, 503],
#     [201, 401, 601],
#     [202, 402, 602],
#     [203, 403, 603]
# ]


def first(array):
    array = list(map(
        lambda k: list(filter(lambda t: t != '', k)), array
    ))

    array = list(filter(lambda k: is_triangle(k), array))

    print(len(array))


def second(array):
    array = list(map(
        lambda k: list(filter(lambda t: t != '', k)), array
    ))
    array = list(filter(lambda k: len(k) == 3, array))
    new_array = []
    for i in range(len(array) // 3):
        one = []
        two = []
        three = []
        for k in range(i * 3, i * 3 + 3):
            print(k)
            one.append(array[k][0])
            two.append(array[k][1])
            three.append(array[k][2])
        new_array.append(one)
        new_array.append(two)
        new_array.append(three)
    new_array = list(filter(lambda k: is_triangle(k), new_array))
    print(new_array)
    print(len(new_array))

second(array)
