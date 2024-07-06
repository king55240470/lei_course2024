import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# 生成随机数据
np.random.seed(0)

# 创建PDF
pdf_pages = PdfPages('academic_charts.pdf')

# 散点图
plt.figure()
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y, c='blue', alpha=0.5)
plt.title('Scatter Plot')
pdf_pages.savefig()
plt.close()

# 折线图
plt.figure()
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.title('Line Plot')
pdf_pages.savefig()
plt.close()

# 柱状图
plt.figure()
data = [3, 5, 7, 9]
plt.bar(range(len(data)), data, color='orange')
plt.title('Bar Chart')
pdf_pages.savefig()
plt.close()

# 直方图
plt.figure()
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
pdf_pages.savefig()
plt.close()

# 箱线图
plt.figure()
data = [np.random.rand(50) for _ in range(4)]
plt.boxplot(data)
plt.title('Box Plot')
pdf_pages.savefig()
plt.close()

# 饼图
plt.figure()
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
pdf_pages.savefig()
plt.close()

# 极坐标图
plt.figure()
r = np.linspace(0, 1, 100)
theta = 2 * np.pi * r
plt.polar(theta, r)
plt.title('Polar Plot')
pdf_pages.savefig()
plt.close()

# 热图
plt.figure()
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('Heat Map')
pdf_pages.savefig()
plt.close()

# 关闭PDF
pdf_pages.close()
