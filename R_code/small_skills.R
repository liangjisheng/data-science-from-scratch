head(kai); # 查看前6行数据
tail(kai); # 查看后6行数据
# options(width=numcols); 拓宽列的输出
x <- 1/pi; # Prints nothing
(x <- 1/pi); # prints assigned value

x <- cbind(rnorm(5),rnorm(5),rnorm(5),rnorm(5),rnorm(5));
rowSums(x); # 对各行求和
colSums(x); # 对各列求和
rbind(x,Total=colSums(x));

x <- rnorm(5);
y <- rnorm(5);
print(x);
print(cbind(x,y));
print(cbind(x,y,Total=x+y));

x <- rnorm(1000);
breaks <- c(-3,-2,-1,0,1,2,3);
f <- cut(x,breaks);
summary(f);
f <- cut(x,breaks,labels=c("Bottom","Low","Neg","Pos","High","Top"));
summary(f);

vec <- c(100,90,80,70,60,50,40,30,20,10);
match(80,vec);
which.min(vec);
which.max(vec);
vec[seq_along(vec)%%2==0]; # 每隔两个取一个元素
vec[c(TRUE,FALSE)];

# 找到成对的最大值和最小值
pmin(1:5,5:1);
pmax(1:5,5:1);
x <- rnorm(50);
x <- pmax(x,0); # 将x中的负数置为0
v <- c(-1,-2,-3,-4,-5,-6,7);
pmax(v,0);

# 生成多个因子的组合
side <- factor(c("Heads","Tails"));
faces <- factor(c("1 pip",paste(2:6,"pips")));
expand.grid(side,faces); # 各个因子的所有组合,笛卡尔积
expand.grid(faces,faces);

dfrm <- data.frame(month=c(7,8,8,6,7),day=c(11,10,25,27,22),
	outcom=c("win","Lose","Tie","Tie","Win"));
dfrm[order(dfrm$month),]; # 排序
dfrm[order(dfrm$month,dfrm$day),];

attributes(dfrm);
class(x); # 
mode(x);
str(x);

x <- c(1:100);
y <- 3*x+5+rnorm(100);
m <- lm(y~x);
class(m);
mode(m);
names(m);
str(m);
m$coefficients;

system.time(sum(rnorm(1000000)));
warning();

vec <- c(1,3,5,7,9);
mean(vec);
numbers <- list(1,3,5,7,9);
mean(numbers); # 不能对列表求均值
mean(unlist(numbers));

lists <- list(col1=list(7,8,9),col2=list(70,80,90),col3=list(700,800,900));
cbind(lists); # 不是想要的结果
cbind(unlist(lists)); # 转换成一个长的一列
do.call(cbind,lists); # 得到想要的结果
cbind(lists[[1]],lists[[2]],lists[[3]]);
lists[1];
lists[[1]];
lists[[1]][1];
lists[[1]][2];

# 定义自己的运算符
'%+-%' <- function(x,margin) x+c(-1,1)*margin;
100 %+-% (1.96*15);
100 %+-% 1.96*15;
'%+%' <- function(s1,s2) paste(s1,s2,sep="");
"Hello" %+% "World";
"limit=" %+% round(qnorm(1-0.05/2),2);