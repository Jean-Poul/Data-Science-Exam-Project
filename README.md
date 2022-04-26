# The Medias Influence On The Stock Market  

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Nina Lisakowski, cph-nl163

## Brief introduction:  
Our focus will be to build a model which can analyze if news are negative or positive. The next step will be to evaluate if there is a direct correlation with these news articles and the stock price. We find it interesting to investigate the psychological aspect of news outlets and how they can affect peoples investment choices. Furthermore the stock market is notoriously unpredictable and therefore it is interesting to challange ourselves to build a model that can predict the trends in the market. We expect to find a correlation between news from well established news outlets and with some probability be able to predict the trend of the stock in focus. An end user of our results may be someone who wants to take the first step into investing/trading. Our model could be a tool to help newcommers to establish confidence in their investment/trade.  

### Exam Project Stage 1: Business

### Objective: Foundation of a business case

### 1. By brainstorming and browsing sources of inspiration collect ideas and define one or more business or social domains, where data analysis can bring a value.  

During our brainstorm we had the following ideas:
- Stock market:  
Is it possible to find trends in stocks/indices and is it possible for outside events to affect the price action.
- Gaming:   
What parameters does it take to make a good game and can we predict how well a game will sell.
- Programmer:  
What paramters (programming language, age, experience, location, education, gender) has an effect on a developers salary.
- Health:  
Can we predict whether a person will get a specific health issue (heart disease, diabetes, cancer) when looking at their current health factors.
- Sport:  
Can we predict whether a football team will win when looking at their current lineup.  
- Space:  
Can we classify whether we have identified a new planet or is it an already discovered planet.

### 2. Search Internet for sources of information, related to your ideas.
We will be more precise when we have chosen a subject but overall we have looked at the following sources for gathering data:
- Stock market:  
[Kaggle for dataset](https://www.kaggle.com/)  
[NYSE for data and news](https://www.nyse.com/index)  
[CNBC for news](https://www.cnbc.com/world/?region=world)  

- Gaming:  
[Kaggle for dataset](https://www.kaggle.com/)  
[Steam database](https://steamdb.info/)  
[Statistics](https://www.statista.com/topics/1680/gaming/#topicHeader__wrapper)  

- Programmer:    
[Kaggle for dataset](https://www.kaggle.com/)  
[Salary](https://data.world/datasets/salary)  
[Statistics](https://review42.com/resources/video-game-statistics/)  

- Health:   
[Kaggle for dataset](https://www.kaggle.com/)  
[Data.world for dataset](https://data.world/datasets/health)  
[Healthdata for dataset](https://healthdata.gov/)  

- Sport:   
[Kaggle for dataset](https://www.kaggle.com/)  
[Data.world for dataset](https://data.world/datasets/sports)  
[Statistics](https://sports-statistics.com/sports-data/sports-data-sets-for-data-modeling-visualization-predictions-machine-learning/)  

- Space:  
[Kaggle for dataset](https://www.kaggle.com/)  
[Data.world for dataset](https://data.world/datasets/space)  
[NASA for dataset](https://data.nasa.gov/)  

### 3. Choose one of the ideas and formulate context, purpose, research questions, and hypothesis for a data science problem definition.
We have chosen to go with our first idea by looking at the stock market since we have an interest for this area and there is a lot of data to be found.   

- Context:  
During COVID-19 a lot of average people started to invest in the stock market due to many factors. However the average person investing on a hobbyist basis, without any formal degree, most likely use some kind of information source as a basis for their investment choices. We would except to see that traditional news outlets, still have a dominant influence over investment choices. Therefore by analyzing news outlets we could potentially predict the future trend of a stock, and thereby formulate a guide for our own investment choice.

- Purpose:  
The purpose is to predict the future trend of a stock by looking at the publicity of the mentioned stock/company to guide our own investment plan.    

- Research questions:      
What stock exchange will be interesting for our purpose?  
Where should we look for news regarding stocks?    
How do other people gather information in this area?    
How do we differentiate between positive and negative news?    
Which news sites are relevant for our purpose and where do we collect our market data regarding the stocks in focus?  
Can we correlate news with the price action?   

- Hypothesis:  
The Research Hypothesis:   
Can trends on the stock markets be predicted, by analyzing publicity in news outlets.  
The Null Hypothesis:  
There is no correlation between news outlets and trends on the stock markets.

### 4. Prepare the technical platform needed for researching and developing the problem solution:  

The following is an overview over our initial thoughts about our programming environment. This can change when further information has been gathered and scope of the assignment has been agreed apon.  

- Software tools:  
Jupyter notebook  
Docker runtime  

- Languages:  
Python  

- Libraries:  
Numpy  
Matplotlib  
Pandas  
Sklearn  
Seaborn  

- Databases:  
MongoDB(store the data)  
Neo4J(analyse relations between the data)  

- Programming environment:  
Agile methods such as scrum(meetings and kanban board) and extreme programming(pair programming)  
Depending on scope of the project then DevOps might be applied to make a pipeline and use CI/CD.   



