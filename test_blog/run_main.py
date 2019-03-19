#!/usr/bin/python
# Author: QUZF
# Datetime: 2019/1/25 15:46

import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

# 这个是优化版：执行所有用例并发送报告，分四个步骤
# 1.加载用例
# 2.执行用例
# 3.获取最新测试报告
# 4.发送邮箱（这一步不想执行的话，注释掉最后面的函数即可）


def add_case(case_path, rule):
    """加载所有的测试用例"""
    testsuit = unittest.TestSuite()
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         testsuit.addTests(test_case)
    #         print(testsuit)
    testsuit.addTests(discover)    # 直接加载discover
    return testsuit


def run_case(all_case, report_path):
    """执行所有的用例，并把结果写入测试报告"""
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_abspath = os.path.join(report_path, now+"report.html")
    # report_abspath = "C:\\pycharm_workspace\\test_blog\\test_report\\"+now+"report.html"
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="自动化测试报告",
                                           description="用例执行情况：")
    # 调用add_case函数返回值
    runner.run(all_case)
    time.sleep(2)
    fp.close()


def get_report_file(report_path):
    """获取最新的测试报告"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print("最新测试生成的报告："+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtp_server, report_file):
    """发送最新的测试报告内容"""
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = "自动化测试报告"
    msg["from"] = sender
    msg["to"] = receiver
    # 加上时间戳
    # msg["date"] = time.strftime('%a,%d %b %Y %H_%M_%S %z')
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att)
    # 登录邮箱
    smtp = smtplib.SMTP()
    # 连接邮箱服务器
    smtp.connect(smtp_server)
    time.sleep(2)
    # 用户名密码
    smtp.login(sender, psw)
    time.sleep(2)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('Test report email has been sent out!')


if __name__ == '__main__':
    """测试用例的路径、匹配规则"""
    # case_path = "C:\\pycharm_workspace\\test_blog\\test_case"
    case_path = os.path.join(os.getcwd(), "test_case")
    rule = "test*.py"
    all_case = add_case(case_path, rule)     # 1.加载用例
    # 生成测试报告的路径
    time.sleep(2)
    # report_path = "C:\\pycharm_workspace\\test_blog\\test_report"
    report_path = os.path.join(os.getcwd(), "test_report")
    run_case(all_case, report_path)       # 2.执行用例
    # 获取最新的测试报告文件
    time.sleep(2)
    report_file = get_report_file(report_path)  # 3.获取最新的测试报告
    # 邮箱配置
    sender = "quzfeng@163.com"
    psw = "fengyongyunming"
    # 收件人多个时，中间用逗号隔开
    receiver = "64816640@qq.com"
    smtp_server = "smtp.163.com"
    # 4.最后一步发送报告,如果不需要就注释掉
    time.sleep(3)
    send_mail(sender, psw, receiver, smtp_server, report_file)




