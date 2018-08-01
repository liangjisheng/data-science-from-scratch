# 均值的检验
x <- rnorm(100,mean=100,sd=15);
t.test(x,mu=95);# 检验均值是否为95
t.test(x,mu=100); # 检验均值是否为100
t.test(x); # x的均值95%的置信区间
t.test(x,conf.level=0.99); # x的均值99%的置信区间

# 中位数的检验
x <- runif(100);
wilcox.test(x,conf.int=TRUE); # x的中位数95%的置信区间
wilcox.test(x,conf.int=TRUE,conf.level=0.99); # x的中位数99%的置信区间

# 检验样本比例 prop.test(x,n,p) n为样本次数，x为成功次数，p为检验的比例
prop.test(11,20,0.5); # 默认检验p!=0.05
prop.test(11,20,0.5,alternative="greate"); #检验p大于0.5
# 样本比例置信区间 prop.test(x,n) n为样本次数，x为成功次数
prop.test(6,9);
prop.test(6,9,conf.level=0.99); # 99%的置信区间

# 检验一个样本数据是否来自正态分布总体
x <- runif(100);
shapiro.test(x);
x <- rnorm(100);
shapiro.test(x);
# nortest软件包专门用于正态检验，包括下列正态检验方法
# Anderson-Darling 检验(ad.test)
# Carmer-Von Mises 检验(cvm.test)
# Lilliefors 检验(lillie.test)
# Pearson 卡方检验正态性符合假设 (person.test)
# Shapiro-Francia 检验 (sf.test)

# 游程检验 数据只有两个取值的序列，例如 是和否，0和1，真和假，或者其他具有两值的数据，
# 想知道这个序列是随机的吗？软件包tseries包含函数runs.test 用于检验一个序列是否随机
# 这个序列需要是一个有两个水平的因子
install.packages("tseries");
library(tseries);
s <- sample(c(0,1),100,replace=T);
runs.test(as.factor(s));
s <- c(1,1,1,0,0,0,1,1,1);
runs.test(as.factor(s));

# 比较两个样本的均值 t.test(x,y) 默认情况下，x,y是不配对数据的，如果观测值是配对的
# 即每一个xi与yi配对，则需要指定参数paired=TRUE t.test(x,y,paired=TRUE)
# 如果x,y方差相同，指定参数var.equal=TRUE以获得较低的保守性检验，更有效的检验

# 不做出关于总体分布的假设是，就进入了非参数统计的世界
# 两个总体的样本，不知道总体的分布，但知道它们有类似的形状，想知道一个总体比另外一个总体是否偏左或偏右
# 使用wilcox.text(x,y),若配对设置参数paired=TURE,给出了两个样本的中央位置是否有显著的不同
# 或者相同，它们的相对频率是否相同

# 检验相关系数的显著性cor.test(x,y),默认检验正态分布的总体，若不是正态分布总体，
# 则使用Spearman法，cor.test(x,y,method="Spearman")

# 检验组的等比例 prop.test() ns <- c(ns1,ns2,...,nsn); nt <- c(nt1,nt2,...,ntn);
# ns给出了每一组的成功的次数,nt给出了相应组的大小
successes <- c(14,10);
trials <- c(38,40);
prop.test(successes,trials);

# 检验两个样本是否来自相同的分布 Kolmogorov-Smirnov比较两个样本并检验它们是否来自于相同的分布
# ks.test(x,y); 它是非参数检验，不需要做任何关于数据分布的假设，适用于所有的分布