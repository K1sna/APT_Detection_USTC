import pickle

# 指定pickle文件的路径
pickle_file_path = '"D:/BaiduSyncdisk/workspace/2024/PartTime/Part-time/中科大/1/0329-0404 TODO/darpa-tc-e3数据处理为事件边/trace主机/ta1-trace-e3-official-1-03-new.pickle"'

# 打开pickle文件并读取内容
with open(pickle_file_path, 'rb') as f:
    data = pickle.load(f)

# 打印读取的数据
print(data)
