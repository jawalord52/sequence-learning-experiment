#install packages
install.packages("MCMCglmm")

#initialise MCMCglmm library
library(MCMCglmm)

#import data file
exp_9_combined

#check for normal distribution
hist(exp_9_combined$response_time)
hist(log(exp_9_combined$response_time))

#model with frequency as a main predictor, response_time transformed to normal
mcmc.freq<-MCMCglmm(fixed = log(response_time) ~ freq + distance + age,
                 nitt=10000, random=~subject_nr, 
                          data= exp_9_combined)
						  
#model with transitional probability as a main predictor, response_time transformed to normal
mcmc.tp<-MCMCglmm(fixed = log(response_time) ~tp + distance + age,
                 nitt=10000, random=~subject_nr, 
                 data= exp_9_combined)
				 
#model with both frequency and transitional probability as a main predictor, response_time transformed to normal
mcmc.both<-MCMCglmm(fixed = log(response_time) ~tp + freq + distance + age,
                  nitt=10000, random=~subject_nr, 
                  data= exp_9_combined)

#model summaries
summary(mcmc.freq)
summary(mcmc.tp)
summary(mcmc.both)