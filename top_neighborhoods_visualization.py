import matplotlib.pyplot as plt
import seaborn as sns

top_neigh = listings['neighbourhood_cleansed'].value_counts().nlargest(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_neigh.values, y=top_neigh.index, palette='coolwarm')
plt.title('Top 10 Sydney Neighborhoods by Airbnb Listings')
plt.xlabel('Number of Listings')
plt.ylabel('Neighborhood')
plt.tight_layout()
plt.show()
