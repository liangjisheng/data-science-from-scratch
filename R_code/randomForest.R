iris.obj <- rfsrc(Species ~ ., data = iris,tree.err = TRUE, importance = TRUE)
plot(iris.obj)
v.obj <- rfsrc(Surv(time,status)~.,veteran)
plot(v.obj)
plot.survival(rfsrc(Surv(time, status)~ ., veteran), cens.model = "rfsrc")

