"""
本代码样例主要实现以下功能:
* 从环境变量中解析出 MNS 主题模型的配置信息
* 根据以上获取的信息，初始化 MNS 客户端
* 向 MNS 写入一条测试数据


This sample code is mainly doing the following things:
* Get MNS configuration information from environment variables
* Initiate MNS client
* Send a test message to MNS Topic

"""
# -*- coding: utf-8 -*-
import logging
import os
from mns.account import Account
from mns.topic import *

my_topic = None
topic_name = ""

def initialize(context):
    global my_topic , topic_name
    # 从参数上下文中拿到一组临时密钥，避免了您把自己的AccessKey信息编码在函数代码里
    access_key_id = context.credentials.access_key_id
    access_key_secret = context.credentials.access_key_secret
    security_token = context.credentials.security_token
    # 获取自己 mns 的推送地址 Endpoint
    mns_endpoint = os.getenv("MNS_ENDPOINT")
    # 获取自己 mns topic 的名称
    topic_name = os.getenv("MNS_TOPIC_NAME")
    # 创建mns实例
    my_account = Account(mns_endpoint, access_key_id,
                         access_key_secret, security_token)
    # 获取mns实例的一个Topic对象
    my_topic = my_account.get_topic(topic_name)


def handler(environ, start_response):
    logger = logging.getLogger()
    
    logger.info("Publish Message To Topic {}".format(topic_name))

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    
    try:
        msg_body = "I am a test message."
        msg = TopicMessage(msg_body)
        re_msg = my_topic.publish_message(msg)
        start_response(status, response_headers)
        return "Publish Message Succeed. MessageBody:%s MessageID:%s" % (msg_body, re_msg.message_id)
    except MNSExceptionBase as e:
        if e.type == "TopicNotExist":
            logger.info("Topic '{}' not exist, please create topic before send message.".format(topic_name))
        raise RuntimeError(e)
