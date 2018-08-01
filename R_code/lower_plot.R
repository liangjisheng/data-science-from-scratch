plot(-4:4,-4:4,type="p",col="blue");
# 绘制点，连接点
points(x=c(3,-2,-1,3,2),y=c(1,2,-2,2,3),col="red");
lines(x=c(3,-2,-1,3,2),y=c(1,2,-2,2,3),col="black");

# 绘制直线
abline(h=0);
abline(v=0);
abline(a=1,b=1); # 绘制y=x+1直线
abline(lm(mtcars$mpg~mtcars$qsec),col="red");

# 绘制线段
segments(x0=2,y0=-4.5,x1=4,y1=-2,col="red",lty="dotted");

# 绘制箭头，设置箭头的长度，角度，样式
arrows(x0=-4,y0=4,x1=-2,y1=0,length=0.15,angle=30,code=3);

# 绘制网格 将x轴分成3等分，y轴分成5等分
grid(nx=3,ny=5,col="lightgray",lty="dotted");

polygon(x,y=NULL,density=NULL,angle=45,
	border=NULL,col=NA,lty=par("lty"),fillOddEven=FALSE);

# 绘制多边形和矩形
plot(-4:4,-4:4,type="p",col="blue");
polygon(x=c(3,-2,-1,3,2),y=c(1,2,-2,2,3),col="red"); # 绘制多边形
rect(xleft=c(-4,0),ybottom=c(2,-4),xright=c(-2,2),ytop=c(4,2),
	col=c("blue","yellow")); # 绘制两个矩形，并填充颜色

# 主标题和子标题，字体相对大小为0.75
plot(mtcars$wt,mtcars$mpg,main="",sub="",xlab="",ylab="");
title(main="My Title",col.main="red",sub="My Sub-title",
	col.sub="blue",xlab="My X label",ylab="My Y label",
	col.lab="green",cex.lab=0.75);
# 使用text()/mtext()函数为绘图区域/边缘区域添加文本注释
plot(x=mtcars$wt,y=mtcars$mpg,main="Milage vs. Car Weight",
	xlab="Weight",ylab="Mileage",pch=18,col="blue");
text(x=mtcars$wt,y=mtcars$mpg,labels=row.names(mtcars),
	cex=0.6,pos=4,col="red");
mtext("Added by mtext()",side=2,line=2,col="blue");
