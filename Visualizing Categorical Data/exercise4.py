import matplotlib.pyplot as plt
import pandas as pd
import codecademylib3

water_usage = pd.read_csv("water_usage.csv")
print(water_usage.head())

wedge_sizes =  water_usage["prop"]
#print(wedge_sizes)

pie_labels =  water_usage["water_source"]
#print(props)

plt.pie(wedge_sizes, labels = pie_labels)
plt.axis('equal')
plt.title('Distribution of House Water Usage')
plt.show()
