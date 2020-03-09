# -*- coding:utf-8 -*-
# @Time : 2020/3/8 19:21
# @Author : Bravezhangw
# @File : send_sms.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import hashlib
import time

import requests

'''
	发送验证码
'''
def send_data():
	APP_KEY = "dc6a021fcb8b81a47890087fcb7cd75d"
	APP_SECRET = "b0bce63a6084"
	nonce = hashlib.new("sha256", str(time.time()).encode("utf-8")).hexdigest()
	cur_time = str(int(time.time()))
	sha1 = hashlib.sha1()
	sha1.update((APP_SECRET + nonce + cur_time).encode("utf-8"))
	CheckSum = sha1.hexdigest()
	url = 'https://api.netease.im/sms/sendcode.action'

	header = {
		"AppKey": APP_KEY,
		"Nonce": nonce,
		"CurTime":cur_time,
		"CheckSum":CheckSum
	}

	post_data = {
		"mobile": "13623613927"
	}
	response = requests.post(url=url, data=post_data,headers=header)
	print(response.content)


if __name__ == '__main__':
	send_data()