## qndxx_qcsh
自动打卡。支持批量打卡。

## 使用方式

在```main.py```同文件夹下创建```student_info.json```（可参照```student_info_example.json```）。

填入以下信息：

- ```cardNo```中填入您的学号或名字（打卡时想展示的信息）

- ```nid```中填入您的团支部id。在您选择完团支部后，可以看到此信息。提示：nid所在的url格式为：

> https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/organization/children?pid={一串N打头的东西，把它填入nid即可}

- ```openid```填入您的微信登录青春上海时的openid（不会变）。该信息可在您填写完毕信息，点击```去学习```后，从系统对你post的request返回的json中的```["result"]["openid"]```获得。提示：该request的url为：

> https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join?accessToken={balabala}

## 其它申明
- 若系统接口有变，不保证本repo及时更新。
- 认识怡宝的可以把信息发给他的bot，实现全自动打卡。
- 关于openid的获取：微信电脑端打开青春上海公众号，右上角点击发消息，然后点击青年大学习按钮。记得微信设置中关闭“使用系统默认浏览器打开链接”。不提供任何形式的抓包教学。
- 若您想看到更多输出信息（用于debug等），可将```main.py```首行的debugging置为1。