# https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629#258862
erfinv <- function (x) qnorm((1 + x)/2)/sqrt(2)

RankGauss <-function(torank){
if( !is.data.frame(torank) & !is.matrix(torank))
{ stop(" The input data must be one data frame or matrix")}
allrank <-apply(torank,2,rank,ties.method="min")
allsort <-torank[!duplicated(torank),]
allsort <-as.data.frame(sapply(torank, sort))
rowrank <-rowSums(allsort)/ncol(torank)
rowrank <-data.frame(allsort, Value=rowrank)
rowrank$RankScale <-seq(from=-.9999, to=.9999, length.out = nrow(rowrank)) # We use the inverse sigmoid
rowrank$RankDist <-with(rowrank,erfinv(RankScale))
back <-apply(allrank, c(1,2), function(onerank){rowrank$RankDist[onerank]}) #Very slow here
back <-as.data.frame(back) names(back) <-names(torank) return(back)
}
