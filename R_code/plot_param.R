hist(mtcars$mpg,col.lab="red"); # 临时性参数

par(); # 查看当前绘图参数设置
opar <- par(); # 保存当前设置
par(col.lab="red"); # 设置坐标轴颜色为红色
hist(mtcars$mpg,col.lab="red");
par(opar); # 恢复绘图参数的原始设置
# 绘图时我们可以用各类符号显示数据，pch是plotting character 的缩写。
# pch缺省下设定数据显示为点状。pch 符号可以使用0 : 25来表示26 个标识
#（参看图pch 符号）,如pch=23设定数据点显示形状为菱形；
# 当pch=0时不显示任何符号；当然我们也可以任意指定如#;%; ¤; j;+;?; :; o等符号。
# 值得注意的是，21 : 25这几个符号可以使用bg="颜色" 参数进行不同的颜色填充。
# 颜色参数col则可以用于设置1:25所表示符号的颜色。

# h=i 绘制水平线，lty=i 线的形状, lwd=i 线的宽度
plot(0:6,type='n');
for(i in c(0:6)) { abline(h=i,lty=i,lwd=i) }

# setup font 1=普通，2=粗体，3=斜体，4=粗斜体，5=符号字体
# font.axis 坐标轴刻度字体样式     font.lab 坐标轴标题字体
# font.main/font.sub 主标题/子标题字体
# family
plot(1:10,1:10,type="n");
windowsFonts(A=windowsFont("Arial Black"),
	B=windowsFont("Bookman Old Style"),
	C=windowsFont("Comic Sans MS"),
	D=windowsFont("Symbol"));
text(3,3,"Hello World Default");
text(4,4,family="A","Hello World from Arial Black");
text(5,5,family="B","Hello World from Bookman Old Style");
text(6,6,family="C","Hello World from Comic Sans MS");
text(7,7,family="D", "Hello World from Symbol");