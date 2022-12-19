# import numpy

# x = numpy.random.uniform(0.0, 5.0, 250)

# print(x)


# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.uniform(0.0, 5.0, 250)

# plt.hist(x, 5)
# plt.show()


# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.uniform(0.0, 5.0, 100000)

# plt.hist(x, 100)
# plt.show()


from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)