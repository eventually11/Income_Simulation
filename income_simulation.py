import pandas as pd
import random
import matplotlib.pyplot as plt

# 定义快递员编号和概率
couriers = list(range(1, 201))  # 1-100 为一类，101-200 为另一类
probabilities = [0.5 if 1 <= courier <= 100 else 0.25 for courier in couriers]

# 创建快递员和概率的 DataFrame
courier_df = pd.DataFrame({
    'Courier_ID': couriers,
    'Probability': probabilities
})

# 打印快递员和概率的 DataFrame
print("快递员和概率的 DataFrame:")
print(courier_df.head())

# 定义每个收入档次的订单数量
orders_per_tier = 500  # 每个收入档次的订单数量
order_values = [50, 40, 30]  # 三档订单收入

# 模拟订单分配的函数
def assign_order():
    return random.choices(couriers, probabilities)[0]

# 分别为每个收入档次生成 500 个订单，总共 1500 个订单
orders = []
for value in order_values:
    for _ in range(orders_per_tier):
        orders.append({
            'Order_ID': len(orders) + 1,
            'Courier_ID': assign_order(),
            'Order_Value': value
        })

# 生成订单的 DataFrame
order_df = pd.DataFrame(orders)

# 打印订单分配结果
print("\n订单分配结果的 DataFrame:")
print(order_df.head())

# 如果需要将 DataFrame 保存到文件，可以使用以下代码：
# order_df.to_csv('order_distribution.csv', index=False)


# 计算每个快递员的总收入
courier_income = order_df.groupby('Courier_ID')['Order_Value'].sum().reset_index()

# 添加一个新列，区分全职和兼职快递员
courier_income['Type'] = courier_income['Courier_ID'].apply(lambda x: 'Full-time' if x <= 100 else 'Part-time')

# 设置颜色：全职快递员用蓝色，兼职快递员用绿色
colors = courier_income['Type'].map({'Full-time': 'blue', 'Part-time': 'green'})

# 绘制每个快递员的收入条形图，并用不同颜色区分全职和兼职快递员
plt.figure(figsize=(12, 6))  # 设定画布大小
plt.bar(courier_income['Courier_ID'], courier_income['Order_Value'], color=colors)  # 生成带有颜色区分的条形图
plt.xlabel('Courier ID')  # 设置x轴标签
plt.ylabel('Total Income')  # 设置y轴标签
plt.title('Total Income per Courier (Full-time vs Part-time)')  # 设置标题

# 添加图例
plt.legend(handles=[plt.Rectangle((0,0),1,1,color='blue', label='Full-time'),
                    plt.Rectangle((0,0),1,1,color='green', label='Part-time')])

plt.show()  # 显示图表




# 按照收入高低进行排序
courier_income_sorted = courier_income.sort_values(by='Order_Value', ascending=False)
# 绘制按照收入高低排序的条形图

plt.figure(figsize=(12, 6))  # 设定画布大小
plt.bar(range(len(courier_income_sorted)), courier_income_sorted['Order_Value'], color=courier_income_sorted['Type'].map({'Full-time': 'blue', 'Part-time': 'green'}))
plt.xlabel('Rank (by Income)')  # 设置x轴标签
plt.ylabel('Total Income')  # 设置y轴标签
plt.title('Total Income per Courier (Sorted by Income)')  # 设置标题

# 添加图例
plt.legend(handles=[plt.Rectangle((0,0),1,1,color='blue', label='Full-time'),
                    plt.Rectangle((0,0),1,1,color='green', label='Part-time')])

plt.show()  # 显示图表