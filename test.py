# Đầu tiên import thư viện pandas để đọc file csv
import pandas as pd
# Tiếp theo ta mở file testData.csv
df = pd.read_csv('testData.csv')
# và in ra màn hình 10 dòng đầu tiên
print(df.head(10))
# hoặc in ra màn hình toàn bộ dữ liệu
print(df.head(10))