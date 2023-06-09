class Node:
    def __init__(self, feature=None, threshold=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.label = label
        self.left = None
        self.right = None

    @staticmethod
    def gini_index(groups, classes):
        total_samples = sum([len(group) for group in groups])
        gini = 0.0
        for group in groups:
            group_size = float(len(group))
            if group_size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / group_size
                score += p * p
            gini += (1.0 - score) * (group_size / total_samples)
        return gini

    @staticmethod
    def split_dataset(dataset, feature, threshold):
        left, right = [], []
        for row in dataset:
            if row[feature] < threshold:
                left.append(row)
            else:
                right.append(row)
        return left, right

    @staticmethod
    def find_best_split(dataset):
        class_values = list(set(row[-1] for row in dataset))
        best_feature, best_threshold, best_gini, best_groups = None, None, float('inf'), None
        for feature in range(len(dataset[0]) - 1):
            for row in dataset:
                groups = Node.split_dataset(dataset, feature, row[feature])
                gini = Node.gini_index(groups, class_values)
                if gini < best_gini:
                    best_feature, best_threshold, best_gini, best_groups = feature, row[feature], gini, groups
        return {'feature': best_feature, 'threshold': best_threshold, 'groups': best_groups}

    @staticmethod
    def create_terminal_node(group):
        class_labels = [row[-1] for row in group]
        return max(set(class_labels), key=class_labels.count)

    def build_tree(self, node, max_depth, min_size, depth):
        left, right = node['groups']
        del(node['groups'])
        if not left or not right:
            node['left'] = node['right'] = Node.create_terminal_node(left + right)
            return
        if depth >= max_depth:
            node['left'], node['right'] = Node.create_terminal_node(left), Node.create_terminal_node(right)
            return
        if len(left) <= min_size:
            node['left'] = Node.create_terminal_node(left)
        else:
            node['left'] = Node.find_best_split(left)
            self.build_tree(node['left'], max_depth, min_size, depth + 1)
        if len(right) <= min_size:
            node['right'] = Node.create_terminal_node(right)
        else:
            node['right'] = Node.find_best_split(right)
            self.build_tree(node['right'], max_depth, min_size, depth + 1)

    def decision_tree(self, dataset, max_depth, min_size):
        root = Node.find_best_split(dataset)
        self.build_tree(root, max_depth, min_size, 1)
        return root

    def predict(self, node, row):
        if row[node['feature']] < node['threshold']:
            if isinstance(node['left'], dict):
                return self.predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predict(node['right'], row)
            else:
                return node['right']


dataset = [
    [2.771244718, 1.784783929, 0],
    [1.728571309, 1.169761413, 0],
    [3.678319846, 2.81281357, 0],
    [3.961043357, 2.61995032, 0],
    [2.999208922, 2.209014212, 0],
    [7.497545867, 3.162953546, 1],
    [9.00220326, 3.339047188, 1],
    [7.444542326, 0.476683375, 1],
    [10.12493903, 3.234550982, 1],
    [6.642287351, 3.319983761, 1]
]

tree = Node().decision_tree(dataset, max_depth=3, min_size=1)

# Test the Decision Tree
test_data = [
    [3.095607236, 1.783283623],
    [8.675418651, 0.242820951],
    [7.673756466, 3.508563011]
]

print("Test Results:")
for data in test_data:
    prediction = Node().predict(tree, data)
    print(f"Input: {data}, Prediction: {prediction}")
