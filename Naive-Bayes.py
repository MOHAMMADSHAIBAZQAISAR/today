class NaiveBayesClassifier:
    def __init__(self):
        self.class_counts = {}
        self.feature_counts = {}
        self.classes = set()

    def train(self, X, y):
        for features, label in zip(X, y):
            self.class_counts[label] = self.class_counts.get(label, 0) + 1
            for feature in features:
                if label not in self.feature_counts:
                    self.feature_counts[label] = {}
                self.feature_counts[label][feature] = self.feature_counts[label].get(feature, 0) + 1
                self.classes.add(label)

    def predict(self, X):
        predictions = []
        for features in X:
            max_prob = float('-inf')
            predicted_class = None
            for label in self.classes:
                prob = self.calculate_probability(features, label)
                if prob > max_prob:
                    max_prob = prob
                    predicted_class = label
            predictions.append(predicted_class)
        return predictions

    def calculate_probability(self, features, label):
        probability = 1.0
        total_count = sum(self.class_counts.values())
        for feature in features:
            feature_count = self.feature_counts[label].get(feature, 0)
            class_count = self.class_counts[label]
            probability *= (feature_count + 1) / (class_count + total_count)
        return probability

# Example usage
X_train = [
    ["I love this car"],
    ["This view is amazing"],
    ["I feel great"],
    ["I'm not happy with the product"],
    ["This is a terrible place"],
    ["I don't like this movie"]
]
y_train = ['yes', 'yes', 'yes', 'no', 'no', 'no']

X_test = [
    ["I like this place"]
]
# Preprocess the text data
X_train = [sentence[0].lower().split() for sentence in X_train]
X_test = [sentence[0].lower().split() for sentence in X_test]


nb_classifier = NaiveBayesClassifier()
nb_classifier.train(X_train, y_train)
predictions = nb_classifier.predict(X_test)
print(predictions)
