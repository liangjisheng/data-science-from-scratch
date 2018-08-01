if (0){
n <- 5:10
x <- c(2,4,6)
all <- c(n,x)
all[3]
all[c(1,3,5)]
all[-c(1,3,5)]
is.numeric(all)
is.character(all)
all=as.character(all)
is.character(all)
all
all[c(3:5)]
plot(kai$时间,kai$开盘)
cat("li")
}

odd=0
even=0
for(i in 1:length(all)) {
if(all[i]%%2==0) even=c(even,i)
else odd=c(odd,i)
}
odd=odd[-1]
even=even[-1]
cat("all:",all,"\n")
cat("奇数的索引号:",odd,"\n")
cat("偶数的索引号:",even,"\n")