


## 数据格式解读章节

### 串口发送CAN格式

![](assets/CAN_脚本/file-20260408173823815.png)


CAN 230 4 01 02 03 04

这一串协议中

- CAN：代表这些数据走的是CAN协议
- 230：CAN_ID的值
- 4：dlc  数据长度
- 01 02 03 04：数据内容

### 示波器捕获标准CAN协议

![](assets/CAN_脚本/file-20260409102554632.png)





## 电机通信相关章节

### PP系列电机协议解读（CAN）

![](assets/CAN_脚本/file-20260409103733214.png)

- CAN_ID：基本ID0x01~0xff可用，0x00为广播
- DLC：CAN数据帧长度
- CMD：命令类型
- ADDR：指令地址，也可以理解为寄存器地址
- data0~data3：数据内容，大端模式（高位在前）

命令类型表：

![](assets/CAN_脚本/file-20260409105126510.png)

指令地址：（部分）
![](assets/CAN_脚本/file-20260409105142939.png)


### CAN和CANOPEN的区别




### PHU系列电机血祭解读（PHU）































































