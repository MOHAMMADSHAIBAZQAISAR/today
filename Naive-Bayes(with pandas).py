from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
import pandas as pd

# Example data
data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Convert categorical variables to numerical labels
data_encoded = data.apply(lambda x: pd.factorize(x)[0])

# Split the features and target variable
X = data_encoded.drop(columns=['Play'])
y = data_encoded['Play']

# Create the decision tree classifier
dt = DecisionTreeClassifier()
dt.fit(X, y)

# Print the decision tree in tree format
tree_text = export_text(dt, feature_names=list(X.columns))
print(tree_text)
