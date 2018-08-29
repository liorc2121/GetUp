from sklearn.svm import SVC
from sklearn import tree
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import time
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2,  f_classif
from sklearn.model_selection import cross_val_score


k_best_sizes = [10, 20, 30, 50]


def select_k_features(data, labels, k):
    k_best = SelectKBest(score_func=f_classif, k=k)
    new_features = k_best.fit_transform(data, labels)
    return new_features, [i for i, v in enumerate(k_best.get_support()) if v]


class Classifier:
    def __init__(self, classifier, classifier_name):
        self.classifier = classifier
        self.classifier_name = classifier_name

    # classifier the data and print the accuracy of the Classifier
    def fit(self, feature_vector, feature_labels, k_times):
        try:
            print('\t' + self.classifier_name)
            start = time.time()
            avg_score = 0
            print('\t\tTest on all features')
            scores = cross_val_score(self.classifier, feature_vector, feature_labels, cv=k_times)
            print('\t\t\tcross-validation average scores: %.3f\n' % (sum(scores) / len(scores)))

            for size in k_best_sizes:
                if size < len(feature_vector):
                    new_data, selected_features = select_k_features(feature_vector, feature_labels, size)
                    scores = cross_val_score(self.classifier, new_data, feature_labels, cv=k_times)
                    print('\t\tTest on %d best features' % size)
                    print('\t\t\tcross-validation average scores: %.3f' % (sum(scores) / len(scores)))
                    print('\t\t\tthe indexes of the selected features are:')
                    print('\t\t\t' + str(selected_features))
                    print('')  # line separation between sizes



            '''

            kf = KFold(n_splits=k_times, shuffle=True)
            for train_indexes, test_indexes in kf.split(feature_vector):

                # Init all,  the vector by training set indexes
                training_feature_vector = [feature_vector[i] for i in train_indexes]
                result_training = [feature_labels[i] for i in train_indexes]
                test_feature_vector = [feature_vector[i] for i in test_indexes]
                result_test = [feature_labels[i] for i in test_indexes]

                # Calculate the success rate of the predict vector
                self.classifier.fit(training_feature_vector, result_training)
                predicted_vector = self.classifier.predict(test_feature_vector)
                avg_score += accuracy_score(result_test, predicted_vector)

            avg_score /= k_times
            print(self.classifier_name + ":" + "%.2f" % (avg_score * 100) + "%")
            end = time.time()
            print(self.classifier_name + ' total time to classify is' + str(end - start))
            '''
        except:
            print(self.classifier_name + ' is not completed')






class ClassifierFactory:
    def __init__(self):
        self.classifiers = [Classifier(SVC(), 'SVM'),
                            Classifier(tree.DecisionTreeClassifier(), 'DecisionTree'),
                            Classifier(KNeighborsClassifier(), 'KNN')]

    def fit_all(self, all_feature_vector, labels, k_times = 5):
        for classifier in self.classifiers:
            classifier.fit(all_feature_vector, labels, k_times)





