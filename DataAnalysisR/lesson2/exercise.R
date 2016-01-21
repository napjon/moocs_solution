reddit <- read.csv('Lesson2/reddit.csv')
getwd()
table(reddit$employment.status)
summary(reddit)
levels(reddit$age.range)
qplot(data = reddit, x = income.range)
reddit$age.range <- ordered(reddit$age.range, levels=c("Under 18", "25-34", "35-44", "45-54", "55-64", "65 or Above","NA"))
is.factor(reddit.age.range)
reddit.age.range
qplot(data=reddit,x = age.range)
levels(reddit.age.range)
reddit$income.range
