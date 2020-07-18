fifteen_A_star

文件：
A_star.py: A星算法运行脚本；
BFS.py: 广度优先算法运行脚本；
DFS_max_deepth.py: 有界深度优先算法运行脚本；
report_A_star_E.txt: 情况1，欧氏距离-A星算法运行结果输出文件
report_A_star_M.txt: 情况1，曼哈顿距离-A星算法运行结果输出文件
report_A_star_E_new.txt: 情况2，欧氏距离-A星算法运行结果输出文件
report_A_star_M_new.txt: 情况2，曼哈顿距离-A星算法运行结果输出文件
report_DFS_max_deepth.txt: 有界深度优先运行结果输出文件
report_BFS.txt: 广度优先算法运行结果输出文件


程序运行方法：
  所有程序均在Python3环境下运行；
  在项目文件夹中通过命令行输入：
      python A_star.py -m cal_E_distence > report_A_star_E.txt
  即可通过欧氏距离的计算方法计算启发函数，并且输出结果保存在report_A_star_E.txt文件中。
      python A_star.py -m cal_M_distence > report_A_star_M.txt
  即可通过曼哈顿距离的计算方法计算启发函数，并且输出结果保存在report_A_star_M.txt文件中。
      python DFS_max_deepth.py > report_DFS_max_deepth.txt
  即可通过有界深度优先算法，并且输出结果保存在report_DFS_max_deepth.txt文件中。
      python BFS.py > report_BFS.txt
  即可通过广度优先算法，并且输出结果保存在report_BFS.txt文件中。

  在.py 文件中修改初始状态4*4的列表，即可看到不同情况下的输出结果。


参考：https://blog.csdn.net/t949500898/article/details/107397693
