# Create a new qualitative variable, called Elite, by binning the Top10perc variable. We are going
# to divide colleges into two groups based on whether the proportion of students coming from
# the top 10% of their high school classes exceeds 50%, i.e., college$Top10perc >50.
# The task is to predict whether a college is elite or not.

# 1. Apply two machine learning algorithms to the dataset. One of the algorithms should have not
# been used in previous homeworks. In other words, one of the algorithms must be different
# from kNN, Naïve Bayes, linear regression and C5.0. Use confusion matrices and different
# performance measure to compare the algorithms. 20 points
# load packages
library(caret)
library(e1071)
library(randomForest)
library(xgboost)

# set seed for future runds
set.seed(123)

# read in data
df.colleges <- read.csv("~/Downloads/colleges.csv")

# create is_elite boolean
df.colleges$is_elite <- ifelse(df.colleges$Top10perc > 50, 1, 0)

table(df.colleges$is_elite)

# make private into into boolean
df.colleges$Private <- ifelse(df.colleges$Private == 'Yes', 1, 0)


# randomize data order so that the test/train split
# won't be alphabetic like the data
rows <- sample(nrow(df.colleges))
df.colleges.random <- df.colleges[rows, ]

# get sample 
sample_size <- round(nrow(df.colleges.random) * .7, 0)
# split data to get test data
train_data <- sample(seq_len(nrow(df.colleges.random)), size = sample_size)
# split data set between test and training data
train.df.colleges.random <- subset(df.colleges.random[train_data, ], select=-c(X, Top10perc, Top25perc))
test.df.colleges.random <- subset(df.colleges.random[-train_data, ], select=-c(X, Top10perc, Top25perc))

# get table of values
table(test.df.colleges.random$is_elite)
table(train.df.colleges.random$is_elite)

################## naive bayes
# train bayes classifier
naive_bayes_classifier <- naiveBayes(as.factor(is_elite) ~ ., data = train.df.colleges.random)

# predict data using model against test data
bayes_test_pred <- predict(naive_bayes_classifier, subset(test.df.colleges.random, select=-c(is_elite)))

# get model statistics
caret::confusionMatrix(as.factor(bayes_test_pred), as.factor(test.df.colleges.random$is_elite))


################### random forest model
# train rf classifier
rf_classifier <- randomForest(as.factor(is_elite) ~ ., data = train.df.colleges.random,
                             ntree=100, mtry=2, importance=TRUE)

# get model importances
varImpPlot(rf_classifier)

# pred against test
rf_pred <- predict(rf_classifier, subset(test.df.colleges.random, select=-c(is_elite)))

# get model statistics
caret::confusionMatrix(as.factor(rf_pred), as.factor(test.df.colleges.random$is_elite))


# 2. Perform automated parameter tuning for both models (if they allow it) using the caret
# package. 20 points
# random forest auto tuning
rf_m <- train(as.factor(is_elite) ~ ., data = train.df.colleges.random, method = "rf")
rf_m
# predict
rf_pred_tuned <- predict(rf_m, subset(test.df.colleges.random, select=-c(is_elite)))

# rf model stats
caret::confusionMatrix(as.factor(rf_pred_tuned), as.factor(test.df.colleges.random$is_elite))

# naive bayes auto tuning
nb_m <- train(as.factor(is_elite) ~ ., data = train.df.colleges.random, method = "nb")
nb_m
# predict
nb_pred_tuned <- predict(nb_m, subset(test.df.colleges.random, select=-c(is_elite)))

# nb model stats
caret::confusionMatrix(as.factor(nb_pred_tuned), as.factor(test.df.colleges.random$is_elite))


# 3. Try to improve the performance of each algorithm by using ensemble learning (one method
#   of ensemble learning of your choice) and the caret package. Compare the algorithms. 20 points

xg_m <- train(as.factor(is_elite) ~ ., data = train.df.colleges.random, method = "xgbTree")
xg_m
# predict
xg_pred_tuned <- predict(xg_m, subset(test.df.colleges.random, select=-c(is_elite)))

# xgboost model stats
caret::confusionMatrix(as.factor(xg_pred_tuned), as.factor(test.df.colleges.random$is_elite))
