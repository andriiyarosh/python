import numpy as np
import matplotlib.pyplot as plt
import math

# массив, содержащий в себе координаты 5-ти точек
class2 = np.array([[0.49, 0.89],
                   [0.34, 0.81],
                   [0.36, 0.67],
                   [0.47, 0.49],
                   [0.52, 0.53]])

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


# метод возвращает мин расстояние от заданой точки до эталона класса
# принимает на воход одинарный массив с точкой и класс, содержащий в себе массив точек
def euclid_min_distance_to_class(d1, *class_dots):
    # запоминаем первую точку класса, чтобы с помощью неё вычислить эвклидово расстояние до заданой точки
    first_element = class_dots[0]
    # вычисляем эвклидово расстояние (обычное расстояние от А до Б, только со своей формулой) от заданой точки до
    # первой точки класса формула эвклидового расстояния - sqrt( (x1 - x2)^2 + (y1-y2)^2 )
    min_d_euclid = math.sqrt((d1[0] - first_element[0]) ** 2 + (d1[1] - first_element[1]) ** 2)

    # проходим в цикле по всем точкам класса и для каждой из этих точек определяем эвклидово расстояние до заданой точки
    for class_dot in class_dots:
        item_to_d1 = math.sqrt((d1[0] - class_dot[0]) ** 2 + (d1[1] - class_dot[1]) ** 2)
        # находим минимальное евклидово расстояние и возвращаем его как ответ
        if item_to_d1 <= min_d_euclid:
            min_d_euclid = item_to_d1

    return min_d_euclid


# метод возвращает расстояние от точки до класса, которое вычисляется
# путем нахождения максимума из модулей разности значений каждого признака
# входящие параметры - заданая точка и класс, содержащий в себе массив точек
def module_difference(d1, *class_dots):
    # запоминаем первую точку класса, чтобы с помощью неё вычислить расстояние до заданой точки
    first_element = class_dots[0]
    # вычисслям расстояни от заданой точки до первой точки класса.
    # формула, которая исп. для исчесления - max( |x1 - x2|, |y1 - y2| )
    min_distance_from_dot_to_class_dot = max(math.fabs(d1[0] - first_element[0]), math.fabs(d1[1] - first_element[1]))

    # проходим в цикле по всем точкам класса и для каждой из этих точек определяем расстояние до заданой точки
    for class_item in class_dots:
        item_to_d1 = max(math.fabs(d1[0] - class_item[0]), math.fabs(d1[1] - class_item[1]))
        # находим минимальное евклидово расстояние и возвращаем его как ответ
        if item_to_d1 <= min_distance_from_dot_to_class_dot:
            min_distance_from_dot_to_class_dot = item_to_d1

    return min_distance_from_dot_to_class_dot


# метод возвращает расстояние от заданой точки до центроида класса (класс содержит в себе массив точек)
def dot_to_centroid(d, *class_dots):
    # запоминаем длинну класса, т.е. количество точек
    length = len(class_dots)
    # сумма всех x-ов класса
    sum_x = 0
    # сумма всех y-ов класса
    sum_y = 0

    # проходим в цикле все точки класса и запоминаем сумммы всех х-ов и у-ов
    for class_item in class_dots:
        sum_x += class_item[0]
        sum_y += class_item[1]

    # формула, вычисляющая точку центроида
    centroid = (sum_x / length, sum_y / length)
    # вычисляем эталонное расстояние (просто расстояние) от заданой точки до центроида
    to_centr = math.sqrt((d[0] - centroid[0]) ** 2 + (d[1] - centroid[1]) ** 2)
    return to_centr


def sum_of_two_etalones(dot, *class_dots):
    first_dot = class_dots[0][0]
    first_dot_index = 0
    min_d_euclid_first = math.sqrt((dot[0] - first_dot[0]) ** 2 + (dot[1] - first_dot[1]) ** 2)
    if class_dots[0].__len__() == 1:
        return min_d_euclid_first

    second_dot = class_dots[0][1]
    second_dot_index = 1
    min_d_euclid_second = math.sqrt((dot[0] - second_dot[0]) ** 2 + (dot[1] - second_dot[1]) ** 2)

    for class_dot in range(len(class_dots[0])):
        euclid_to_class_dot = math.sqrt((dot[0] - class_dots[0][class_dot-1][0]) ** 2 + (dot[1] - class_dots[0][class_dot-1][1]) ** 2)
        if euclid_to_class_dot <= min_d_euclid_first and first_dot_index != class_dot and second_dot_index != class_dot:
            min_d_euclid_first = euclid_to_class_dot
            first_dot_index = class_dot
        if euclid_to_class_dot <= min_d_euclid_second and second_dot_index != class_dot and first_dot_index != class_dot:
            min_d_euclid_second = euclid_to_class_dot
            second_dot_index = class_dot

    return min_d_euclid_first + min_d_euclid_second


# метод возвращает индекс класса - его позицию, которая я вляется самой минимальной среди переданнах значений
def determine_class_index(*args):
    minimum_value = args[0]
    class_position = 0
    for element in args:
        if element <= minimum_value:
            minimum_value = element
            class_position = args.index(element) + 1
    return class_position


# строим график класса №2
p2, = plt.plot(class2[:, 0], class2[:, 1], '^g')
p3, = plt.plot(class3[:, 0], class3[:, 1], '|g')
p4, = plt.plot(class4[:, 0], class4[:, 1], '*r')
p6, = plt.plot(class6[:, 0], class6[:, 1], '+b')

# просим пользователя ввести координаты, чтобы задать точку
dotX = float(input('Type x coordinate: '))
dotY = float(input('Type x coordinate: '))
# создаем новый массив, с координатами, которые указал пользователь
a = np.array([dotX, dotY])
# строим график с заданной точкой
p7, = plt.plot(a[0], a[1], "*b")
# выводим ответ на 1 задание
print('Euclidean: Your dot relates to class with index of',
      determine_class_index(
          euclid_min_distance_to_class(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
          euclid_min_distance_to_class(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
          euclid_min_distance_to_class(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
          euclid_min_distance_to_class(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :],
                                       class6[4, :])))
# выводим ответ на 2 задание
print('Max of modules: Your dot relates to class with index of',
      determine_class_index(module_difference(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
                            module_difference(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
                            module_difference(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
                            module_difference(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :], class6[4, :])),
      '\n\n')
# выводим ответ на 3 задание
print('Object to class, 1: Your dot relates to class with index of',
      determine_class_index(dot_to_centroid(a, class2[0, :], class2[1, :], class2[2, :], class2[3, :], class2[4, :]),
                            dot_to_centroid(a, class3[0, :], class3[1, :], class3[2, :], class3[3, :], class3[4, :]),
                            dot_to_centroid(a, class4[0, :], class4[1, :], class4[2, :], class4[3, :], class4[4, :]),
                            dot_to_centroid(a, class6[0, :], class6[1, :], class6[2, :], class6[3, :], class6[4, :])))

# выводим ответ на 4 задание
print('Object to class, 5: Your dot relates to class with index of',
      determine_class_index(sum_of_two_etalones(a, class2),
                            sum_of_two_etalones(a, class3),
                            sum_of_two_etalones(a, class4),
                            sum_of_two_etalones(a, class6)))

# задаем легенди для каждой точки
plt.legend((p2, p3, p4, p6, p7), ('class2', 'class3', 'class4', 'class6', 'dot'))
# включаем сетку
plt.grid(True)
# рисуем график
plt.show()
