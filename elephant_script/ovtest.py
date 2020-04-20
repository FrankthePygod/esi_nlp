import pandas as pd


df = pd.read_excel('C:/Users/xqm50/Downloads/2019_Holiday_Program.xlsx',sheet_name=0)

# df: drop the first 3 columns:
df.drop(['KO KEY BRAND','KO KEY PACKAGE','Weeks'], axis = 1, inplace = True)
df.head()
df.shape

# define X_train, y_trian, X_test, y_test:

from sklearn import preprocessing

X_li = list(df.columns.values)
X_li.remove('Incr $')
y = 'Incr $'
X = df[X_li]
y = df[y]


# get rid of high VIF:

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer
from statsmodels.stats.outliers_influence import variance_inflation_factor

class ReduceVIF(BaseEstimator, TransformerMixin):
    def __init__(self, thresh=5.0, impute=True, impute_strategy='median'):
        # From looking at documentation, values between 5 and 10 are "okay".
        # Above 10 is too high and so should be removed.
        self.thresh = thresh

        # The statsmodel function will fail with NaN values, as such we have to impute them.
        # By default we impute using the median value.
        # This imputation could be taken out and added as part of an sklearn Pipeline.
        if impute:
            self.imputer = Imputer(strategy=impute_strategy)

    def fit(self, X, y=None):
        print('ReduceVIF fit')
        if hasattr(self, 'imputer'):
            self.imputer.fit(X)
        return self

    def transform(self, X, y=None):
        print('ReduceVIF transform')
        columns = X.columns.tolist()
        if hasattr(self, 'imputer'):
            X = pd.DataFrame(self.imputer.transform(X), columns=columns)
        return ReduceVIF.calculate_vif(X, self.thresh)

    @staticmethod
    def calculate_vif(X, thresh=5.0):
        # Taken from https://stats.stackexchange.com/a/253620/53565 and modified
        dropped=True
        while dropped:
            variables = X.columns
            dropped = False
            vif = [variance_inflation_factor(X[variables].values, X.columns.get_loc(var)) for var in X.columns]

            max_vif = max(vif)
            if max_vif > thresh:
                maxloc = vif.index(max_vif)
                print(f'Dropping {X.columns[maxloc]} with vif={max_vif}')
                X = X.drop([X.columns.tolist()[maxloc]], axis=1)
                dropped=True
        return X

transformer = ReduceVIF()

X = transformer.fit_transform(X[X.columns[-10:]], y)

X.head()

#train test split:

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
X_train, X_test, y_train, y_test

# standardization
from sklearn import preprocessing
 X_scaled = preprocessing.scale(X_train)
 y_scaled = preprocessing.scale(y_train)

# for later usage of test set:

scaler = preprocessing.StandardScaler().fit(X_train)
scaler.mean_
scaler.scale_
scaler.transform(X_test)
scaler.transform(y_test)

# model
from sklearn.linear_model import LinearRegression

# train model

reg = LinearRegression().fit(X_train, y_train)

reg.score(X_test,y_test)
reg.score(X_train,y_train)

#cross validation to check for R2 stability to prevent overfit:

from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer
from sklearn.metrics import confusion_matrix


scores = cross_validate(reg, X_train, y_train, cv=10,
                        scoring=('r2', 'neg_mean_squared_error'),
                        return_train_score=True)

scores['train_r2']
reg.get_params()

reg.coef_[0]

for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, reg.coef_[idx]))

# get full stats report:

import statsmodels.api as sm
from scipy import stats


X2 = sm.add_constant(X_train)
est = sm.OLS(y_train, X2)
est2 = est.fit()
print(est2.summary())
