x <- seq(from=-3,to=3,length.out=100)
y <- dnorm(x)
plot(x,y,main="Standard Normal Distribution",type='l',
ylab="Density",xlab="Quantile")
abline(h=0)
# The body of the polygon follows the density curve where 1 <= z <= 2
region.x <- x[1 <= x & x <=2]
region.y <- y[1 <= x & x <=2]
# we add initial and final segments,which drop down to the Y axis
region.x <- c(region.x[1],region.x,tail(region.x,1))
region.y <- c(	      0,region.y,	   	 	 0)
# polygon(region.x,region.y,density=10)
polygon(region.x,region.y,density=10,col="red")