x <- rnorm(100);
plot(x);
y <- dnorm(x);
plot(x,y);

plot(cars,main="cars: Speed vs. Stopping Distance(1920)",
	xlab="Speed(MPH)",ylab="Stopping Distance(ft)",
	type="n");
grid();
points(cars);

# type=n,在不显示数据的情况下初始化图形框架
plot(x,y,type="n");
grid(); # 绘制网格
points(x,y);

with(iris,plot(Petal.Length,Petal.Width));
# 分类
with(iris,plot(Petal.Length,Petal.Width,pch=as.integer(Species)));
# 添加图例
legend(1.5,2.4,c("setosa","versicolor","virginica"),pch=1:3);


f <- factor(iris$Species);
with(iris,plot(Petal.Length,Petal.Width,pch=as.integer(Species)));
legend(1.5,2.4,as.character(levels(f)),pch=1:length(levels(f)));

legend(0.5,9.5,c("Estimate","Lower conf lim","Upper conf lim"),
	lty=c("solid","dashed","dotted"));

install.packages("faraway");
library(faraway);
data(strongx); # 导入数据，使用R软件包faraway中的数据集strongx来建模
m <- lm(crossx~energy,data=strongx); # lm 最佳线性回归模型
plot(crossx~energy,data=strongx);
abline(m);

# 绘制多组散点图
plot(kai);
head(iris);
plot(iris[,1:4]);

#创建每个因子水平的散点图
data(Cars93,package="MASS");
coplot(Horsepower~MPG.city | Origin,data=Cars93);

# 创建条形图
heights <- tapply(airquality$Temp,airquality$Month,mean);
barplot(heights,main="Mean,Temp. by Month",
	names.arg=c("May","Jun","Jul","Aug","Sep"),
	ylab="Temp(deg.F)");

install.packages("gplots");
library(gplots);
attach(airquality);
heights <- tapply(Temp,Month,mean);
lower <- tapply(Temp,Month,function(v) t.test(v)$conf.int[1]);
upper <- tapply(Temp,Month,function(v) t.test(v)$conf.int[2]);
barplot2(heights,plot.ci=TRUE,ci.l=lower,ci.u=upper,
	ylim=c(50,90),xpd=FALSE,main="Mean Temp. By Month",
	names.arg=c("May","Jun","Jul","Aug","Sep"),
	ylab="Temp(deg.F)");

# 给条形图上颜色
barplot(c(3,4,5),col=c("red","white","blue"));
# 转换条形快的等级为高度
rel.hts <- rank(heights)/length(heights);
grays <- gray(1-rel.hts);
barplot(heights,col=grays,
	ylim=c(50,90),xpd=FALSE,main="Mean Temp. By Month",
	names.arg=c("May","Jun","Jul","Aug","Sep"),
	ylab="Temp(deg.F)");

library(quantmod);
setSymbolLookup(WK=list(name='000002.sz',src='yahoo'));
getSymbols("WK");
chartSeries(WK);

# 贵州茅台
setSymbolLookup(GZMT=list(name='600519.ss',src='yahoo'))
getSymbols("GZMT")
chartSeries(GZMT);
