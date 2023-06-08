from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
}

# Convert categorical data to numerical labels
data_encoded = {}
for key, values in data.items():
    labels = {value: i for i, value in enumerate(set(values))}
    data_encoded[key] = [labels[value] for value in values]

X = []
y = data_encoded['Play']
for i in range(len(data_encoded['Outlook'])):
    X.append([
        data_encoded['Outlook'][i],
        data_encoded['Temperature'][i],
        data_encoded['Humidity'][i],
        data_encoded['Wind'][i]
    ])

dt = DecisionTreeClassifier()
dt.fit(X, y)

tree_text = export_text(dt, feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'])
print(tree_text)
