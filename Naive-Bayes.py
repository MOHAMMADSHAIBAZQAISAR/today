# Define the training dataset
training_data = [
    ["I love this car", "positive"],
    ["This view is amazing", "positive"],
    ["I feel great", "positive"],
    ["I'm not happy with the product", "negative"],
    ["This is a terrible place", "negative"],
    ["I don't like this movie", "negative"]
]

# Create an empty vocabulary set
vocabulary = set()

# Add words from training data to the vocabulary
for data in training_data:
    sentence = data[0]
    words = sentence.split()
    vocabulary.update(words)

# Count the occurrences of each class in the training data
class_counts = {}
for data in training_data:
    label = data[1]
    if label in class_counts:
        class_counts[label] += 1
    else:
        class_counts[label] = 1

# Compute the probabilities of each class
total_data = len(training_data)
class_probabilities = {}
for label, count in class_counts.items():
    class_probabilities[label] = count / total_data

# Create a dictionary to store word probabilities
word_probabilities = {}

# Count the occurrences of each word in each class
word_counts = {}
for data in training_data:
    sentence = data[0]
    label = data[1]
    words = sentence.split()
    if label not in word_counts:
        word_counts[label] = {}
    for word in words:
        if word in word_counts[label]:
            word_counts[label][word] += 1
        else:
            word_counts[label][word] = 1

# Compute the probabilities of each word given a class
for label in word_counts:
    word_probabilities[label] = {}
    total_words = sum(word_counts[label].values())
    for word in vocabulary:
        if word in word_counts[label]:
            word_probabilities[label][word] = word_counts[label][word] / total_words
        else:
            word_probabilities[label][word] = 0.0

def classify_text(text):
    words = text.split()
    # Initialize the class probabilities
    class_scores = {}
    for label in class_probabilities:
        # Start with the class probability
        score = class_probabilities[label]
        for word in words:
            # Check if the word is in the vocabulary
            if word in vocabulary:
                # Multiply the score by the word probability
                score *= word_probabilities[label][word]
        class_scores[label] = score
    # Select the class with the highest probability
    predicted_class = max(class_scores, key=class_scores.get)
    return predicted_class

# Test the classifier
test_text = "I like this place"
predicted_label = classify_text(test_text)
print("Predicted Label:", predicted_label)

#output: Negative
