medicine=c(rep("placebo",3),rep("A",4),rep("B",3));
medicine=as.factor(medicine);
levels(medicine);
levels(medicine)=c("MedicineA","Medicine B","Placebo");

m1=matrix(c(1:9),nrow=3,ncol=3,byrow=T);
m2=matrix(c(1:9),nrow=3,ncol=3,bycol=T);
attributes(m1);
as.vector(m1);
dim(m1);
dimnames(m1);
dimnames(m1)=list(c("row1","row2","row3"),
	c("col1","col2","col3"));

x <- c(c(1,2,3),c(4,5,6),c(7,8,9));
x_mat <- matrix(x,3,3,byrow=T); # 默认按列填充
x_mat <- matrix(x,3,3,bycol=T); # 与下一行等价
x_mat <- matrix(x,3,3,);

blah <- list(c("l","two","three","4"),
	matrix(c(1,2,3,4,5,6),nrow=2,ncol=3),c(1,7,17));
blah[1];
blah[[1]];
blah[[1]][3];
blah[[2]][1:2,2];
names(blah) <- c("score","a.matrix","some.numbers");
blah$score;
blah$a.matrix;
blah$some.numbers;
attributes(blah);