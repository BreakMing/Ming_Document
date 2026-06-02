## 案例简介

Vibe_Coding_Keyboard依托BS21E主控芯片与Lite OS系统开发，搭载星闪无线链路、USB‑HID收发架构，集成三个定制机械按键、PDM数字麦克风与1.14英寸TFT彩屏。设备上行传输按键指令与音频数据，电脑通过HID下发状态信息，打造轻量化编程辅助外设，免驱适配多系统，优化日常编码操作效率。


## 功能特点





## 目录结构
```
Vibe_Coding_Keyboard/
├── assets  
├── hardware # 硬件文件 
├── software # 软件固件  
└── README.md

```

## 固件烧录

### 硬件连接

使用下载调试模块按以下接线方式分别与接收模块和发送模块连接。

```

```

### 软件烧录

1、下载烧录工具

- 下载[BurnTool](https://gitee.com/hihope_iot/near-link/blob/master/tools/BurnTool_5.0.39.rar)工具，并压BurnTool压缩包。

2、进入BurnTool，点击“Setting”，波特率设置为750000。

![](assets/Hisi%20无线收发模块/file-20260525123345695.png)

3、选择端口，选择固件，并勾选“Auto burn”和“Auto disconnect”。

![](assets/Hisi%20无线收发模块/file-20260525123843382.png)

4、点击Connect，断开开发板连接的供电线，再重新连接开发板供电线，即可烧录固件。

![](assets/Hisi%20无线收发模块/file-20260525123949382.png)


## 功能调试




### 按键输入




### 语音输入




### 屏幕状态显示





## 调试建议













































