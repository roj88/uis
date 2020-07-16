# 1. Load Boston.cvs data set. It records 14 variables for 506 neighborhoods around Boston
df.boston <- read.csv("~/Downloads/Boston.csv")

# 2. Which suburbs have low crime rates?
head(df.boston[order(df.boston$crim),], 5)

# 3. Create a binary variable, crim1, that contains 1 if crim contains a value above its 
# median, and a 0 if crim contains a value below its median. You can compute the median using
# the median() function.
df.boston$crim1 <- ifelse(df.boston$crim > median(df.boston$crim), 1, 0)

# 4. Explore the data in order to investigate the association between crim1 and the other features.
# Which of the other features seem most likely to be useful in predicting crim1? Decide which
# attributes you are going to use to predict crim1. 5 points
# create correlation matrix
df_boston_correlation_matrix <- cor(subset(df.boston, select = -c(X)))
df_boston_correlation_matrix["crim1", ]

# 5. Set the seed of the random number generator to a fixed integer so that you can reproduce your work. 1 point
set.seed(123)

# 6. Normalize the attribute values 2 points
# the function normalize normalizes numberical data
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}
# normalize data and place into a seperate data frame
df.boston.normalized <- as.data.frame(lapply(df.boston[2:16], normalize))
df.boston.normalized

# 7. Randomize the order of the rows in the dataset. 2 points
rows <- sample(nrow(df.boston.normalized))
df.boston.normalized <- df.boston.normalized[rows, ]

# 8. Split the data into a training set and a test set. Use a test set of 100 rows. 4 points
# get test training size
sample_size <- 100
# split data to get test data
test_data <- sample(seq_len(nrow(df.boston.normalized)), size = sample_size)
# split data set between test and training data
test.df_boston_normalized <- subset(df.boston.normalized[test_data, ], select=c(indus, nox, age, dis, rad, tax))
train.df_boston_normalized <- subset(df.boston.normalized[-test_data, ], select=c(indus, nox, age, dis, rad, tax))
# store labels
train.df_boston_normalized.labels <- df.boston.normalized[-test_data, 15]
test.df_boston_normalized.labels <- df.boston.normalized[test_data, 15]


# 9. Perform kNN on the training data, with several values of K, in order to predict crim1. Which value
# of K seems to perform the best on this data set? 6 points
# import library
library(class)
library(gmodels)
library(caret)

# run a for loop in order to get the best k by the model accuracy
x <- c(1:20)
newdf <- data.frame(K=integer(),
                 Accuracy=double(),
                 False_Positive=integer(),
                 False_Negative=integer()) 
for(i in x) {
  test_pred <- knn(train = train.df_boston_normalized,
                   test = test.df_boston_normalized,
                   train.df_boston_normalized.labels, k = i, l = 0, prob = FALSE, use.all = TRUE)
  # calc confusion matrix
  confusion_matrix <- table(test_pred, test.df_boston_normalized.labels)
  n <- sum(confusion_matrix)
  diag <- diag(confusion_matrix)
  # get the accuracy
  accuracy <- sum(diag) / n
  fp <- confusion_matrix[[2,1]]
  fn <- confusion_matrix[[1,2]]
  
  # place k and accuracy in a table
  single_line_df <- data.frame(i, accuracy, fp, fn)
  
  # append data to empty df
  newdf <- rbind(newdf, single_line_df)
}

# plot out the k vs the accuracy
plot(newdf$i, newdf$accuracy, main="kNN K-Value vs Model Accuracy", xlab="k-value", ylab="model accuracy")
lines(newdf$i, newdf$accuracy)
newdf


# 10. Run a Naïve Bayes classifier to predict crim1. Remember that the Naïve Bayes does not require that
# attributes be normalized and the rows be randomized. 10 points
# import package
library(e1071)

sample_size <- 100
# split data to get test data
test_data <- sample(seq_len(nrow(df.boston)), size = sample_size)
# split data set between test and training data
test.df_boston <- subset(df.boston[test_data, ], select=c(indus, nox, age, dis, rad, tax, crim1))
train.df_boston <- subset(df.boston[-test_data, ], select=c(indus, nox, age, dis, rad, tax, crim1))

# run bayes classifier
naive_bayes_classifier <- naiveBayes(as.factor(crim1) ~ ., data = train.df_boston)

# predict data using model against test data
bayes_test_pred <- predict(naive_bayes_classifier, subset(test.df_boston, select=-c(crim1)))

# get prediction confusion matrix
bayes_confusion_matrix <- table(bayes_test_pred, test.df_boston$crim1)
bayes_confusion_matrix
# get the accuracy
n_bayes <- sum(bayes_confusion_matrix)
diag_bayes <- diag(bayes_confusion_matrix)
accuracy <- sum(diag_bayes) / n_bayes
accuracy
bayes_confusion_matrix[[2,1]] # false positive
bayes_confusion_matrix[[1,2]] # false negative