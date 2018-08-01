plot(pressure);
plot(pressure,type="l");
# lty="solid" or lty=1 default 控制线的类型
# lty="dashed" or lty=2
# lty="dotted" or lty=3
# lty="dotdash" or lty=4
# lty="longdash" or lty=5
# lty="twodash", or lty=6
# lty="blank" or lty=0 (抑制绘图)
x <- pressure$temperature;
y <- pressure$pressure;
plot(x,y,type="l",lty="dashed",col="red");
plot(x,y,type="l",lty="solid",col="red");
plot(x,y,type="l",lty="dotted",col="red");
plot(x,y,type="l",lty="dotdash",col="red");
plot(x,y,type="l",lty="longdash",col="red");
plot(x,y,type="l",lty="twodash",col="red");
plot(x,y,type="l",lty="blank");

plot(x,y,type="l",col="red");
lines(x,y+100,type="l",lty="dashed",col="green");
lines(x,y+200,type="l",lty="dotted",col="blue");

x1 <- runif(30);
x2 <- rnorm(30);
y1 <- dunif(x1);
y2 <- dnorm(x2);
xlim <- range(c(x1,x2));
ylim <- range(c(y1,y2));
plot(x1,y1,type="l",xlim=xlim,ylim=ylim);
lines(x2,y2,type="l");

x <- rnorm(100);
m <- mean(x);
plot(x);
abline(h=m); # 添加水平线
# abline(h=0);
stdevs <- m+c(-2,-1,1,2)*sd(x);
abline(h=stdevs,lty="dotted"); # 上下两个标准差的地方绘制虚线

# 创建箱线图
boxplot(x);

data(UScereal,package="MASS");
boxplot(sugars~shelf,data=UScereal,
	main="Sugar Content by Shelf",
	xlab="Shelf",ylab="Sugar(grams per portion)");