"""
 scikit-lego, which is a library containing numerous useful functionalities that are expanding scikit-learn’s capabilities.

 -variable
    day_nr : a numeric index representing the passage of time
    day_of_year : the ordinal day of the year

 - sk learn의 fit_transform() : train dataset에서만 사용됨, fit()과 tramsform()을 한번에 처리할 수 있게 하는 메서드
    FunctionTransformer : function or function object and returns the result of this
    function. This is useful for stateless transformations such as taking the
    log of frequencies, doing custom scaling

    초 단위로 인코딩을 하기 위해서 시-분-초를 int형태로 바꿔줘야 한다. 1일을 한 주기로 사인함수 매핑
    sine 함수와 cos 함수 두가지 값을 모두 사용해 줘야 한다.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import mean_absolute_error
# from sklego.preprocessing import RepeatingBasisFunction

second_data = pd.read_csv('../clustering/converted_data.csv')
# for reproducibility
np.random.seed(42)

# generate the DataFrame with dates
range_of_dates = pd.date_range(start="2017-01-01",
                           	end="2020-12-30")
X = pd.DataFrame(index=range_of_dates)

# create a sequence of day numbers
X["day_nr"] = range(len(X))
X["day_of_year"] = X.index.day_of_year
print("X : ",'\n',X)


# =====================================================================

# generate the components of the target
# signal_1 = 3 + 4 * np.sin(X["day_nr"] / 365 * 2 * np.pi)
# signal_2 = 3 * np.sin(X["day_nr"] / 365 * 4 * np.pi + 365/2)
# noise = np.random.normal(0, 0.85, len(X))
#
# # combine them to get the target series
# y = signal_1 + signal_2 + noise
#

# # plot
# y.plot(figsize=(16,4), title="Generated time series");
# =====================================================================

def sin_transformer(period):
	return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))

def cos_transformer(period):
	return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))


print(second_data['starttime'])
X_2 = X.copy()
X_2["month"] = X_2.index.month # 해당하는 월을 추가한 데이터
X_2["month_sin"] = sin_transformer(12).fit_transform(X_2)["month"]
X_2["month_cos"] = cos_transformer(12).fit_transform(X_2)["month"]
X_2["day_sin"] = sin_transformer(365).fit_transform(X_2)["day_of_year"]
X_2["day_cos"] = cos_transformer(365).fit_transform(X_2)["day_of_year"]

# second_data["day_sin"] = sin_transformer(86400).fit_transform(second_data)["starttime"]
# second_data["day_cos"] = cos_transformer(86400).fit_transform(second_data)["starttime"]


print(X_2)
# print(second_data)
# fig, ax = plt.subplots(2, 1, sharex=True, figsize=(16,8))
# # second_data[["month_sin", "month_cos"]].plot(ax=ax[0])
# second_data[["day_sin", "day_cos"]].plot(ax=ax[1])
# plt.suptitle("Cyclical encoding with sine/cosine transformation");
# plt.show()