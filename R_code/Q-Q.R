# 创建正太Q-Q图，判断数据是否服从正态分布
# qqnorm(x) 创建基本Q-Q图，qqline(x)添加对角线
data(Cars93,package="MASS");
qqnorm(Cars93$Price,main="Q-Q Plot: Price");
qqline(Cars93$Price); # 尾部的点在对角线上方，表示大体向左偏的趋势,可以通过对数变换纠正

qqnorm(log(Cars93$Price),main="Q-Q Plot: Price");
qqline(log(Cars93$Price));
# 大部分点与对角线保持很近距离，表明log(Price)是近似正态的

# 其他Q-Q图
y <- rt(50,5); # 50个自由度为5的学生t分布
plot(qt(ppoints(y),5),sort(y)); # qt(y) 学生t分布的分位数函数
abline(a=0,b=1);

Rate <- 1/10;
y <- rexp(50,rate=Rate);
plot(qexp(ppoints(y),rate=Rate),sort(y),
	main="Q-Q Plot",xlab="Theoretical Quantiles",
	ylab="Sample,Quantiles");
abline(a=0,b=1);

plot(-4:4, -4:4, type = "n")  # setting up coord. system
points(rnorm(200), rnorm(200), col = "red")