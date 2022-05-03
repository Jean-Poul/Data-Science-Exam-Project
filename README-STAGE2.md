# Exam Project Stage 2: Data 

#### Objective: Data acquisition and exploration 
Based on the ideas and assumptions defined at the previous stage of your business case analysis,
create the first prototype of your solution implementation.
1. Searching Internet and other media, find relevant data sources that can be used in your 
experiments.  
News source:  

https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests
https://www.kaggle.com/datasets/aaron7sun/stocknews

Ticker prices:  
https://www.kaggle.com/datasets/paultimothymooney/stock-market-data

2. Collect and integrate the data sources in shared repository by either ETL (Extract Transform Load) 
or ELT (Extract Load Transform).  
Our data will be loaded straight into the system to begin with. This might change further down the line. Thoughts:  
- Webscrape news.  
- Load data from our database.   


3. Explore the data by applying methods of descriptive and inferential statistics. 
 - a. design data processing scenario 

 - b. decide on data processing parameters

 - c. apply data visualisation techniques

 - d. prepare a dashboard as a collection of diagrams and brief explanation that can serve the 
selected business CPH Business 2022 Spring {tdi, ste}@cphbusiness.dk  

4. Prepare the data for machine learning analysis, ensuring that the data is:  

 - a. meaningful – describes relevant and correctly measured features and observations  

 - b. sufficient – describes various cases and feature occurrences, decided by testing 

 - c. shaped – presented in a structure, appropriate for processing by machine learning 
algorithms  

 - d. cleaned – repaired from missing values and outliners  

 - e. scaled – transform data distributions in comparable scales, when necessary  

 - f. engineered – analyse all features and select the most informative for further processing
Export your notebook solution to Github and a link to it in Peergrade.  

__________________________
Deadline: 6th May 2022
#TODO:  
- Clean data from missing values
	- format='%Y-%m-%d %H:%M:%S'
	- remove start years (2009) and ends year (NaN and 2020)


