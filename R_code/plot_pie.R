set.seed(1);
x <- sample(c(1:50),10);
set.seed(2);
y <- sample(c(1:50),10);
y1 <- sort(y);
xt <- ts(x); # 时间序列对象
xy <- cbind(x,y);
f <- as.factor(c(rep('a',3),rep('b',5),rep('c',2)));

par(mfrow=c(3,2));
plot(x);	# 散点图
plot(xt);	# 折线图
plot(f); # 绘制f的条形图
plot(x,y);	# 绘制y对x的散点图
plot(xy);# 绘制y对x的散点图
plot(f,y); # f为一个因子，y为向量，绘制y在f的各水平下的盒图

x <- c(1:5);
y <- x;
par(pch=22,col="red");par(mfrow=c(2,4));
opts <- c("p","l","o","b","c","s","S","h");
for(i in 1:length(opts)) {
	plot(x,y,type="n",main=paste("type=",opts[i]))
	lines(x,y,type=opts[i]);
}

sal_num <- c(45,21,50,43,90,32);
click_num1 <- sal_num+5;
click_num2 <- sal_num+10;
plot(sal_num,col="black",type="o",ylim=c(0,105),axes=TRUE);
lines(click_num1,col="red",type="o",pch=22,lty=2);
lines(click_num2,col="blue",type="o",pch=22,lty=2);

boxplot(x=c(cars$speed,35));
boxplot(x=c(cars$speed,35),range=3); # range 参数的值改变胡须的延伸位置

# pie 饼图
slices <- c(10,12,4,16,8);
lbls <- c("US","UK","Australia","Germany","France");
pie(slices,labels=lbls,main="Pie Chart of Countries");

slices <- c(10,12,4,16,8);
lbls <- c("US","UK","Australia","Germany","France");
pct <- round(slices/sum(slices)*100); # 所占%比
lbls <- paste(paste(lbls,pct),"%",sep=""); # add % to labels
pie(slices,labels=lbls,col=rainbow(length(lbls)),
	main="Pie Chart of Countries");