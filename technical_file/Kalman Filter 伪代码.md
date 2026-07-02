# Kalman Filter 伪代码（角度估计）

状态向量 $x = [\theta, b]^T$（角度 + 陀螺仪零偏），所有矩阵运算已展开为标量，可直接翻译为 C 代码。

```
初始化:
    dt = 0.01                            // 采样周期，100Hz
    angle = 0.0                          // 初始角度（可取加速度计第一拍的值）
    bias  = 0.0                          // 初始零偏

    // 协方差矩阵 P
    p00 = 1.0                            // 角度方差
    p01 = 0.0
    p10 = 0.0
    p11 = 1.0                            // 零偏方差

    // 过程噪声 Q
    q_angle = 0.001                      // 角度模型噪声
    q_bias  = 0.000003                   // 零偏漂移噪声（极慢）

    // 测量噪声 R
    r_measure = 0.03                     // 加速度计角度方差（静止时算得）


每个采样周期循环:

    // ============ 0. 读取传感器 ============
    gyro_rate   = read_gyroscope()       // 陀螺仪角速度
    accel_angle = read_accel_angle()     // 加速度计推算角度


    // ============ 1. 预测阶段 ============

    // 状态预测: x- = F*x + B*gyro_rate
    // F = [[1, -dt], [0, 1]]   B = [[dt], [0]]
    angle_pred = angle + (gyro_rate - bias) * dt
    bias_pred  = bias

    // 协方差预测: P- = F*P*F^T + Q
    // 矩阵乘法手动展开：
    p00_pred = p00 - dt*p10 - dt*(p01 - dt*p11) + q_angle
    p01_pred = p01 - dt*p11
    p10_pred = p10 - dt*p11
    p11_pred = p11 + q_bias


    // ============ 2. 更新阶段 ============

    // 新息: y = z - H*x- , H = [1, 0]
    innovation = accel_angle - angle_pred

    // 新息协方差: S = H*P-*H^T + R
    s = p00_pred + r_measure

    // 卡尔曼增益: K = P-*H^T / S
    k0 = p00_pred / s                    // 角度增益
    k1 = p10_pred / s                    // 零偏增益

    // 状态更新: x = x- + K*innovation
    angle = angle_pred + k0 * innovation
    bias  = bias_pred  + k1 * innovation

    // 协方差更新: P = (I - K*H)*P-
    p00 = (1.0 - k0) * p00_pred
    p01 = (1.0 - k0) * p01_pred
    p10 = p10_pred - k1 * p00_pred
    p11 = p11_pred - k1 * p01_pred


    // ============ 3. 输出 ============
    output_angle = angle                 // 融合后的最优角度
    output_rate  = gyro_rate - bias      // 零偏补偿后的角速度
```
