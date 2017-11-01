#install packages
install.packages("lme4")

#import data file
exp_9_combined

#initialise lme4 library
library(lme4)

#Non MCMC method implemented as check
lmer.freq <- lmer(response_time~ freq + distance + age + (1|subject_nr), data = exp_9_combined)

lmer.tp <- lmer(response_time~ tp + distance + age + (1|subject_nr), data = exp_9_combined)

lmer.both <- lmer(response_time~ freq + tp + distance + age + (1|subject_nr), data = exp_9_combined)

summary(lmer.freq)
summary(lmer.tp)
summary(lmer.both)

#model comparisons
anova(lmer.tp, lmer.freq)
anova(lmer.freq, lmer.both)