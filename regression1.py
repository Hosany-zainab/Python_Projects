import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):

    n = np.size(x)

    m_x, m_y = np.mean(x), np.mean(y)

    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y-b_1*m_x

    return b_0, b_1


def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="g", marker="*", s=30)
    y_pred = b[0] + b[1]*x

    #potting the regression line
    plt.plot(x, y_pred, color="y")

    # putting label
    plt.xlabel('age')
    plt.ylabel('Population_having_mobile')

    plt.show() #fuction to show plot


def main():
    #observation
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    y = np.array([40, 80, 90, 82, 65, 50, 35, 30, 15, 5])

    b = estimate_coef(x, y)
    print("Estimated coefficient:/nb_0 = {} \\nb_1 = {}".format(b[0],b[1]))

    #plotting regression_line
    plot_regression_line(x,y,b)


if __name__ == "__main__":
    main()

