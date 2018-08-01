# 添加坐标轴
x <- c(1:10); y <- x; z <- 10/x;
par(mar=c(5,4,4,8)+0.1);
# 只绘制x轴，抑制绘制y轴
plot(x,y,type="b",pch=21,col="red",yaxt="n",lty=3,xlab="",ylab="");
lines(x,z,type="b",pch=22,col="blue",lty=2);
# 左侧添加坐标轴，设置刻度标签样式
axis(side=2,at=x,labels=x,col.axis="red",las=2);
# 右侧添加坐标轴，设置标签及刻度线的长度
axis(side=4,at=z,labels=round(z,digits=2),col.axis="blue",
	cex.axis=0.7,tck=-0.1);
mtext("y=1/x",side=4,line=3,cex.lab=1,las=2,col="blue");
title("An Example of Creative Axes",xlab="X values",
	ylab="Y=X");
# 添加图例，并设置格式
counts <- table(mtcars$vs,mtcars$gear);
barplot(counts,main="Car Distribution by Gears and VS",
	xlab="Number of Gears",col=c("darkblue","red"),
	beside=TRUE);
legend(x=7.5,y=12,legend=c("L-A","L-B"),pch=15,
	col=c("blue","red"),cex=0.8,pt.cex=1,box.lty="dashed");