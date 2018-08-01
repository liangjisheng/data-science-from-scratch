x <- rnorm(100);
colors <- ifelse(x>=0,"black","gray");
plot(x,type="h",lwd=3,col=colors);

colors <- ifelse(x>=0,"green","red");
plot(x,type="l",col=colors);

y <- dnorm(x);
plot(x,y,type="h",lwd=3,col="yellow");

# 画函数曲线
curve(sin,-3,3);
curve(dnorm,-3.5,3.5,main="Std. Normal Density");
f <- function(x) exp(-abs(x)) * sin(2*pi*x);
curve(f,-5,5,main="Dampened Sine Wave");

# 图形间暂停
# par(ask=TURE); par(ask=FALSE);
# par(lwd=2) # 改变默认线宽
# par("lty") # 查看默认线的类型
# par("bg") # 查看默认背景色

# 在一页中显示多个图形
par(mfrow=(c(2,2))); # 行优先填充
Quantile <- seq(from=0,to=1,length.out=30);
# dbeta计算beta分布的概率密度函数,后两个参数为形状参数
plot(Quantile,dbeta(Quantile,2,4),type="l",main="First");
plot(Quantile,dbeta(Quantile,4,2),type="l",main="Second");
plot(Quantile,dbeta(Quantile,1,1),type="l",main="Third");
plot(Quantile,dbeta(Quantile,0.5,0.5),type="l",main="Fourth");
# par(mfcol=c(3,3)); # 按列填充

# 打开另一个图形窗口 win.graph()
# dev.set(); # 切换活动窗口
win.graph(width=7.0,height=5.5);

