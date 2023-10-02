#install.packages("caret")
library(caret)

CreateModel_ErrorRate <- function(x) {
# credit_data is Credit-screening-23.csv
# function to construct a C5.0 model on all data in credit_data except fold x 
# returns the success rate when tested on the fold x
    credit_data_train <- credit_data[-x,]
    credit_data_test <- credit_data[x,]
    credit_model <- C5.0(credit_data_train[-16], credit_data_train$class)
    error_rate <- sum(predict(credit_model,credit_data_test) != credit_data_test$class)/nrow(credit_data_test)
    success_rate <- 1 - error_rate
    return(success_rate)}
    
CrossValidate <- function(seed, NumFolds) {
# perform cross-validation on credit_data which is Credit-screening-23.csv
# return a list of the error rates on the individual folds
     set.seed(seed)
     # divide credit_data into NumFolds
     myfolds <- createFolds(credit_data$class, NumFolds)
     # construct a list of success rates on each fold
     SuccessRateList <- lapply(myfolds,CreateModel_ErrorRate)
     SuccessRate <- sum(unlist(SuccessRateList))/NumFolds
     return(append(SuccessRateList,SuccessRate)) }

Rmushroom <- read.csv("C:/Users/Eli Brignac/OneDrive/Desktop/CISC-483/Data-Mining/HW3/Mushroom-data-23R.csv", stringsAsFactors = TRUE)

str(Rmushroom)