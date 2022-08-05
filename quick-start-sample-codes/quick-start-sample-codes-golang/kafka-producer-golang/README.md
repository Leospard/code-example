# kafka-producer-fc-event-golang 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=FCToODPSSamplePython3&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=FCToODPSSamplePython3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=FCToODPSSamplePython3&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=FCToODPSSamplePython3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=FCToODPSSamplePython3&type=packageDownload">
  </a>
</p>


## 前期准备

### 权限准备

使用该项目，确认您的操作账户拥有以下的产品权限 / 策略：


| 服务/业务 | 函数计算                                                     |
| --------- | ------------------------------------------------------------ |
| 权限/策略 | AliyunFCFullAccess<br/>AliyunKafkaFullAccess<br/>AliyunVPCReadOnlyAccess |


### 资源准备

  * 一个可用的Kafka消息队列，可参考消息队列Kafka版官方文档[消息队列快速入门](https://help.aliyun.com/document_detail/99949.html)。

    - 创建VPC专有网络（推荐在生产环境中也使用VPC），可参考[VPC官方文档](https://help.aliyun.com/document_detail/65398.htm?spm=a2c4g.11186623.0.0.61be4c9d4aGfpg#task-1012575)。VPC控制台[链接](https://vpcnext.console.aliyun.com/)。至此即可拥有VPC和相应交换机。

    > 部署Kafka实例时会提示创建可用的VPC专有网络

  * 在Kafka控制台创建需要使用的Kafka Topic与Consumer Group。

### 环境准备

由于Go的Kafka客户端程序包含CGO，虽然Go拥有交叉编译器，但如果没有安装相应交叉编译C的工具链，无法直接编译出跨平台的可执行文件。即当我们使用了CGO时，要想实现跨平台编译，同时需要让C/C++代码也支持跨平台编译。

函数计算的环境为Linux / amd64所以其他操作系统要构建相应可执行文件需要相应环境。

- Mac

  ```bash
  # 下载linux编译工具链
  brew install FiloSottile/musl-cross/musl-cross
  ```
  
- Windows / Mac

  ```bash
  # 拉取镜像
  docker pull karalabe/xgo-latest
  ```
# 代码 & 预览

- [ :smiley_cat:  源代码](https://github.com/devsapp/)
- 为了能够成功部署本样例代码，您在部署过程中需要提供以下参数：
  - 地域 (region): 您需要通过这个参数配置您函数计算服务需要部署的地域，默认值为 cn-hangzhou (杭州)。
    - 为您提供的地域选项为：
      - cn-beijing (北京)
      - cn-hangzhou (杭州)
      - cn-shanghai (上海)
      - cn-qingdao (青岛)
      - cn-zhangjiakou (张家口)
      - cn-huhehaote (呼和浩特)
      - cn-shenzhen (深圳)
      - cn-chengdu (成都)
      - cn-hongkong (香港)
      - ap-southeast-1 (新加坡)
      - ap-southeast-2 (悉尼)
      - ap-southeast-3 (吉隆坡)
      - ap-southeast-5 (雅加达)
      - ap-northeast-1 (东京)
      - eu-central-1 (法兰克福)
      - eu-west-1 (伦敦)
      - us-west-1 (硅谷)
      - us-east-1 (弗吉尼亚)
      - ap-south-1 (孟买)
  - 服务名 (service name): 您需要给您的函数计算服务进行命名，服务名称，只能包含字母、数字、下划线和中划线。不能以数字、中划线开头。长度在 1-128 之间，默认值为 kafka-producer-quick-start。
  - 函数名 (function name): 您需要给您的函数计算函数进行命名，函数名称，只能包含字母、数字、下划线和中划线。不能以数字、中划线开头。长度在 1-64 之间。默认值为 kafka-producer-event-function-golang。
  - vpcId: 我们推荐您使用VPC访问Kafka，选择创建Kafka实例时使用的VPC。注意需要填写函数计算支持的 az。
  - vswitchIds:  使用vpc中的vswitch id, 用于内网访问 kafka。
  - securityGroupId:  kafka 实例所在 vpc 的安全组id，可在`云服务器 ECS`控制台`网络与安全`菜单项找到。
  - Kafka接入点 (bootstrapServers): 您购买的Kafka实例的默认接入点，可以在实例详情中
  - topicName: Kafka实例的topic name, 此topic的数据生产会触发部署函数，需要您提前创建。

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=kafka-producer-fc-event-golang) ，
   [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=kafka-producer-fc-event-golang)  该应用。（此方法在此应用下仅支持Linux环境。推荐使用 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署）

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：

  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init kafka-producer-fc-event-golang -d kafka-producer-fc-event-golang`
  - 填入在以上模块介绍的参数
  - 进入项目目录，`cd kafka-producer-fc-event-golang`根据使用环境选择相应`pre-deploy`中`run`的字段。
  - 进行项目部署： `s deploy -y`
- 本地调试
  - 进入应用项目工程下，执行下面命令：`s invoke -e '{"Key": "test go kafka producer"}'`。
  - 即可查看到模拟事件触发函数后的结果。

```bash
========= FC invoke Logs begin =========
FC Invoke Start RequestId: ae8994c8-03fe-4d65-8726-3529e4150c80
2022-08-03T08:39:51.098Z ae8994c8-03fe-4d65-8726-3529e4150c80 [INFO] main.go:73: sending the message to kafka: test go kafka producer!
%3|1659515992.098|FAIL|rdkafka#producer-1| [thrd:123:9092/bootstrap]: 123:9092/bootstrap: Failed to connect to broker at 0.0.0.123:9092: Invalid argument (after 1ms in state CONNECT, 1 identical error(s) suppressed)
FC Invoke End RequestId: ae8994c8-03fe-4d65-8726-3529e4150c80

Duration: 2001.49 ms, Billed Duration: 2002 ms, Memory Size: 128 MB, Max Memory Used: 16.54 MB
========= FC invoke Logs end =========

FC Invoke instanceId: c-62ea33c8-fad19eba6bb641218616

FC Invoke Result:
"Finish sending the message to kafka: test go kafka producer!"


End of method: invoke
```

​		

- 端对端测试

  - 登陆函数计算控制台，进入对应的函数配置测试参数为`{"key":"test kafka producer go"}`（注意参数需要配置为键值为"Key"的json形式【"Key"是在demo程序中设定的，可修改】）点击`测试函数`
  
  返回结果如下：

  ```bash
  "Finish sending the message to kafka: test kafka producer go!"
  ```
  日志如下：
  
  ```bash
  2022/08/03 08:40:51.351737 start
  FC Initialize Start RequestId: 21319b27-95ac-47ba-a62b-00324fb76aa0
  2022-08-03 16:40:51 21319b27-95ac-47ba-a62b-00324fb76aa0 [INFO] main.go:35: Initializing the kafka config
  FC Initialize End RequestId: 21319b27-95ac-47ba-a62b-00324fb76aa0
  FC Invoke Start RequestId: 89973d15-8831-4326-9f93-4f84fa5b074c
  2022-08-03 16:40:53 89973d15-8831-4326-9f93-4f84fa5b074c [INFO] main.go:73: sending the message to kafka: test kafka producer go!
  2022/08/03 08:40:53.874318 Send OK topic:HelloTopic partition:6 offset:16 content:test kafka producer go
  FC Invoke End RequestId: 89973d15-8831-4326-9f93-4f84fa5b074c
  ```
  
  - 登陆Kafka控制台，查看对应实例的对应Topic`消息详情`，找到对应分区，即可查询到相应消息。
  
  

</deploy>

<appdetail id="flushContent">

# 应用详情



本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑



</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">



| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <center>微信公众号：`serverless`</center>                    | <center>微信小助手：`xiaojiangwh`</center>                   | <center>钉钉交流群：`33947367`</center>                      |

</p>

</devgroup>