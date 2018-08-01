# solve() 计算线性方程组 Ax=B 使用solve(a,b)
a=matrix(runif(16),4,4);
b=matrix(rnorm(16),4,4);
solve(a,b);

#如果solve里只有一个矩阵，R会自动使用单位矩阵带入b，求得a的逆矩阵
solve(a);
I=solve(a)%*%a;
for(i in 1:4) for(j in 1:4) if(i!=j) I[i,j]=0

#制造10个顾客会员卡号
uid=as.character(round(runif(10)*100000)+100000);
#制造10个ip地址
ip=rep(NA,10);
for(i in 1:10) {
	ip1=as.character(round(runif(1)*200));
	ip2=as.character(round(runif(1)*200));
	ip3=as.character(round(runif(1)*200));
	ip4=as.character(round(runif(1)*200));
	ip[i]=paste(ip1,".",ip2,".",ip3,".",ip4,sep="");
}
#把前面制造的顾客会员卡号与ip地址合并
data=cbind(uid,ip);
data.tmp=data;
#复制前面这笔data数据99遍，构造1000个数据
for(i in 1:99) data.tmp=rbind(data.tmp,data);
data=data.tmp;
#制造100个不同的日期
today=Sys.time();
dtime=rep(today,100);
for(i in 1:100) dtime[i]=today+round(rnorm(1)*1000000);
#复制者100个时间9遍，构造1000个数据，与data合并
dtime=as.character(dtime);
dtime.tmp=dtime
for(i in 1:9) dtime.tmp=c(dtime.tmp,dtime)
dtime=dtime.tmp;
data=cbind(data,dtime);
#制造1000个随机出现的A到Z的字母，当做被浏览过的网页
#LETTERS()这个函数可以自动生成从A到Z的所有字母
url=rep(NA,10);
for(i in 1:nrow(data)) {
	url.tmp=round(runif(1)*25+1);
	url[i]=LETTERS[url.tmp];
}
#合并数据
data=cbind(data,url);
#查看生成的数据
head(data); #显示数据结构和前6行数据


uip=levels(factor(data[,"130.90.177.53"])); #取出独特ip
uip.no=length(uip); #计算独特ip的数量
m=0; #第m此浏览，出事设为0
for(i in 1:uip.no) {
	#找出相同ip在data里的索引位置
	uip.which=which(data[,"ip"]==uip[i]);
	data.uip=data[uip.which,];#挖出所有相同ip的数据
	#因为我们只想要比较日期，所以把data.uip里的时间去掉
	#只留下日期（日期在dtime里的第1到第10个字符）
	data.uip=cbind(data.uip[,c("uid","ip")],substr(data.uip[,"dtime"],1,10),data.uip[,"url"]);
	colnames(data.uip)=c("uid","ip","dtime","url");
	udate=levels(factor(data.uip[,"2016-08-02"])); #取出同一ip里的独特日期
	udate.no=length(udate); #计算同一ip里独特如期的数量
	for(j in 1:udate.no){
		m=m+1;#找到第m此浏览
		#找出所有相同日期在data.uip里的位置
		udate.which=which(data.uip[,"dtime"]==udate[j]);
		#以下开始构造复杂数据结构：第m行第1栏放uid
		path[[m]][1]=data.uip[i,"uid"];
		#第m行第2栏放ip
		path[[m]][2]=data.uip[i,"ip"];
		#第m行第3栏放日期
		path[[m]][3]=udate[j];
		#搜集第m此浏览的所有路径，放第4栏
		path[[m]][4]=as.list(data.uip[udate.which,"url"]);
	}
}