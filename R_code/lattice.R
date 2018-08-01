attach(mtcars); # 将mtcars的每一列作为一个变量放到工作空间中
layout(mat=matrix(c(1,1,2,3),2,2,byrow=TRUE),widths=c(3,1),
	heights=c(1,2));
layout.show(3);
hist(wt);
hist(mpg);
hist(disp);

# par() fig指定各个图形的绘制位置 new指定是否将图形绘制到已有图形
# 在散点图上添加盒图
par(fig=c(0,0.8,0,0.8),new=FALSE);
plot(mtcars$wt,mtcars$mpg,xlab="Miles Per Gallon",ylab="Car Weight");
par(fig=c(0,0.8,0.55,1),new=TRUE);
boxplot(mtcars$wt,horizontal=TRUE,axes=FALSE);
par(fig=c(0.65,1,0,0.8),new=TRUE);
boxplot(mtcars$mpg,axes=FALSE);
mtext("Enhanced Scatterplot",side=3,outer=TRUE,line=-3);

# histogram 	直方图
# densityplot	核密度图
# qqmath		理论分位数图
# qq			双样本分位数图
# stripplot		带形图
# bwplot		盒图
# dotplot		克利夫兰点图
# barchart		条形图
# xyplot		散点图
# splom		散点图阵列
# contourplot	表面等高线图
# levelplot		表面为色彩图
# wireframe		三维表面透视图
# cloud		三维散点图
# parallel		平行坐标图

# 高级格函数(Lattice Function)
library(lattice);
attach(mtcars);
gear.f <- factor(gear,levels=c(3,4,5));
lables <- c("3gears","4gears","5gears");
# 按gear.f绘制mpg的多面板盒图
bwplot(x=~mpg|gear.f,main="Boxplot by Gears",xlab="Miles per Gallon",
	layout=c(3,1));
# 按gear.f绘制mpg~wt的多面板散点图
xyplot(x=mpg~wt|gear.f,main="Scatterplots by Gears",
	xlab="Miles per Gallon",layout=c(3,1));