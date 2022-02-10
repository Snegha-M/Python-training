'''
Bar:
    bar() function to draw bar graphs
'''
import matplotlib.pyplot as plt
import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()

# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# plt.show()

'''
Horizontal Bars:
    If you want the bars to be displayed horizontally instead of vertically, use the barh() function
'''
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y)
# plt.show()

'''
Bar Color:
    The bar() and barh() takes the keyword argument color to set the color of the bars.
'''
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red")
# plt.show()

#Color Names:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "hotpink")
# plt.show()

#Color Hex:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "#4CAF50")
# plt.show()

'''
Bar Width:
    The bar() takes the keyword argument width to set the width of the bars.
    The default width value is 0.8
'''
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, width = 0.1)
# plt.show()



#For horizontal bars, use height instead of width.
#The default height value is 0.8
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y, height = 0.1)
# plt.show()

