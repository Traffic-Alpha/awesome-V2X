# Awesome V2X

A curated list of Vehicle to X (V2X) resources (continually updated). You can reference [Journal Information](./Paper/Journal_Information/) for more information.

## Table of Contents

- [Awesome V2X](#awesome-v2x)
  - [Table of Contents](#table-of-contents)
  - [Paper](#paper)
    - [2017](#2017)
    - [2018](#2018)
    - [2021](#2021)
    - [2023](#2023)
    - [2024](#2024)
  - [License](#license)


## Paper

```
format:
- [title](paper link) [links]
  - author1, author2, and author3...
  - keyword
  - publisher
  - code
  - experiment environments and datasets
  - paper reading url
```

### 2017

- [CARLA: An Open Urban Driving Simulator](https://proceedings.mlr.press/v78/dosovitskiy17a.html)
  - Alexey Dosovitskiy, German Ros, Felipe Codevilla, Antonio Lopez, Vladlen Koltun
  - Proceedings of the 1st Annual Conference on Robot Learning, PMLR 78:1-16, 2017.
  - [Paper Reading](./Paper/2017/Dosovitskiy_CARLA.md), (Carla 仿真平台)
  - 介绍了 Carla 仿真平台，从两个方面，（1）Carla 仿真部分；（2）给了一个 benchmark，测试不同决策的结果；

### 2018

- [Microscopic Traffic Simulation using SUMO](https://ieeexplore.ieee.org/document/8569938)
  - Pablo Alvarez Lopez, Michael Behrisch, Laura Bieker-Walz, Jakob Erdmann, Yun-Pang Flotterod, Robert Hilbrich, Leonhard Lucken, Johannes Rummel, Peter Wagner and Evamarie Wießner
  - 2018 21st International Conference on Intelligent Transportation Systems (ITSC)
  - [Paper Reading](./Paper/2018/Lopez_2018_Microscopic_SUMO.md), (SUMO 仿真平台，无需多言)
  - 把 SUMO 主要功能介绍了一遍。通过一个例子，介绍了路网生成，流量生成，仿真过程中的模型等。读一下对 SUMO 有更多的理解，有更多场景生成的方式。

### 2021

- [Planning and Decision-making for Connected Autonomous Vehicles at Road Intersections: A Review](https://cjme.springeropen.com/articles/10.1186/s10033-021-00639-3)
  - Shen Li, Keqi Shu, Chaoyi Chen and Dongpu Cao
  - Planning, Decision-making, Autonomous intersection management, Connected autonomous vehicles
  - Chinese Journal of Mechanical Engineering
  - [Paper Reading](./Paper/2021/Li_2021_Planning_and_Decision_making.md)


### 2023

- [GPT-Driver: Learning to Drive with GPT](https://arxiv.org/abs/2310.01415)
  - Jiageng Mao, Yuxi Qian, Hang Zhao, Yue Wang
  - [Paper Reading](./Paper/2023/Mao_2023_GPT-Driver.md), (轨迹规划, 大语言模型)

- [Drive as You Speak: Enabling Human-Like Interaction with Large Language Models in Autonomous Vehicles](https://arxiv.org/abs/2309.10228)
  - Can Cui, Yunsheng Ma, Xu Cao, Wenqian Ye, Ziran Wang
  - [Paper Reading](./Paper/2023/Cui_2023_Drive_As_You_Speak.md), (自动驾驶, 大语言模型)

- [Receive, Reason, and React: Drive as You Say with Large Language Models in Autonomous Vehicles](https://arxiv.org/abs/2310.08034)
  - Can Cui, Yunsheng Ma, Xu Cao, Wenqian Ye, Ziran Wang
  - [Paper Reading](./Paper/2023/Cui_2023_Receive,_Reason_React.md), (自动驾驶, 大语言模型)，这一篇上 `Drive as You Speak` 的详细版本

- [Talk2BEV: Language-enhanced Bird’s-eye View Maps for Autonomous Driving](https://arxiv.org/abs/2310.02251)
  - Tushar Choudhary, Vikrant Dewangan, Shivam Chandhok, Shubham Priyadarshan, Anushka Jain, Arun K. Singh, Siddharth Srivastava, Krishna Murthy Jatavallabhula, K. Madhava Krishna
  - [Paper Reading](./Paper/2023/Choudhary_2023_Talk2BEV.md), (自动驾驶, 场景理解, 大语言模型)

- [Network Clustering-based Multi-agent Reinforcement Learning for Large-scale Traffc Signal Control](https://ieeexplore.ieee.org/abstract/document/10364020)
  - Zhicheng Tao, Chao Li, Qinmin Yang
  - 2023 International Annual Conference on Complex Systems and Intelligent Science (CSIS-IAC)
  - [Paper Reading](./Paper/2023/Tao_2023_Network_Clustering_TSC.md), (信号灯控制, 路口相似度聚类)

- [Open-TI: Open Traffic Intelligence with Augmented Language Model](https://arxiv.org/abs/2401.00211)
  - Longchao Da, Kuanru Liou, Tiejin Chen, Xuesong Zhou, Xiangyong Luo, Yezhou Yang, Hua Wei
  - [Paper Reading](./Paper/2023/Da_2023_Open-TI.md), (智慧交通系统, 人机交互, 大语言模型)

- [LLM-ASSIST: Enhancing Closed-Loop Planning with Language-Based Reasoning](https://arxiv.org/abs/2401.00125)
  - S P Sharan, Francesco Pittaluga, Vijay Kumar B G, Manmohan Chandraker
  - [Paper Reading](./Paper/2023/Sharan_2023_LLM-Assist.md), (轨迹生成, 自动驾驶, 大语言模型)
  - 利用 rule-based planner + LLM，如果 rule-based planner 产生的轨迹得分较低，则使用 LLM 去分析场景并产生新的轨迹。

- [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918)
  - Yuqi Wang, Jiawei He, Lue Fan, Hongxin Li, Yuntao Chen, Zhaoxiang Zhang
  - [Paper Reading](./Paper/2023/Wang_2023_Driving_into_the_Future.md), (场景预测, 自动驾驶, 大语言模型)
  - 对多视角的视频进行预测（结合当前 state 和 action，对场景预测），对不同动作的未来场景进行打分，最后选择分数高的场景对应的动作进行执行。

- [CoTV: Cooperative Control for Traffic Light Signals and Connected Autonomous Vehicles Using Deep Reinforcement Learning](https://ieeexplore.ieee.org/document/10144471)
  - Jiaying Guo, Long Cheng, Shen Wang
  - IEEE Transactions on Intelligent Transportation Systems ( Volume: 24, Issue: 10, October 2023)
  - [Paper Reading](./Paper/2023/Guo_2023_CoTV.md), (信号灯控制，CAV 速度控制，多智能体强化学习)
  - 利用强化学习同时控制 CAV（速度） 和 Traffic Light，为了解决扩展性，这里只控制距离 Traffic Light 最接近的 CAV。

- [LimSim: A Long-term Interactive Multi-scenario Traffic Simulator](https://ieeexplore.ieee.org/document/10422219)
  - Licheng Wen, Daocheng Fu, Song Mao, Pinlong Cai, Min Dou, Yikang Li, Yu Qiao
  - 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
  - [Paper Reading](./Paper/2023/Wen_2023_LimSim.md), (仿真平台，交通场景介绍)
  - 介绍了一款自动驾驶仿真器，包含多样性的场景和车辆之间的交互。**文章里面有对交通仿真器的总结，networkFiles 文件夹里面包含 SUMO 路网，从仿真器四个特色来介绍。**

### 2024

- [World Models for Autonomous Driving: An Initial Survey](https://arxiv.org/abs/2403.02622)
  - Yanchen Guan, Haicheng Liao, Zhenning Li, Guohui Zhang, Chengzhong Xu
  - [Paper Reading](./Paper/2024/Guan_2024_World_Models.md), (World Model, RSSM, PETA, AV)
  - World Model 在 Autonomous Driving 上的综述，主要介绍了两种 World Model 的结构，RSSM 和 JEPA，以及 World Model 在 AV 中的一些应用，（1）场景生成，（2）决策控制；

- [UniTSA: A Universal Reinforcement Learning Framework for V2X Traffic Signal Control](https://ieeexplore.ieee.org/abstract/document/10535743)
  - Maonan Wang, Xi Xiong, Yuheng Kan, Chengcheng Xu, Man-On Pun
  - [Paper Reading](./Paper/2024/Wang_2024_UniTSA.md)（[相关代码，Github-UniTSA](https://github.com/wmn7/Universal-Light)）
  - 利用数据增强的方式，使得 agent 可以见到训练集中不包含的路口情况，使得 agent 可以在没有见过的路口上获得更好的结果。

## License

Awesome V2X is released under the Apache 2.0 license.