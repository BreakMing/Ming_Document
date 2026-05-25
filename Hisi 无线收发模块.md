# 案例简介

Hisi 无线收发模块是一个基于BS21e的案例，发送模块可以外部连接麦克风或串口设备，通过星闪连接，发送给接收模块，接收模块可以在电脑上模拟出一个USB-HID设备，获取到发送模块发送的数据。

# 功能特点

- 支持音频数据传输
- 支持星闪无线通信

# 开发指导

## 硬件连接

- 下单pcb板
- 焊接元器件
- 使用burnTool工具烧录固件


## 固件烧录

1、下载烧录工具

- 下载[BurnTool](https://gitee.com/hihope_iot/near-link/blob/master/tools/BurnTool_5.0.39.rar)工具
- 下载完成后打开BurnTool.exe文件

2、点击“Setting”，波特率设置为750000

![](assets/Hisi%20无线收发模块/file-20260525123345695.png)

3、选择端口

![](assets/Hisi%20无线收发模块/file-20260525123451068.png)

4、选择固件，并勾选“Auto burn”和“Auto disconnect”获取


