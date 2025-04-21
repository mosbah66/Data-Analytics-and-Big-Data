# Classify professional hosts (owning multiple listings)
host_freq = listings['host_id'].value_counts()
listings['host_type'] = listings['host_id'].map(lambda x: 'Professional' if host_freq[x] > 1 else 'Individual')

sns.countplot(data=listings, x='host_type')
plt.title('Distribution of Professional vs. Individual Hosts')
plt.tight_layout()
plt.show()
