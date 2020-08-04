# The task is to calculate the concentration for each filter from the 50% and 90% Petrosian radius measurements:

# conc=petroR50/petroR90

# As described earlier, data has the following fields:

#     colours: u-g, g-r, r-i, and i-z;
#     eccentricity: ecc
#     4th adaptive moments: m4_u, m4_g, m4_r, m4_i, and m4_z;
#     50% Petrosian: petroR50_u, petroR50_r, petroR50_z;
#     90% Petrosian: petroR90_u, petroR90_r, petroR90_z.

import numpy as np
from sklearn.tree import DecisionTreeClassifier


def splitdata_train_test(data, fraction_training):
    np.random.seed(0)
    np.random.shuffle(data)
    return data[:int(len(data)*fraction_training)], data[int(len(data)*fraction_training):]


def generate_features_targets(data):
    targets = data['class']

    features = np.empty(shape=(len(data), 13))
    features[:, 0] = data['u-g']
    features[:, 1] = data['g-r']
    features[:, 2] = data['r-i']
    features[:, 3] = data['i-z']
    features[:, 4] = data['ecc']
    features[:, 5] = data['m4_u']
    features[:, 6] = data['m4_g']
    features[:, 7] = data['m4_r']
    features[:, 8] = data['m4_i']
    features[:, 9] = data['m4_z']

    # concentration in u filter
    features[:, 10] = data['petroR50_u']/data['petroR90_u']
    # concentration in r filter
    features[:, 11] = data['petroR50_r']/data['petroR90_r']
    # concentration in z filter
    features[:, 12] = data['petroR50_z']/data['petroR90_z']

    return features, targets


def dtc_predict_actual(data):
    train, test = splitdata_train_test(data, 0.7)

    train_features, train_targets = generate_features_targets(train)
    test_features, test_targets = generate_features_targets(test)

    dtc = DecisionTreeClassifier()

    # Training Decision Tree model
    dtc.fit(train_features, train_targets)

    # Getting predictions
    predictions = dtc.predict(test_features)

    return predictions, test_targets


if __name__ == '__main__':
    data = np.load('galaxy_catalogue.npy')

    predicted_class, actual_class = dtc_predict_actual(data)

    # Print some of the initial results
    print("Some initial results...\n   predicted,  actual")
    for i in range(10):
        print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))
