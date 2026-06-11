#ML Utilities
import numpy as np

def train_test_split(features, labels, train_size=None, test_size=None, shuffle=True, seed=True):
    if (len(features) == len(labels)) and (seed is True or seed is False) and (shuffle is True or shuffle is False):
        #size definition
        if train_size is None and test_size is None:
            train_size = 0.75
            test_size = 0.25
        elif train_size is None and test_size is not None:
            train_size = 1 - test_size
        elif train_size is not None and test_size is None:
            test_size = 1 - train_size
        if train_size <= 0 or test_size <= 0 or train_size + test_size > 1:
            raise ValueError("Train size and test size must be positive numbers and their sum must be lower than 1")
        
        #split calculation
        features = np.array(features)
        labels = np.array(labels)
        train_test_division = int(np.round(len(features) * train_size, 0))
        if train_test_division == 0 or train_test_division == len(features):
            raise ValueError("Train size or test size is too low")
        if shuffle is True:
            if seed is True:
                np.random.seed(9)
            random_idx = np.random.permutation(np.arange(len(features)))
        else:
            random_idx = np.arange(len(features))

        #splitting
        train_features = features[random_idx[:train_test_division]]
        train_labels = labels[random_idx[:train_test_division]]
        test_features = features[random_idx[train_test_division:]]
        test_labels = labels[random_idx[train_test_division:]]
        return train_features, train_labels, test_features, test_labels
    else:
        raise ValueError("Features and labels must have the same size, seed and shuffle must be Boolean")

if __name__ == "__main__":
    X = [[1,2],[2,3],[2,4],[3,3],[3,4],[4,5],[5,5],[6,6],[6,7],[7,8],[8,8],[8,9]]
    y = [0,0,0,0,0,0,1,1,1,1,1,1]
    train_X, train_y, test_X, test_y = train_test_split(X, y, 0.75)
    print(train_X)
    print(train_y)
    print(test_X)
    print(test_y)