library(readxl)
library(dplyr)
library(tidyr)
library(ggplot2)
library(scales)

out_dir   <- "Desktop/dsi/visualization/02_activities/assignments/assignment_3/r_outputs"
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

# Read data
df <- read_excel("Desktop/dsi/visualization/02_activities/assignments/assignment_3/data/1985-2019 Analysis of ridership.xlsx")
year_row <- unlist(df[4, -1])   
total_row <- unlist(df[66, -1])   
weekday_row <- unlist(df[64, -1])  
weekend_row <- unlist(df[65, -1])  

# Parse years (i.e., "2015 *")
years <- suppressWarnings(as.numeric(gsub("[^0-9]", "", as.character(year_row))))
years <- years[!is.na(years) & years >= 1985 & years <= 2019]

n <- length(years)
total <- suppressWarnings(as.numeric(total_row[1:n]))
weekday <- suppressWarnings(as.numeric(weekday_row[1:n]))
weekend <- suppressWarnings(as.numeric(weekend_row[1:n]))

# Figure 1: Annual ridership line plot
df1 <- data.frame(Year = years, Ridership = total) %>% 
  filter(!is.na(Ridership)) %>% 
  arrange(Year)

p1 <- ggplot(df1, aes(x = Year, y = Ridership)) +
  geom_line(linewidth = 1, color = "steelblue") +
  geom_point(size = 3, shape = 21, fill = "white", stroke = 1, color = "steelblue") +
  scale_x_continuous(breaks = seq(1985, 2019, by = 5)) +
  scale_y_continuous(labels = label_comma()) +
  labs(title = "TTC Annual Ridership (1985–2019)", x = "Year", y = "Ridership (thousands)") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, face = "bold"))

ggsave(file.path(out_dir, "r_viz_1_ridership.png"), p1, width = 8, height = 5, dpi = 300)

# Figure 2: Weekday vs Weekend ratio
df2 <- data.frame(Year = years, Weekday = weekday, Weekend = weekend) %>%
  filter(!is.na(Weekday), !is.na(Weekend)) %>%
  arrange(Year) %>%
  pivot_longer(cols = c(Weekday, Weekend), names_to = "DayType", values_to = "Ridership") %>%
  group_by(Year) %>%
  mutate(Share = Ridership / sum(Ridership)) %>%
  ungroup() %>%
  mutate(DayType = ifelse(DayType == "Weekday", "WEEKDAY", "WEEKEND/HOLIDAY"))

p2 <- ggplot(df2, aes(x = as.factor(Year), y = Share, fill = DayType)) +
  geom_col(width = 0.8) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_manual(values = c("WEEKDAY" = "#F4A3A3", "WEEKEND/HOLIDAY" = "#8FD19E"), name = "") +
  labs(title = "TTC Ridership Share: Weekday vs Weekend/Holiday", x = "Year", y = "Share of Annual Ridership") +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, face = "bold"),
        axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1),
        legend.position = "bottom")

ggsave(file.path(out_dir, "r_viz_2_weekday_weekend.png"), p2, width = 10, height = 5, dpi = 300)
