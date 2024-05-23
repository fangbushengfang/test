import numpy as np

# x_list = np.linspace(0, 1, 11)
# len1 = len(x_list)

x_list = np.linspace(0, 0.5, 6)
len1 = len(x_list)


# def iterator_func(x, x1, y):
#     return 1.105 * y + 0.055 * x + 0.05 * x1

def iterator_func(x, x1, y):
    return 0.905 * y + 0.045 * x+0.045*x**2 + 0.05 * x1+0.05*x1**2

y_list = []


def opti_euler(x_list, y0, length):
    for i in range(0, length - 1):
        temp = iterator_func(x_list[i], x_list[i + 1], y0)
        y0 = temp
        y_list.append(y0)
    return y_list


opti_euler(x_list, 0, len1)
y_array=y_list
print(np.round(y_array,6))
