



data = read.csv("Results.csv", header = FALSE)
colnames(data) = c("Method", "Measure", "Wiki", "Number")

require(dplyr)
require(tidyr)
require(xtable)

improvement = c()

for(i in c(0:7)){
  improvement[(i*6+1):(i*6+6)] = 
  data$Number[(i*12+7):(i*12+12)] - data$Number[(i*12+1):(i*12+6)]
}

improvement = data.frame(0, 0, 0, improvement)
colnames(improvement) = c("Method", "Measure", "Wiki", "Improvement")

for(i in c(0:7)){
  improvement$Method[(i*6+1):(i*6+6)] = 
    data$Method[(i*12+1):(i*12+6)] 
  improvement$Measure[(i*6+1):(i*6+6)] = 
    data$Measure[(i*12+1):(i*12+6)] 
  improvement$Type[(i*6+1):(i*6+6)] = 
    data$Type[(i*12+1):(i*12+6)] 
}


data_wider = data %>%
  pivot_wider(names_from = Measure, values_from = Number)
improvement_wider = improvement %>%
  pivot_wider(names_from = Measure, values_from = Improvement)


xtable(data_wider, digits = 3, type = "latex",
       caption = "Performance of Models with and without KSI framework and New/Original Wikipedia")

xtable(improvement_wider, digits = 3, type = "latex",
       caption = "Improvement of Models with KSI framework using New vs Original Wikipedia")

