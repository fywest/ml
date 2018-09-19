
# coding: utf-8

# <img style="float: right; width:100px;" src="https://static.shiyanlou.com/img/shiyanlou_logo.svg"><h1 style="color:brown;">楼 + 机器学习实战</h1></img>

# # 监督学习介绍

# ### 实验介绍
# 
# 监督学习，如果你是第一次听说这个名词，那么可能完全不清楚是什么含义。不用担心，在本次实验中，你将全面了解监督学习，并在接下来的实验章节中，学习使用监督学习完成数据预测。

# ### 实验知识点
# 
# - 机器学习综述
# - 机器学习算法
# - 监督学习介绍
# - 分类和回归

# ### 实验环境
# 
# - Python 3.6

# ### 目录索引
# 
# - <a href="#机器学习综述">机器学习综述</a>
# - <a href="#监督学习介绍">监督学习介绍</a>
# - <a href="#实验总结">实验总结</a>

# ---

# ## 机器学习综述

# 本次《楼+ 之机器学习实战》课程中，我们一共包含了 6 周的内容，标题如下：
# 
# - 第 1 周：监督学习：回归
# - 第 2 周：监督学习：分类
# - 第 3 周：非监督学习：聚类
# - 第 4 周：强化学习
# - 第 5 周：深度学习基础
# - 第 6 周：深度学习

# 对于这六周的内容而言，前 4 周属于「传统机器学习」的内容。这里使用「传统机器学习」一词概述不太准确，所以我们使用「统计机器学习」这个更学术、更准确的词语。
# 
# 统计机器学习，英文是：Statistical Machine Learning，它是概率论、统计学、计算理论、最优化方法、以及计算机科学组成的交叉学科，其主要的研究对象是如何从经验中学习并改善具体算法的性能。
# 
# 目前，我们通常所说的「机器学习」往往就是指「统计机器学习」。它大致分为四个类别：
# - 监督学习（英文：Supervised learning）
# - 非监督学习（英文：Unsupervised learning）
# - 半监督学习（英文：Semi-supervised learning）
# - 强化学习（英文：Reinforcement learning）

# 在《楼+ 之机器学习实战》课程的介绍内容中，我们引入了图 1 来介绍机器学习、深度学习和人工智能的关系。如果要将「统计机器学习」纳入进去，它应该可以被放到 `1980's` 到 `2010's` 之间的部分。当然，这并不是说 2010 年之后，统计机器学习就不发展了。相反，像强化学习、非监督学习等领域还需要人类不懈地探索和发现。

# <img width='800px' style="border:2px dashed #000000;" src="https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531365795642.png"></img>
# <div style="color: #888; font-size: 10px; text-align: right;">[©️ 图片来源](https://www.nvidia.com/page/home.html)</div>

# ## 监督学习介绍

# 上面，我们介绍了机器学习通常被分为四大类别。而这四大类别又被细分为数十种不同的机器学习算法 / 方法（详见表 1）。

# <div style="color: #999; font-size: 12px; text-align: center;">表 1：机器学习算法不完全分类</div>
# <table>
#   <tr>
#     <th>分类</th>
#     <th>具体方法</th>
#   </tr>
#   <tr>
#     <td rowspan="8">监督学习</td>
#     <td>人工神经网络</td>
#   </tr>
#   <tr>
#     <td>贝叶斯网络</td>
#   </tr>
#   <tr>
#     <td>支持向量机</td>
#   </tr>
#   <tr>
#     <td>随机森林</td>
#   </tr>
#   <tr>
#     <td>逻辑回归</td>
#   </tr>
#   <tr>
#     <td>K近邻</td>
#   </tr>
#   <tr>
#     <td>决策树</td>
#   </tr>
#   <tr>
#     <td>隐马尔可夫模型</td>
#   </tr>
#   <tr>
#     <td rowspan="3">非监督学习</td>
#     <td>人工神经网络</td>
#   </tr>
#   <tr>
#     <td>关联规则学习</td>
#   </tr>
#   <tr>
#     <td>分层聚类</td>
#   </tr>
#   <tr>
#     <td rowspan="4">半监督学习</td>
#     <td>生成模型</td>
#   </tr>
#   <tr>
#     <td>低密度分离</td>
#   </tr>
#   <tr>
#     <td>联合训练</td>
#   </tr>
#   <tr>
#     <td>图方法</td>
#   </tr>
#   <tr>
#     <td rowspan="3">强化学习</td>
#     <td>时间差分学习</td>
#   </tr>
#   <tr>
#     <td>Q学习</td>
#   </tr>
#   <tr>
#     <td>SARSA</td>
#   </tr>
# </table>

# 那么，问题来了：**监督学习究竟是什么意思呢？其细分的各种方法又有哪些特点呢？**

# ### 监督学习定义

# 关于监督学习的定义，这里引用著名机器学习专家 **Mehryar Mohri** 在其专著 **Foundations of Machine Learning** 中的叙述：
# 
# >Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples.

# 这句话翻译成中文的大意是：
# 
# > 监督学习是基于示例输入-输出数据对，在输入和输出数据之间建立数学函数的机器学习任务，而该数学函数来源于对有标签训练数据集的学习过程。

# 解析一下这句话中的几个关键词。`示例输入-输出数据对`其实就是`训练数据集`，而`输入`指的是训练数据集中的`特征变量`，`输出`则是`标签`。而建立`数学函数`，实际就是训练`机器学习预测模型`。这句话，其实就是一个典型的机器学习过程。而监督学习的关键在于，这里提供的**训练数据集有标签**。

# ### 监督学习示例

# **为了更好地理解上面关于监督学习的定义，下面举一个判断花朵种类的例子。**
# 
# 如图 2 所示，训练数据集给出了 3 种不同花朵的花瓣长度特征（训练集特征），我们已经知道这 3 朵花的种类 A, B, C（标签）。那么，对于一朵未知种类的花，就可以根据它的花瓣长度（测试样本特征）来判断它所属种类（测试样本标签）。下图中，未知花朵判断成 B 类肯定更合适一些。

# <img width='800px' src="https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531365795294.png"></img>

# 综上，**监督学习中的「监督」就体现在训练集具有「标签」**。就像上图中，我们给出了已知种类的花，对于未知种类的花就根据特征去比较就可以了。

# ### 监督学习中的分类与回归

# 通过上面的小例子，你应该对「监督学习」有一定印象了。而类似于上面这种识别类别的问题，我们一般称之为监督学习的分类问题。分类其实是一种最常见的问题类型，例如：动物的种类判断、植物的种类判断、各类物品的种类判断等。

# 除了分类问题，监督学习中还有十分重要的一类，那就是回归问题，这也就是本周需要学习的内容。首先，回归问题和分类问题一样，训练数据都包含标签，这也是监督学习的特点。而不同之处在于，分类问题预测的是类别，回归问题预测的是连续值。
# 
# 例如，回归问题往往解决：
# 
# - 股票价格预测
# - 房价预测
# - 洪水水位线
# 
# 上面列举的问题，我们需要预测的目标都不是类别，而是实数连续值。

# <img width='800px' src="https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531365794755.png"></img>

# 那么，机器学习中常见的回归问题解决方法有：
# 
# - 线性回归方法
# - 多项式回归方法
# - 岭回归以及 LASSO 回归方法
# 
# 而解决分类问题的方法有：
# 
# - 支持向量机
# - K-近邻算法
# - 决策树算法
# - 随机森林算法
# - 朴素贝叶斯算法
# - ……

# 上面提到的这些方法，在接下来的课程中都会学习。我们会从算法原理入手，通过 Python 建立预测模型，并对实际数据集进行预测分析。

# ## 实验总结

# 本次实验中，我们重新梳理了机器学习的概念以及细分类别，并了解了常见的机器学习算法。同时，实验针对监督学习进行了介绍，这会对后续两周的学习提供帮助。本次实验包含的知识点有：
# 
# - 机器学习综述
# - 机器学习算法
# - 监督学习介绍
# - 分类和回归

# **拓展阅读：**
# 
# - [机器学习-维基百科](https://zh.wikipedia.org/wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0)

# ---

# <div style="color: #999;font-size: 12px;">©️ 本课程内容，由作者授权实验楼发布，未经允许，禁止转载、下载及非法传播。</div>