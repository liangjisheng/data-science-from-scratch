which(all==9|all==10)
all[c(which(all==9|all==10))]
for(i in 1:length(all)) if(all[i]%%2==0) cat(i,"\t");cat("\n")
for(i in 1:length(all)) if(all[i]==9|all[i]==10) cat(i,"\t"); cat("\n")
t1=proc.time();which(all==9|all==10); t2=proc.time(); t2-t1;
t1=proc.time();
for(i in 1:length(all)) if(all[i]==9|all[i]==10) cat(i,"\t");c("\n");
t2=proc.time();
t2-t1;

odd=0
even=0
for(i in 1:length(all)) {
	if(all[i]%%2==0) even=c(even,i) else odd=c(odd,i)
}
odd=odd[-1]
even=even[-1]
cat("all vector:", all,"\n")
cat("奇数索引号: ",odd,"\n")
cat("偶数索引号: ",even,"\n")

for(i in 1:10) for(j in 1:10) if(data[i,j]>5) tem[i,j]=1

x <- c(1,2,3,4,5);y <- c(3,5,7,9);
2*x
2*y
t(y)
y/10
x%*%t(y)

x <- matrix(c(1:6),2,3); y <- matrix(c(1:6),3,2);
x%*%y
y%*%x