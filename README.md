# freelancer-webScraping-analysis

## Overview
#### This project involves scraping freelancer data from Freelancer.com and performing an analysis on the freelancers' performance. We gather information such as their skills, hourly rate, reviews, rating, and other key metrics to understand the patterns and insights that can help freelancers improve their performance on the platform.

## What You’ll Find in This Repository:
#### 1-Data Scraping: Python script using Selenium to scrape freelancer profiles based on various skills.
#### 2-Data Cleaning: Using Pandas to clean and organize the scraped data into a structured format.
#### 3-Analysis: Various statistical analyses and visualizations to understand trends like hourly pay across skills, ratings vs reviews, on-time delivery rates, and more.
#### 4-Data Export: Exporting the cleaned data to an Excel file for further analysis.

## Take Care!
#### Scraping may take a long time, especially if you are scraping multiple pages. To manage this, you can limit the number of pages the scraper navigates through. This can be done by modifying the get_freelancers function in the script, where c controls the page number (you can change it to limit the number of pages).

## Conclusions:
#### The project provides valuable insights into the freelance market, specifically on Freelancer.com. Key findings include:

#### India leads the market with the highest number of active freelancers (3,542), followed by the USA (902). Egypt ranks 9th with just 136 active freelancers.

#### The most common skill is JavaScript, making it one of the most competitive fields.

#### The average hourly rate for freelancers is $26/hour, and $27/hour for those who have successfully completed projects.

#### Machine Learning specialists command the highest average hourly rate at $29/hour.

#### Only 23.42% of freelancers complete projects within the agreed budget, highlighting the importance of clear communication and set expectations.

#### There is a strong correlation between on-time delivery and reemployment rate (14.5%), suggesting that freelancers who meet deadlines are more likely to be rehired.
