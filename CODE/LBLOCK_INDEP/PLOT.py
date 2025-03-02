import numpy as np
import matplotlib.pyplot as plt

DIC1={10: 0.78125, 12: 0.78125, 14: 0.78125, 15: 1.5625, 16: 1.5625, 18: 2.34375, 20: 8.59375, 21: 1.5625, 22: 0.78125, 24: 10.9375, 25: 1.5625, 27: 1.5625, 28: 7.8125, 30: 3.90625, 32: 15.625, 33: 1.5625, 35: 1.5625, 36: 8.59375, 40: 10.9375, 42: 0.78125, 44: 7.8125, 45: 1.5625, 48: 1.5625, 50: 1.5625, 54: 0.78125, 55: 1.5625, 60: 0.78125, 66: 0.78125}
DIC1 = dict(sorted(DIC1.items(), key=lambda item: item[0], reverse=True))

y_values = []
percentages = []  # 对应的百分比权重
for i in DIC1:
    y_values.append(72+4-np.log2(i))
    percentages.append(DIC1[i])

x_positions = np.cumsum([0] + percentages)  # [0, 5, 20, 45, 75, 90, 100]
plt.figure(figsize=(8, 5))
for i in range(len(y_values)):
    plt.hlines(y=y_values[i], xmin=x_positions[i], xmax=x_positions[i+1], colors='b', linewidth=2)

# 画竖直线连接各层
for i in range(1, len(y_values)):
    plt.vlines(x=x_positions[i], ymin=y_values[i-1], ymax=y_values[i], colors='gray', linestyle="dashed")

# 设置标签
plt.xlabel("Percentage of Keys/% (Sorted by the Probability)",fontsize=14)
plt.ylabel("Probability of Valid Plaintext Pairs("+r'$-log_2\mathcal{P}$'+")",fontsize=14)
# plt.title("The Probability distribution ")
plt.xlim(0, 100)
plt.ylim(min(y_values) - 1, max(y_values) + 1)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# 显示图像
plt.show()
