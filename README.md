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

*若您想看到更多输出信息（用于debug等），可将```main.py```首行的debugging置为1。