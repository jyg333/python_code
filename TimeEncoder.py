"""
 scikit-lego, which is a library containing numerous useful functionalities that are expanding scikit-learn’s capabilities.

 - 초 단위로 인코딩을 하기 위해서 시-분-초를 int형태로 바꿔줘야 한다. 1일을 한 주기로 사인-코사인 함수 매핑
    sine 함수와 cos 함수 두가지 값을 모두 사용해 줘야 한다.

 -variable
    day_nr : a numeric index representing the passage of time
    day_of_year : the ordinal day of the year

 - sk learn의 fit_transform() : train dataset에서만 사용됨, fit()과 tramsform()을 한번에 처리할 수 있게 하는 메서드
    FunctionTransformer : function or function object and returns the result of this
    function. This is useful for stateless transformations such as taking the
    log of frequencies, doing custom scaling
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
import re

class TimeEncoder:

    def sin_transformer(self,period):
        return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))

    def cos_transformer(self,period):
        return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))

    def daySin(self, day_column=None):

        day : int = 86400
        trans =  self.sin_transformer(day).fit_transform(day_column)

        return trans

    def dayCos(self, day_column):

        day:int = 86400
        trans = self.cos_transformer(day).fit_transform(day_column)

        return trans

    def yearSin(self, year_column):

        year : int = 365
        trans = self.sin_transformer(year).fit_transform(year_column)

        return trans

    def yearCos(self, year_column):

        year : int = 365
        trans = self.sin_transformer(year).fit_transform(year_column)

        return trans
