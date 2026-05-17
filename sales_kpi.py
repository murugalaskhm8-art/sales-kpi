import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [10000, 15000, 12000, 18000]
}

df = pd.DataFrame(data)

# Display data
print(df)

# Create chart
plt.plot(df['Month'], df['Sales'])
plt.title('Monthly Sales KPI')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
