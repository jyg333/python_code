"""인풋 데이터를 받고 함수로 처리"""
"""시간 데이터에서 시간 값만 추출해서 time comparison_table과 비교해
sin cos 값을 리턴하는 함수 만들기"""
import re
from datetime import date
import pandas as pd


class TimeEncoder:

    # pandas series를 input parameter로 받고 list를 return
    def time2SinCos(time_data: pd.Series):

        len_data = len(time_data)
        alpha = time_data[0]  # 문자열에서 시간이 위치하는 인덱스를 찾기 위한 변수
        time_location = (re.search(r'\d{2}:', alpha).span(0)[0])  # 시간 데이터 인덱스

        # 시간별 sin-cos 비교 데이터

        time_comparison_data = pd.read_csv('time_comparison_table.csv')

        sin_list = []
        cos_list = []

        for k in range(len_data):
            temp = time_data[k]
            time_extraction = temp[time_location:time_location + 8]
            # print(time_extraction)

            x = time_extraction
            y = int(x[0:2]) * 3600 + int(x[3:5]) * 60 + int(x[6:8])
            # print("y : ",y, '\n')
            sin = time_comparison_data.iloc[y].time_sin
            cos = time_comparison_data.iloc[y].time_cos
            sin_list.append(sin)
            cos_list.append(cos)
            # print("sin : ",sin,'\n')
            # print("cos : ",cos,'\n')

        return sin_list, cos_list

    # 365일을 갖는 평년을 위한 메서드
    def day2SinCos(time_data: pd.Series):

        len_day = len(time_data)
        alpha = time_data[0]
        l = (re.search(r'\d{4}-\d{2}-\d{2}', alpha).span(0)[0])  # 시간 데이터 인덱스

        normal_year = pd.read_csv('normal_year_table.csv')
        # leap_year = pd.read_csv('leap_year_table.csv') # 윤년

        day_sin = []
        day_cos = []
        for k in range(len_day):
            temp = time_data[k]

            time_temp1 = date(int(temp[l:l + 4]), int(temp[l + 5:l + 7]), int(temp[l + 8:10]))
            time_temp = date(int(temp[l:l + 4]), 1, 1)

            date_delta = time_temp1 - time_temp  # 날짜 값 인덱스를 맞춰주기 위해 1더함
            date_delta = date_delta.days + 1  # timedelta type의 변수라 에러 가 있었음

            day_sin.append(normal_year.iloc[date_delta].sin_year)
            day_cos.append(normal_year.iloc[date_delta].cos_year)

        return day_sin, day_cos