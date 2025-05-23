# -*- coding: utf-8 -*-
"""data_preprocessing_tools.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yimBeV4oone-2fM7bClM4l7Vhn3ZQQ1f
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imputer.fit(X[:, 1:2])
X[:, 1:2] = imputer.transform(X[:, 1:2])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder="passthrough")
X = ct.fit_transform(X)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, 0:1] = sc.fit_transform(X_train[:, 0:1])
X_train[:, 2:3] = sc.fit_transform(X_train[:, 2:3])
X_train[:, 4:5] = sc.fit_transform(X_train[:, 4:5])
X_train[:, 10:11] = sc.fit_transform(X_train[:, 10:11])
X_train[:, 11:12] = sc.fit_transform(X_train[:, 11:12])
X_train[:, 12:13] = sc.fit_transform(X_train[:, 12:13])
X_test[:, 0:1] = sc.transform(X_test[:, 0:1])
X_test[:, 2:3] = sc.transform(X_test[:, 2:3])
X_test[:, 4:5] = sc.transform(X_test[:, 4:5])
X_test[:, 10:11] = sc.transform(X_test[:, 10:11])
X_test[:, 11:12] = sc.transform(X_test[:, 11:12])
X_test[:, 12:13] = sc.transform(X_test[:, 12:13])