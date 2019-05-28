from scipy.spatial.distance import cityblock
import numpy as np

np.set_printoptions(suppress=True)
import pandas
from error import evaluateEER


class ManhattanDetector:

    def __init__(self, subjects):
        self.user_scores = []
        self.imposter_scores = []
        self.mean_vector = []
        self.subjects = subjects


    def training(self):
        self.mean_vector = self.train.mean().values
        #print(self.mean_vector)

    def testing(self):
        for i in range(self.test_genuine.shape[0]):
            cur_score = cityblock(self.test_genuine.iloc[i].values,self.mean_vector)
            #print(cur_score/10)
            self.user_scores.append(cur_score)


        for i in range(self.test_imposter.shape[0]):
            cur_score = cityblock(self.test_imposter.iloc[i].values,self.mean_vector)
            self.imposter_scores.append(cur_score)

    def evaluateFalseRejection(self):
        eers = []

        for subject in subjects:
            self.user_scores = []
            self.imposter_scores = []
            genuine_user_data = data.loc[data.subject == subject,"H.period":"H.Return"]
            imposter_data = data.loc[data.subject != subject, :]

            self.train = genuine_user_data[:10]
            self.test_genuine = genuine_user_data[10:20]
            self.test_imposter = imposter_data.groupby("subject").head(10).loc[:, "H.period":"H.Return"]

            self.training()
            self.testing()
            print(subject+':')

            print(self.user_scores)
            scalingMax = np.amax(self.user_scores)
            scalingMin = np.amin(self.user_scores)
            scalingAll = []
            falseRejectionRate = []
            for i in self.user_scores:
                scaling = (i-scalingMin)/(scalingMax-scalingMin)
                scalingAll.append(scaling)

            counter = 0
            for j in scalingAll:
                if(j<0.85):
                    counter = counter+1

            falseRejectionRate.append(counter/len(scalingAll))
            print(scalingAll)
            print("False Rejection Rate: {0}".format(falseRejectionRate))

        #return np.mean(eers)

    def evaluateFalseAcceptance(self):
        eers = []

        for subject in subjects:
            self.user_scores = []
            self.imposter_scores = []
            genuine_user_data = data.loc[data.subject == subject, "H.period":"H.Return"]
            imposter_data = data.loc[data.subject != subject, :]

            self.train = genuine_user_data[:10]
            self.test_genuine = genuine_user_data[10:20]
            self.test_imposter = imposter_data.groupby("subject").head(10).loc[:, "H.period":"H.Return"]

            self.training()
            self.testing()
            print(subject + ':')

            print(self.user_scores)
            scalingMax = np.amax(self.user_scores)
            scalingMin = np.amin(self.user_scores)
            scalingAll = []
            falseAcceptionRate = []
            for i in self.imposter_scores:
                scaling = (i - scalingMin) / (scalingMax - scalingMin)
                scalingAll.append(scaling)

            counter = 0
            for j in scalingAll:
                if (j > 0.85):
                    counter = counter + 1

            falseAcceptionRate.append(counter / len(scalingAll))
            print(scalingAll)
            print("False Acception Rate:{0}".format(falseAcceptionRate))



        # return np.mean(eers)

    def evaluateWolf(self):


        for subject in subjects:
            self.user_scores = []
            self.imposter_scores = []
            genuine_user_data = data.loc[data.subject == subject, "H.period":"H.Return"]
            imposter_data = data.loc[data.subject != subject, :]

            self.train = genuine_user_data[:10]
            self.test_genuine = genuine_user_data[10:20]
            testtt = imposter_data.groupby("subject")
            self.test_imposter = testtt.first().head(10).loc[:, "H.period":"H.Return"]
            self.test_imposter = imposter_data.groupby("subject").head(10).loc[:, "H.period":"H.Return"]
            #self.test_wolf=imposter_data.groupby("s003").head(10).loc[:, "H.period":"H.Return"]

            self.training()
            self.testing()
            print(subject + ':')

            print(self.user_scores)
            scalingMax = np.amax(self.user_scores)
            scalingMin = np.amin(self.user_scores)
            scalingAll = []
            falseAcceptionRate = []
            for i in self.imposter_scores:
                scaling = (i - scalingMin) / (scalingMax - scalingMin)
                scalingAll.append(scaling)

            counter = 0
            for j in scalingAll:
                if (j > 0.85):
                    counter = counter + 1

            falseAcceptionRate.append(counter / len(scalingAll))
            print(scalingAll)
            print("False Acception Rate:{0}".format(falseAcceptionRate))

        # return np.mean(eers)


path = "F:\\keystroke\\DSL-StrongPasswordData.csv"
data = pandas.read_csv(path)
subjects = data["subject"].unique()
print("False Rejection Rates:")
#ManhattanDetector(subjects).evaluateFalseRejection()
print("False Acception Rates:")
#ManhattanDetector(subjects).evaluateFalseAcceptance()
ManhattanDetector(subjects).evaluateWolf()