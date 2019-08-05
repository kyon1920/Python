import requests
import re
import os

def getStation():
	url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
	response = requests.get(url,verify=True)    # 发送网络请求并验证
	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
	stations = dict(stations)    # 转换为字典形式
	stations = str(stations)    # 转换为字符串类型，否则无法写入文件
	write(stations)    # 调用写入方法，实现下载车站文件

def write(stations):
	file = open('stations.txt','w',encoding = 'utf-8_sig')    # 写入模式打开文件
	file.write(stations)    # 写入文件
	file.close()
def read():
	file = open('stations.txt','r',encoding = 'utf-8_sig')    # 以读模式打开文件
	data = file.readline()    # 以行形式读取文件
	file.close()
	return data
def isStations():
	isStations = os.path.exists('stations.txt')    # 判断车站文件是否存在
	return isStations