setwd("C:/Users/prabat/Desktop/AA")
hours <- read.csv('hours.csv', as.is = T)
dates <- read.csv('dates.csv', as.is = T)
users <- read.csv('output.csv', as.is = T)

library(ggplot2)

dates$Date<-as.Date(dates$Date, format = "%d-%m-%Y")

d <- ggplot(data=dates, aes(x = dates$Date, y = dates$Freq))
d <- d + geom_area(size = 0.01, fill = "firebrick")
d <- d + ggtitle("User Activity over Time") + labs(x = "Time", y = "Messages")
d <- d + theme(axis.text.x = element_text(angle = 90)) + scale_x_date(date_labels = "%b", date_breaks = "1 month")
ggsave("Dates.png", width=15, height=9, dpi=300)


u <- ggplot(data=users, aes(x = reorder(users$Name, users$Freq), y = users$Freq))
u <- u + geom_bar(fill="firebrick", stat = "identity")
u <- u + labs(title = "Most Active Users in the Group")
u <- u + geom_text(aes(label=users$Name), hjust = 1.6, color = "white", size = 4.6)
u <- u + labs(x = NULL, y = "Messages") + scale_y_continuous(breaks = seq(0,1000, by = 100), minor_breaks = waiver()) + coord_flip() 
u <- u + theme(axis.text.y=element_blank())
ggsave("Users.png", width=15, height=9, dpi=300)


h <- ggplot(data = hours, aes(hours$Hour, hours$Freq, group = 1))
h <- h + geom_line(color = "firebrick", size = 1.0)
ggsave("Hours.png", width=15, height=9, dpi=300)

