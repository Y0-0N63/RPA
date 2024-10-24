import pandas as pd
import matplotlib.pylab as plt
from matplotlib import font_manager

hat = pd.read_csv('ch4-2.csv')
print(hat.describe(), end='\n\n')

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family = font_name)

plt.figure(figsize = (10, 17))

# plt.subplot(1, 2, 1)      
plt.hist(hat.weight, bins = 7)

plt.title('부화장 병아리 무게 분포 현황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

plt.show()