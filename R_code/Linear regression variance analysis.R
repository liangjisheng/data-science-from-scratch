# 一元线性回归
x <- 1:100;
y <- 3*x+5+rnorm(100);
m <- lm(y~x); # 线性回归模型，使用最小二乘,回归模型保存在m中
# 将x,y合并为一个数据框
dfrm <- data.frame(x,y);
lm(y~x,data=dfrm); # lm()会从数据框而不是工作空间中访问用于回归的变量

# 多元线性回归
# lm(y~u+v+w) # 预测变量由加号分开
# lm(y~u+v+w,data=dfrm);

# 得到回归统计量
anova(m); 		# 方差分析表
coefficients(m); 	# 模型系数
coef(m); 		# 与上面的作用相同
confint(m); 	# 给出回归系数的置信区间
deviance(m); 	# 给出残差平方和
effects(m); 	# 正交影响向量
fitted(m); 		# 拟合y值的向量
residuals(m); 	# 模型残差
resid(m); 		# 与上面的作用相同
summary(m); 	# 给出重要统计量
vcov(m); 		# 主要参数的方差，协方差矩阵

#运行无截距的线性回归模型 lm(y~x+0) 回归方程y=beta*x+偏差

# full.model <- lm(y ~ x1+x2+x3+x4)	后项逐步回归，移除无意义的变量
# reduced.model <- step(full.model,direction="backward") 

# min.model <- lm(y~1) 开始有很少的变量，逐步添加变量改进模型，trace=0抑制step的大量输出
# fwd.model <- step(min.model,direction="forward",scope=(~x1+x2+x3+x4),trace=0)

# 对数据子集的回归 lm(y~x,subset=1:100) 使用x的前100个数据
# lm(y~x,subset=1:floor(length(x)/2)) 使用x的前半段
# 在回归公式中使用表达式
# lm(y~I(u+v))  y=b0+b1(u+v)+误差项
# lm(y~u+I(v^2))

# 多项式回归 lm(y~poly(x,3),raw=TRUE); y=b0+b1*x+b2*x^2+b3*x^3+误差项
# 转换数据的回归 lm(log(y)~x); lm(sqrt(y) ~ month); 
# lm(y~sqrt(x)); lm(log(y)~log(x))

# 寻找最佳幂变换
library(MASS);
x <- 10:100;
eps <- rnorm(length(x),sd=5);
y <- (x+eps)^(-1/1.5);
m <- lm(y ~ x);
summary(m);
plot(m);
plot(m,which=1); # 绘制残差和拟合值的图
bc <- boxcox(m); # 绘制lambda的值和相应结果模型的对数似然值
which.max(bc$y); # 得到y的最大对数似然估计
lambda <- bc$x[which.max(bc$y)]; # 给出lambda的位置
# 对y应用幂变换，拟合修正的模型，给出更理想的R^2的值
z <- y^lambda;
m2 <- lm(z~x);
summary(m2);
# m2 <- lm(I(y^lambda~x)); 等价的单行代码
confint(m); # 回归系数的置信区间 confint(m,level=0.99)

# 诊断线性回归
install.packages("car");
library(car);
outlier.test(m);

# 识别有影响的观察值,就是离群值
influence.measures(m);

# 残差自相关检验
install.packages("lmtest");
library(lmtest);
dwtest(m); # 默认执行单边检验 p值大于0.05表明不存在显著的自相关
dwtest(m,alternative="two.sided"); # 执行双边检验

# 预测新值
preds <- data.frame(x=c(110:120));
predict(m,newdata=preds);

# 建立预测区间
predict(m,newdata=preds,interval="prediction");

# 单因素方差分析 
# oneway.test(x~f); m <- aov(x~f); summary(m);
# 找到组间均值的不同 TukeyHSD(m); plot(TukeyHSD(m));

# 创建交互关系图 interaction.plot(pred1,pred2,resp);
library(faraway);
data(rats);
interaction.plot(rats$poison,rats$treat,rats$time);

# 执行稳健方差分析 kruskal.test(x~f);

# 运用方差比较模型 anova(m1,m2);
