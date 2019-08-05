import requests

'''
    5-7 目的地 3 车次 6 出发地 8 出发时间 9 到达时间 10 历时 26 无座 29 硬座
    24 软座 28 硬卧 33 动卧 23 软卧 21 高级软卧 30 二等座 31 一等座 32 商务特等座
'''

response = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-07-25&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT')
result = response.json()
result = result['data']['result']
n = 0
for i in result:

	# print(i)
	list = i.split('|')    # 分割字符串
	for a in list:
		print(n, a)    # 打印信息编号
		n+=1
	n = 0
	# print(list)