# hist直方图
data(Cars93,package="MASS");
hist(Cars93$MPG.city);
# 第二个参数20表示直方图的个数
hist(Cars93$MPG.city,20,main="City MPG (1993)",xlab="MPG");

x <- Cars93$MPG.city;
hist(x,30,prob=T); # 使用概率 using a probability scale
lines(density(x)); # Graph the approximate density 绘制近似密度

samp <- rgamma(500,2,2);
hist(samp,20,prob=T);
lines(density(samp));

x <- rnorm(50);
y <- dnorm(x);
plot(x,y);
plot(x,y,type="l",col="red");
abline(v=mean(x),col="blue");
abline(v=c(-2,-1,1,2)*sd(x),lty="dotted",col="yellow");
# table(x) 对事件进行计数，type="h" 表示绘制直方图
plot(table(x),type="h",lwd=5,ylab="Freq");
plot(table(x)/length(x),type="h",lwd=5,ylab="Freq");