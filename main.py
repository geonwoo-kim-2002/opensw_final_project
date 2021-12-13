import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

주택매매가격지수 = pd.read_csv('주택매매가격지수.csv')
주택전세가격지수 = pd.read_csv('주택전세가격지수.csv')
연도별출산율 = pd.read_csv('연도별출산율.csv')

fig, ax1 = plt.subplots()

연도별출산율.plot(kind='line', x='날짜', ax=ax1)
plt.title("연도별 조출생률")

fig, ax1 = plt.subplots()

주택매매가격지수.plot(kind='line', x='날짜', y='총지수[2019.01=100]', color='green', ax=ax1)
ax1.set_ylabel('주택매매가격지수(2019.01=100)')
ax2 = ax1.twinx()
연도별출산율.plot(kind='line', x='날짜', y='전국', color='red', ax=ax2)
ax2.set_ylabel('전국 조출생률')
plt.title("전국 주택매매가격지수와 조출생률")

fig, ax1 = plt.subplots()

주택전세가격지수.plot(kind='line', x='날짜', y='총지수[2019.01=100]', color='green', ax=ax1)
ax1.set_ylabel('주택전세가격지수(2019.01=100)')
ax2 = ax1.twinx()
연도별출산율.plot(kind='line', x='날짜', y='전국', color='red', ax=ax2)
ax2.set_ylabel('전국 조출생률')
plt.title("전국 주택전세가격지수와 조출생률")

fig, ax1 = plt.subplots()

주택매매가격지수.plot(kind='line', x='날짜', y='총지수(서울)[2019.01=100]', color='green', ax=ax1)
ax1.set_ylabel('서울 주택매매가격지수(2019.01=100)')
ax2 = ax1.twinx()
연도별출산율.plot(kind='line', x='날짜', y='서울특별시', color='red', ax=ax2)
ax2.set_ylabel('서울 조출생률')
plt.title("서울 주택매매가격지수와 조출생률")

fig, ax1 = plt.subplots()

주택전세가격지수.plot(kind='line', x='날짜', y='총지수(서울)[2019.01=100]', color='green', ax=ax1)
ax1.set_ylabel('서울 주택전세가격지수(2019.01=100)')
ax2 = ax1.twinx()
연도별출산율.plot(kind='line', x='날짜', y='서울특별시', color='red', ax=ax2)
ax2.set_ylabel('서울 조출생률')
plt.title("서울 주택전세가격지수와 조출생률")

plt.show()
