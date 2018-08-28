from sklearn.svm import SVC
from sklearn import tree
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import time


class Classifier:
    def __init__(self, classifier, classifier_name):
        self.classifier = classifier
        self.classifier_name = classifier_name

    # classifier the data and print the accuracy of the Classifier
    def fit(self, feature_vector, feature_labels, k_times):
        try:
            start = time.time()
            avg_score = 0
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
        except:
            print(self.classifier_name + ' is not completed')


class ClassifierFactory:
    def __init__(self):
        self.classifiers = [Classifier(SVC(), 'SVM'),
                            Classifier(MultinomialNB(), 'Naive Bayes:'),
                            Classifier(tree.DecisionTreeClassifier(), 'DecisionTree'),
                            Classifier(KNeighborsClassifier(), 'KNN')]

    def fit_all(self, all_feature_vector, all_label, k_times):
        for classifier in self.classifiers:
            classifier.fit(all_feature_vector, all_label, k_times)
