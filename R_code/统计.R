x <- rnorm(100);
mean(x>0); # 求x>0在生成的随机数里所占的频率
mean(abs(x-mean(x))>2*sd(x));# 偏离平均值超过两个标准差的观测值所占的比例
mean(diff(x)>0); # 时间序列中，观测值大于前一个观测值所占的比例
sum(x>0); # x中大于0的个数
sum(x>mean(x));
sum(abs(x-mean(x))>2*sd(x)); #偏离平均值超过两个标准差的观测值的个数
sum(diff(x)>0);

f <- factor(c("li","li","shu","shu","li","li","liang","liang"));
f1 <- factor(c("a","a","a","b","b","b","b","c"));
table(f); # 产生一个因子的计数
table(f1);
table(f,f1); # 产生列联表，计算相应的组合发生了多少次
summary(table(f,f1));# 对列联表的数据进行卡方检验，也可用chisq.test()

vec <- runif(1000); # 1000个0-1之间均匀分布的随机数
quantile(vec,0.05); # vec中0.05分位数
quantile(vec,c(.05,.95));
quantile(vec); # 四分位数
mean(vec<0.01); # vec中小于0.01的数所占的比例
sum(vec<0.01);
mean(vec<0.06)-mean(vec<0.01);

x <- rnorm(100,5,1); # 100个均值为5，标准差为1的正太分布数据
scale(x); # 计算所有数据元素的相应的z分数(又称规范化数据)
