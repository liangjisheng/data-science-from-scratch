f <- function(x) 3*x^4-2*x^3+3*x^2+4*x+5;
optimize(f,lower=-20,upper=20); # 求-20到20之间f(x)的最小值

# f <- function(v) { a <- v[1];
# 	b <- v[2];
# 	sum(abs(z-((x+a)^b)));
# }
# optim(c(1,1),f); # 最小化或者最大化多参数函数
fibmat <- matrix(c(0,1,1,1),2,2);
eigen(fibmat); # 求特征值和特征向量

n <- 3;
x <- rnorm(1000);
d <- dist(x); # computer distance between observations
hc <- hclust(d);	 # 根据距离把观测值形成一个层次聚类图,又称谱系树
clust <- cutree(hc,k=n); # 从谱系树中抽取出聚类

means <- sample(c(-3,0,3),99,replace=TRUE);
x <- rnorm(99,mean=means);
tapply(x,factor(means),mean);

d <- dist(x); # 计算所有点之间的距离
hc <- hclust(d);
clust <- cutree(hc,k=3);
head(clust,20);
tapply(x,clust,mean);
plot(x~ factor(means),main="Original Clusters",xlab="Cluster Mean");
plot(x~ factor(clust),main="Identified Clusters",xlab="Cluster Number");

data(pima,package="faraway");
b <- factor(pima$test);
m <- glm(b~diastolic+bmi,family=binomial,data=pima);
summary(m);
m.red <- glm(b~bmi,family=binomial,data=pima);
newdata <- data.frame(bmi=32.0);
predict(m.red,type="response",newdata=newdata);
newdata <- data.frame(bmi=quantile(pima$bmi,0.90));
predict(m.red,type="response",newdata=newdata);

