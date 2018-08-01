# 对象类zoo和xts表达时间序列
library(zoo);
library(xts);
# as.zoo(xts); as.xts(ts);
prices <- c(132.45,130.85,130.00,129.55,130.85);
dates <- as.Date(c("2010-01-04","2010-01-05","2010-01-06",
		"2010-01-07","2010-01-08"));
ibm.daily <- zoo(prices,dates);
print(ibm.daily);

prices <- c(131.18,131.20,131.17,131.15,131.17);
# 9.5表示早上9:30,之后第一个1秒的时间是9.500278，
seconds <- c(9.5,9.500278,9.500556,9.500833,9.501111);
ibm.sec <- zoo(prices,seconds);
print(ibm.sec);

# 提取数据
coredata(ibm.daily);
# 提取日期序列
index(ibm.daily);

vignette("zoo"); # 查看zoo包的相关文档
vignette("xts");

ibm.daily[2];
ibm.daily[2:4];
ibm.daily[as.Date('2010-01-05')];
dates <- seq(as.Date('2010-01-04'),as.Date('2010-01-08'),by=2);
ibm.daily[dates];

# 时间序列的滞后 lag(ts,k);
lag(ibm.daily,k=+1,na.pad=TRUE); # na.pad=TRUE用NA来填充缺失的数据
lag(ibm.daily,k=-1,na.pad=FALSE); # na.pad=FALSE直接把缺失的数据删除
lag(ibm.daily,k=-1,na.pad=TRUE);

# 计算逐次差分
diff(ibm.daily);
diff(ibm.daily)/ibm.daily;
100*(diff(ibm.daily)/ibm.daily);
log(ibm.daily);
diff(log(ibm.daily));
# rollmean(ts,k); rollmean(ts,k,align=TRUE);
# aling=TRUE表示仅应用历史数据计算移动均值
# 在日历时间范围内应用函数
# apply.daily(ts,f); apply.weekly(ts,f); apply.monthly(ts,f);
# apply.quarterly(ts,f); apply.yearly(ts,f);

# 应用滚动函数 rollapply(ts,width,f,align="right");
# align="right",align="left",align="center"(default);
# 绘制自相关函数(Autocorrelation Function) acf(ts);
# 检验时间序列的自相关 Box.test(ts);
# 两个时间序列的滞后相关性 ccf(ts1,ts2);

# 时间序列的平滑 
# library(KernSmooth);
# gridsize <- length(y);
# bw <- dpill(t,y,gridsize=gridsize);
# lp <- locpoly(x=t,y=y,bandwidth=bw,gridsize=gridsize);
# smooth <- lp$y; t是时间变量，y是时间序列
t <- seq(from=-10,to=10,length.out=201);
noise <- rnorm(201);
y <- sin(t)+noise;
library(KernSmooth);
gridsize <- length(y);
# gridsize设定构造局部多项式所用的数据点的个数
bw <- dpill(t,y,gridsize=gridsize);
# locpoly()进行平滑操作，并返回列表，元素y是平滑后的数据
lp <- locpoly(x=t,y=y,bandwidth=bw,gridsize=gridsize);
smooth <- lp$y;
plot(y,type="l");
lines(smooth,type="l");