# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(1, 9)
# a1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(1, 10)
# a1 = a1 + 0.5
# h = 0.1
# b = a * 0.1
# b1 = a1 * 0.1
#
# d=np.sum(np.multiply((np.power(1-np.exp(-b),0.5)),(1/b)))
# d1=np.sum(np.multiply((np.power(1-np.exp(-b1),0.5)),(1/b1)))
#
# e=0.05*(100+0.79+2*d)
# e1=0.1/6*100.79+0.4/6*d1+0.2/6*d
#
# c = (100 + 0) * 0.05 + 2 * 0.05 * np.sum((np.multiply((np.power((1 - np.exp(-b)), 0.5)), (1 / b))))
# print(e)
#
# c1 = 0.1 / 6 * 100 + 0.4 / 6 * np.sum(np.multiply((np.power((1 - np.exp(-b1)), 0.5)), (1 / b1))) + 0.2 / 6 * np.sum(
#     np.multiply((np.power((1 - np.exp(-b)), 0.5)), (1 / b)))
# print(e1)

