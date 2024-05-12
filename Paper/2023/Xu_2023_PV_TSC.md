<!--
 * @Author: pangay 1623253042@qq.com
 * @Date: 2024-05-12 17:01:04
 * @LastEditors: pangay 1623253042@qq.com
 * @LastEditTime: 2024-05-12 17:20:23
-->
# PV-TSC: Learning to Control Traffic Signals for Pedestrian and Vehicle Traffic in 6G Era
- [PV-TSC: Learning to Control Traffic Signals for Pedestrian and Vehicle Traffic in 6G Era](#pv-tsc-learning-to-control-traffic-signals-for-pedestrian-and-vehicle-traffic-in-6G-era)
  - [Introduction](#introduction)
    - [问题背景](#问题背景)
    - [传统方法存在的问题](#传统方法存在的问题)
    - [本文的解决方法](#本文的解决方法)

  - [Experiment](#experiment)
  - [Conclusion](#conclusion)

## Introduction

### 问题背景
交通环境中，行人安全和车辆都很重要，交通信号控制可以优化车辆和行人的通行效率和安全相关的问题。
### 传统方法问题

1. 传统方法较少考虑行人，它们无法保证行人没有无限等待时间，在性能上存在一些不足。
2. 传统方法中的固定时间控制无法根据实时交通情况做出调整，导致车辆和行人的行车时间和等待时间无法最优化
3. 传统方法中的信号控制方案可能存在无法避免的无限等待情况，影响交通流畅度和效率
4. 行人识别，之前使用摄像头的多一些，但是不能确定行人的移动方向，因为人行道上不区分移动方向。此处考虑使用 6G 的方法。

### 本文的解决方法

本文的解决方法是通过引入Pedestrian-Vehicle Trafﬁc Signal Control (PV-TSC)方案来实现的。PV-TSC考虑了行人和车辆交通，设计了基于不同排队行为的强化学习方案，以有效调度交通信号以实现安全和高效的出行。该方法是分散的，对于多个交叉口有良好的可扩展性。此外，PV-TSC将“压力”奖励扩展到行人交通流，有效地将邻近交叉口的信息整合到本地模型中。