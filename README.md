# Income_Simulation

## Project background

In the delivery industry, ensuring efficient order distribution and balancing the income disparity among couriers are key concerns. Full-time couriers often have more availability or priority compared to part-time couriers, which can result in differences in income over time. This project aims to simulate a realistic delivery system in which couriers handle restaurant orders, allowing us to evaluate how these disparities develop.

The restaurant prices vary, affecting each courier's potential income, and the simulation provides insight into how different probabilities of securing orders impact cumulative earnings. The model simulates how income is distributed across a fleet of couriers over thousands of rounds, enabling an analysis of how different strategies for order allocation and courier participation might influence both efficiency and equity in income distribution.

## description
This project simulates income distribution for couriers working at restaurants. Couriers are divided into two groups: full-time and part-time. Full-time couriers have double the chance of securing an order compared to part-time couriers, reflecting their higher availability or priority in the system. The restaurants have varying order prices, and over time, the simulation tracks the total earnings of each courier.

- Full-time couriers have a higher chance of securing orders (twice the chance of part-time couriers).

- Different restaurants offer varying order values, influencing total earnings.

- The simulation tracks income distribution over a long period, displaying both the short-term and long-term impacts on courier earnings.


## Problem Analysis: Income Distribution and Order Allocation

The primary goal of this simulation is to assess the fairness and efficiency of income distribution among couriers, from the perspective of the business. By simulating a delivery system where full-time couriers have a higher probability of securing orders compared to part-time couriers, the project evaluates whether the current order allocation mechanism effectively supports the business’s operational goals. The varying order values from different restaurants introduce further complexity in revenue dynamics, and this simulation will help determine if the distribution of income is balanced in a way that supports profitability and operational efficiency. This analysis aims to ensure that the allocation of orders and income aligns with the company's objectives, while also promoting optimal resource utilization.



## Model Assumptions:

Full-time couriers have twice the probability of receiving orders compared to part-time couriers.
Each order can fall into one of three categories of hourly income:
    High income: 50 units per hour
    Medium income: 40 units per hour
    Low income: 30 units per hour
Order prioritization: Higher-paying orders (50 units) are assigned first, followed by medium-paying orders (40 units), and then the lowest-paying orders (30 units).
Each category has 500 orders per day.
The system has 100 full-time couriers and 300 part-time couriers.




## conclusion 
The analysis reveals some significant disparities in courier income. The highest income of a full-time courier is 1.60 times that of the highest part-time courier, indicating a noticeable advantage for full-time couriers. Additionally, there are 2 full-time couriers with an income of less than 150, which suggests potential issues in workload distribution or efficiency. The average income of a full-time courier is 1.83 times that of a part-time courier, reinforcing the income gap between full-time and part-time workers. Furthermore, the highest income among full-time couriers is 6.42 times the lowest income, which highlights a considerable disparity. This significant gap may be unreasonable and could indicate inequitable assignment of orders or differing levels of performance.

To address these issues and improve the income distribution among couriers, the following recommendations are proposed:

Reevaluate Order Assignment: Reassess how orders are distributed among couriers to ensure a more equitable distribution of income opportunities.

Support for Low-Income Couriers: Provide additional training or resources to couriers with lower incomes to help them increase their efficiency and income potential.

Performance-Based Incentives: Implement a performance-based incentive system that rewards lower-performing couriers for improvements, helping to close the income gap.

Monitor Workload Distribution: Closely monitor workload and order assignments to avoid significant disparities and ensure a fairer income distribution across all couriers.
