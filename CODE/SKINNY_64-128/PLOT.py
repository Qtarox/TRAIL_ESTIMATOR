import numpy as np
import matplotlib.pyplot as plt

DIC1={1: 0.4500160720025715, 2: 6.091288974606236, 3: 3.2144005143040824, 4: 16.722918675666985, 5: 3.1501125040180002, 6: 11.057537769206043, 7: 0.4500160720025715, 8: 17.791706846673094, 9: 0.4500160720025715, 10: 4.837672774027644, 12: 12.343297974927676, 14: 0.6910961105753777, 15: 0.4500160720025715, 16: 8.5824493731919, 18: 1.1089681774349083, 20: 2.3063323690131794, 21: 0.06428801028608164, 24: 5.4484088717454195, 28: 0.3294760527161684, 30: 0.33751205400192863, 32: 1.8563162970106077, 36: 0.6348441015750562, 40: 0.33751205400192863, 42: 0.048216007714561235, 48: 0.8678881388621021, 56: 0.048216007714561235, 60: 0.056252009000321436, 64: 0.14464802314368372, 72: 0.09643201542912247, 84: 0.008036001285760205, 96: 0.024108003857280617}
DIC1 = dict(sorted(DIC1.items(), key=lambda item: item[0], reverse=True))

y_values = []
percentages = []  # 对应的百分比权重
for i in DIC1:
    y_values.append(46+3-np.log2(i))
    percentages.append(DIC1[i])

x_positions = np.cumsum([0] + percentages)  # [0, 5, 20, 45, 75, 90, 100]
plt.figure(figsize=(8, 5))
for i in range(len(y_values)):
    plt.hlines(y=y_values[i], xmin=x_positions[i], xmax=x_positions[i+1], colors='b', linewidth=2)

# 画竖直线连接各层
for i in range(1, len(y_values)):
    plt.vlines(x=x_positions[i], ymin=y_values[i-1], ymax=y_values[i], colors='gray', linestyle="dashed")

# 设置标签
plt.xlabel("Percentage of Keys/% (Sorted by the Probability)")
plt.ylabel("Probability of Valid Plaintext Pairs("+r'$-log_2\mathcal{P}$'+")")
# plt.title("The Probability distribution ")
plt.xlim(0, 100)
plt.ylim(min(y_values) - 1, max(y_values) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# 显示图像
plt.show()
