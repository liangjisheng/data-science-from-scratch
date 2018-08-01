x <- sample(10); # 1:10的随机样本,不重复抽取
y <- sample(10,replace=T); # 重复抽取
# 产生指定分布的随机样本
sample(c(-1,0,1),size=20,prob=c(1/4,1/2,1/4),replace=T);
set.seed(12345); # 初始化随机种子
sample(10);
sample(10);
sample(10);
set.seed(10);
sample(10);
sample(10);
sample(10);

# 模拟赌博,掷硬币，正面1，反面-1，初始金额w0=0,w(t)=w(t-1)+r(t),t为次数
set.seed(13579);
r=sample(c(-1,1),size=100,replace=T,prob=c(1/2,1/2));
r=c(0,r); # 加入初始金额
w=cumsum(r); # 累积求和
w=as.ts(w); # 转换成时间序列
plot(w,main="随机步行");
abline(h=0);

# 正态分布
x=seq(-4,4,0.1); # [-4,4]，步长为0.1
plot(x,dnorm(x),type="l",main="N(0,1),密度"); # dnorm() 标准正态密度函数
pnorm(1.96); # # pnorm() 标准正态分布函数
q=c(0.025,0.05,0.5,0.95,0.975);
qnorm(q); # 标准正态分布的分位数

hist(rnorm(1000,mean=10,sd=2),main="N(10,4)");

# t分布
1-pt(2.3,5); # 自由度为5的t分布函数,t>2.3的概率
pt(2.3,5,lower.tail=F); # 右尾概率，与上面相同

# 二项分布
x=seq(0:20);
pmf=dbinom(x,size=20,prob=1/4);
plot(x,pmf,type="h",main="Binomial(20,1/4)分布");
1-pbinom(8,size=20,prob=1/4); # x>8  的概率
q=seq(0.1,0.9,0.1);
qbinom(q,size=20,prob=1/4);

# 中心极限定理
set.seed(12345);
u=runif(10000);
summary(u);
var(u);
hist(u,main="U(0,1)");

u=matrix(u,nc=10); # 将u转换为1000*10的矩阵
m=apply(u,1,mean); # 对u的每一行求均值,1只矩阵的第一维数 行
summary(m);
var(m);
hist(m,main="样本平均(n=10)的抽样分布");
dm=dnorm(m,mean=mean(m),sd=sd(m));