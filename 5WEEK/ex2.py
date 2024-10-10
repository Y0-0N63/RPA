import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x, y) :
  for i in range(len(x)):
    plt.text(i, y[i]+0.5, y[i], ha = 'center')

# singer 변수에 데이터셋 입력
singer = pd.read_csv('singer_youtube.csv')
# 위에서부터 5개 데이터 확인
print(singer.head(), end="\n\n")

font_path = 'malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family = font_name)

plt.figure(figsize=(15, 10))
plt.bar(singer['name'], singer['youtube count'], color = ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple'))
plt.title('Youtube count by Singer')
plt.xlabel('Singer')
plt.ylabel('Youtube count')

addtext(singer['name'], singer['youtube count'])

plt.show()
