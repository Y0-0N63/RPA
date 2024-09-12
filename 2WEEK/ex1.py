import pandas as pd

data = {
  '과목번호' : ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
  '과목명' : ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의 세계'],
  '강의실' : ['R1', 'R2', 'R3', 'R4', 'R2', 'R3'],
  '시간수' : [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df, end="\n\n")

sr_name = df['과목명']
print(sr_name, end="\n\n")

sr_no = df.loc[2]
print(sr_no, end='\n\n')

cell_name = df.loc[2]['과목명']
print(cell_name)

df.to_csv("file.csv", index=False)