import numpy as np
import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
h = sympy.Symbol('h')
x_list = np.linspace(0, 1, 6)
len1 = len(x_list)
print(x_list)
y_list = []


def runge_kutta_4_classic(x, y, h):
    k1 = x + y
    k2 = x + h / 2 + y + h / 2 * (k1)
    k3 = x + h / 2 + y + h / 2 * (k2)
    k4 = x + h + y + h * (k3)
    runge_kutta = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)+y
    return runge_kutta


def iteration(x0, y0, step):
    for i in range(0, len1 - 1):
        temp = runge_kutta_func.evalf(subs={x: x0[i], y: y0, h: step})
        y_list.append(temp)
        y0 = temp
    return y_list


runge_kutta_func = runge_kutta_4_classic(x, y, h)
print(sympy.simplify(runge_kutta_func.evalf(subs={h: 0.2})))
iteration(x_list, 1, 0.2)
print(y_list)
