import pickle

# 指定pickle文件的路径
pickle_file_path = 'ta1-theia-e3-official-6r-00.pickle'

# 打开pickle文件并读取内容
with open(pickle_file_path, 'rb') as f:
    data = pickle.load(f)

# 打印读取的数据
print(data)
