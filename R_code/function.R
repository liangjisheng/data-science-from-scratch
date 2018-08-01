stdev=function(x)
{
	sqrt(var(x));
}
z=c(1,2,0.45,-1.2,2.3);
stdev(z);
is.function(stdev);
mystdev=stdev;

test="unchanged";
changed=function()
{
	test="changed";
	test;	# test为函数返回值,为局部变量
}
changed();
test;
test=changed();
stdev; # 只输入函数的名称会显示函数的定义
fix(stdev); # 出现记事本窗口，更改stdev的定义,关闭后自动存储
edit(file="exam_1.r");# 编辑exam_1.r文件

total=0;
for(i in 1:10) {
	total=total+i;
}
total;

total=0;
for(i in c(1,2,4,5,9))
	total=total+i;
total;

# stretch() 把向量中的每一个元素复制相同的次数
stretch=function(vec,num)
{
	output=c();
	for(i in 1:length(vec))
		output=append(output,rep(vec[i],num));
	output;
}
stretch(c("li","shu","yu"),4);
rep(c("li","shu","yu"),4);

x=1;
if(x<1) { "x is less than one"} else {" x is greater than or equal to one"}

# 这个函数不能工作
max.power=function(x,y)
{
	if(x<y & x>0)
		if(x>1) {
			i=1;
			total=x;
			while(total*x<y) {
				i=i+1;
				total=total*x;
			}
			i;
		}
		else "Infinity"
	else NULL
}

# 向量化运算比循环更节省时间
get.mean=function(x) {
	report=rep(0,4);
	for(i in 1:4)
		report[i]=mean(x[,i]);
	report;
}
data(iris);
get.mean(iris);

apply(iris[,1:4],2,mean); # 2指第二维，对列求均值

stdev=function(x)
{
	# stdev with error handing
	if(!is.vector(x))
		stop("The argument to stdev must be a vector")
	else sqrt(var(x))
}
z=rnorm(100);
stdev(z);
z=as.matrix(z);
stdev(z);