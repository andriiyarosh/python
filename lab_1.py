import numpy as np
import matplotlib.pyplot as plt
import math

class2 = np.array([[0.49, 0.89],
                   [0.34, 0.81],
                   [0.36, 0.67],
                   [0.47, 0.49],
                   [0.52, 0.53]])

print(class2[0, :])

class3 = np.array([[0.62, 0.83],
                   [0.79, 0.92],
                   [0.71, 0.92],
                   [0.78, 0.83],
                   [0.87, 0.92]])

class4 = np.array([[0.55, 0.4],
                   [0.66, 0.32],
                   [0.74, 0.49],
                   [0.81, 0.3],
                   [0.77, 0.2]])

class6 = np.array([[0.05, 0.15],
                   [0.09, 0.39],
                   [0.13, 0.51],
                   [0.25, 0.34],
                   [0.15, 0.36]])


def find_etalon(d1, *class_dots):
    first_element = class_dots[0]
    min_d_euclid = math.sqrt((d1[0] - first_element[0]) ** 2 + (d1[1] - first_element[1]) ** 2)

    for class_item in class_dots:
        item_to_d1 = math.sqrt((d1[0] - class_item[0]) ** 2 + (d1[1] - class_item[1]) ** 2)
        if item_to_d1 <= min_d_euclid:
            min_d_euclid = item_to_d1

    return min_d_euclid


def sum_of_two_etalones(d1, *_class):
    first_element = _class[0]
    first_element_index = 0
    min_d_euclid_first = 0
    for class_dot in range(len(_class)):
        min_d_euclid_first = find_etalon(d1, first_element[class_dot])

    for class_item in _class:
        for class_dot in range(len(class_item)):
            item_to_d1 = find_etalon(d1, class_item[class_dot])
            if item_to_d1 <= min_d_euclid_first:
                min_d_euclid_first = item_to_d1
                first_element_index = class_dot

    if first_element_index != 0:
        min_d_euclid_second = find_etalon(d1, first_element[0])
    else:
        min_d_euclid_second = find_etalon(d1, first_element[1])
    # __class.remove(__class[first_element_index])

    for class_item in first_element:
        item_to_d1 = find_etalon(d1, class_item)
        if item_to_d1 <= min_d_euclid_second:
            min_d_euclid_second = item_to_d1

    return min_d_euclid_first + min_d_euclid_second


def module_difference(d1, *class_dots):
    first_element = class_dots[0]
    min_distance_from_dot_to_class_dot = max(math.fabs(d1[0] - first_element[0]), math.fabs(d1[1] - first_element[1]))

    for class_item in class_dots:
        item_to_d1 = max(math.fabs(d1[0] - class_item[0]), math.fabs(d1[1] - class_item[1]))
        if item_to_d1 <= min_distance_from_dot_to_class_dot:
            min_distance_from_dot_to_class_dot = item_to_d1

    return min_distance_from_dot_to_class_dot


def dot_to_centroid(d, *class_dots):
    length = len(class_dots)
    sum_x = 0
    sum_y = 0

    for class_item in class_dots:
        sum_x += class_item[0]
        sum_y += class_item[1]

    centroid = (sum_x / length, sum_y / length)
    return find_etalon(d, centroid)


def sum_of_to_two_closest_etalones(d1, *classes_list):
    first_element = classes_list[0]
    min_d = sum_of_two_etalones(d1, first_element)
    class_index = 0

    for class_item in classes_list:
        min = sum_of_two_etalones(d1, class_item)
        if min <= min_d:
            min_d = min
            class_index = classes_list.index(class_item) + 1

    return class_index


def determine_class_index(*args):
    minimum_value = args[0]
    class_position = 0
    for element in args:
        if element <= minimum_value:
            minimum_value = element
            class_position = args.index(element) + 1
    return class_position


p2, = plt.plot(class2[:, 0], class2[:, 1], '^g')
p3, = plt.plot(class3[:, 0], class3[:, 1], '|g')
p4, = plt.plot(class4[:, 0], class4[:, 1], '*r')
p6, = plt.plot(class6[:, 0], class6[:, 1], '+b')
dotX = float(input('Type x coordinate: '))
dotY = float(input('Type x coordinate: '))
a = np.array([dotX, dotY])
p7, = plt.plot(a[0], a[1], "*b")
print('Euclidean: Your dot relates to class with index of',
      determine_class_index(find_etalon(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
                            find_etalon(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
                            find_etalon(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
                            find_etalon(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :],
                                        class6[4, :])))
print('Max of modules: Your dot relates to class with index of',
      determine_class_index(module_difference(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
                            module_difference(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
                            module_difference(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
                            module_difference(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :], class6[4, :])),
      '\n\n')
print('Object to class, 1: Your dot relates to class with index of',
      determine_class_index(dot_to_centroid(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
                            dot_to_centroid(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
                            dot_to_centroid(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
                            dot_to_centroid(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :], class6[4, :])))
print('Object to class, 5: Your dot relates to class with index of',
      sum_of_to_two_closest_etalones(a, class2, class3, class4, class6))

plt.legend((p2, p3, p4, p6, p7), ('class2', 'class3', 'class4', 'class6', 'dot'))
plt.grid(True)
plt.show()
