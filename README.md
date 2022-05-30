# The Medias Influence On The Stock Market  

This is an exam project for Data Science on CPH Business software developer bachelor.

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Nina Lisakowski, cph-nl163

## Brief introduction:  
Our focus will be to build a model which can analyze if news have a negative or positive impact on a given stock. We will thereafter evaluate if there is a direct correlation with news articles and the stock price. We find it interesting to investigate the psychological aspect of news outlets and how they can affect peoples investment choices. Furthermore, the stock market is notoriously unpredictable and therefore it is interesting to challange ourselves to build a model that can predict the trends in the market. We expect to find a correlation between news from well established news outlets and with some probability be able to predict the trend of the stock in focus. An user who might be interested in our results may be someone who wants to take the first step into investing or trading. Our model could be a tool to help newcommers to establish confidence in their investment or trading choices.  
 
## Getting started:  
  
```shell
Run the whole jupyter notebook to get an understanding of all steps and  
thoughts taken throughout this project
```   
  
## Environment:  
All imports can be found in the first section of our notebook. It it recommended to run the whole notebook to get all the necessary libraries installed on your computer.  
    
## How to use the model:  

To be able to test our model navigate into the /code folder and type the following: 
  
```shell
!python stockpredictionwebapp.py
```
    
or run it through the jypyter notebook.  
   
The web application will be available in the browser on the following link:  
  
[URL: http://localhost:5000/](http://localhost:5000/)  
    
A user will be met with a landing page where predictions can be made.  
    
In the input field type a news headline to get a prediction from our model. Examples on a news headline could be:  
  
```shell
Earnings beat NVDA
```  
  
or  
  
```shell
Nvidia Goes Negative
```  
  
The model will then tell you if the stock in focus (NVIDIA) will be red or green on the day.  
  
## Table of Contents for notebook
### Table of Contents
* [1. Environment Setup](#chapter1)
* [2. Import and cleaning of data](#chapter2)

    * [2.1. Ticker Dataset](#chapter2.1)
        * [2.1.1 Describing Dataset](#chapter2.1.1)
        * [2.1.2 Initial cleaning of Dataset](#chapter2.1.2)
        * [2.1.3 Exploring & visualizing the data](#chapter2.1.3)
            * [2.1.3.1 Correlation & Heatmap](#chapter2.1.3.1)
            * [2.1.3.2 Pairplots](#chapter2.1.3.2)
            * [2.1.3.3 Histograms & Boxplots](#chapter2.1.3.3)
            * [2.1.3.4 Exploring volume and close columns](#chapter2.1.3.4)
            * [2.1.3.5 Exploring volume and close columns](#chapter2.1.3.5)
        * [2.1.4 Preperation for machine learning](#chapter2.1.4)
        
     * [2.2. News Dataset](#chapter2.2)
        * [2.2.1 Describing Dataset](#chapter2.2.1)
        * [2.2.2 Initial cleaning of Dataset](#chapter2.2.2)
        * [2.2.3 Exploring & visualizing the data](#chapter2.2.3)
            * [2.2.3.1 Date column](#chapter2.2.3.1)
            * [2.2.3.2 Stock Column](#chapter2.2.3.2)
            * [2.2.3.3 Nvda Stock](#chapter2.2.3.3)
        * [2.2.4 Preperation for machine learning](#chapter2.2.4)
            * [2.2.4.1 Visualizing with Kmeans & PCA](#chapter2.2.4.1)
            
     * [2.3. Combining Dataset](#chapter2.3)
         * [2.3.1 First Combined Dataset](#chapter2.3.1)
             * [2.3.1.1 Making a pandas profiling report for the combined data set one](#chapter2.3.1.1)
         * [2.3.2 Second Combined Dataset](#chapter2.3.2)
             * [2.3.2.1 Making a pandas profiling report for the combined data set two](#chapter2.3.2.1)
         * [2.3.3 Third Combined Dataset](#chapter2.3.3)
             * [2.3.3.1 Making a pandas profiling report for the combined data set one](#chapter2.3.3.1)
         
* [3. Machine Learning](#chapter3)

    * [3.1. Dataset preperation for machine learning](#chapter3.1)
        * [3.1.1 Dataset one preperation](#chapter3.1.1)
            * [3.1.1.1 Data set one vector isolation in numpy](#chapter3.1.1.1)
        * [3.1.2 Dataset two preperation](#chapter3.1.2)
            * [3.1.2.1 Data set two vector isolation in numpy](#chapter3.1.2.1)
        * [3.1.3 Dataset three preperation](#chapter3.1.3)
            * [3.1.3.1 Data set three vector isolation in numpy](#chapter3.1.3.1)
    
    * [3.2. K-means](#chapter3.2)
        * [3.2.1 Theory](#chapter3.2.1)
        * [3.2.2 Machine Learning Dataset One](#chapter3.2.2)
            * [3.2.2.1 Training the model](#chapter3.2.2.1)
            * [3.2.2.2 Scoring the model](#chapter3.2.2.2)
            * [3.2.2.3 Evaluation of the model ](#chapter3.2.2.3)
            * [3.2.2.4 Finding The Optimal K](#chapter3.2.2.4)
            * [3.2.2.5 Visualizing The Result](#chapter3.2.2.5)
         * [3.2.3 Machine Learning Dataset two](#chapter3.2.3)
            * [3.2.3.1 Training the model](#chapter3.2.3.1)
            * [3.2.3.2 Scoring the model](#chapter3.2.3.2)
            * [3.2.3.3 Evaluation of the model ](#chapter3.2.3.3)
            * [3.2.3.4 Finding The Optimal K](#chapter3.2.3.4)
            * [3.2.3.5 Visualizing The Result](#chapter3.2.3.5)  
         * [3.2.4 Machine Learning Dataset three](#chapter3.2.4)
            * [3.2.4.1 Training the model](#chapter3.2.4.1)
            * [3.2.4.2 Scoring the model](#chapter3.2.4.2)
            * [3.2.4.3 Evaluation of the model ](#chapter3.2.4.3)
            * [3.2.4.4 Finding The Optimal K](#chapter3.2.4.4)
            * [3.2.4.5 Visualizing The Result](#chapter3.2.4.5)  
         * [3.2.5 Summary](#chapter3.2.5)
    
    * [3.3. K-Nearest Neighbors](#chapter3.3)
        * [3.3.1 Theory](#chapter3.3.1)
        * [3.3.2 Machine Learning Dataset One](#chapter3.3.2)
            * [3.3.2.1 Training the model](#chapter3.3.2.1)
            * [3.3.2.2 Scoring the model](#chapter3.3.2.2)
            * [3.3.2.3 Evaluation of the model](#chapter3.3.2.3)
            * [3.3.2.4 Visualizing The Result](#chapter3.3.2.4)
        * [3.3.3 Machine Learning Dataset two](#chapter3.3.3)
            * [3.3.3.1 Training the model](#chapter3.3.3.1)
            * [3.3.3.2 Scoring the model](#chapter3.3.3.2)
            * [3.3.3.3 Evaluation of the model](#chapter3.3.3.3)
            * [3.3.3.4 Visualizing The Result](#chapter3.3.3.4)
        * [3.3.4 Machine Learning Dataset Three](#chapter3.3.4)
            * [3.3.4.1 Training the model](#chapter3.3.4.1)
            * [3.3.4.2 Scoring the model](#chapter3.3.4.2)
            * [3.3.4.3 Evaluation of the model](#chapter3.3.4.3)
            * [3.3.4.4 Visualizing The Result](#chapter3.3.4.4)
        * [3.3.5 Summary](#chapter3.3.5)

    * [3.4. Guassian Naive Bayes](#chapter3.4)
        * [3.4.1 Theory](#chapter3.4.1)
        * [3.4.2 Machine Learning Dataset One](#chapter3.4.2)
            * [3.4.2.1 Training the model](#chapter3.4.2.1)
            * [3.4.2.2 Scoring the model](#chapter3.4.2.2)
            * [3.4.2.3 Evaluation of the model](#chapter3.4.2.3)
            * [3.4.2.4 Visualizing The Result](#chapter3.4.2.4)
        * [3.4.3 Machine Learning Dataset two](#chapter3.4.3)
            * [3.4.3.1 Training the model](#chapter3.4.3.1)
            * [3.4.3.2 Scoring the model](#chapter3.4.3.2)
            * [3.4.3.3 Evaluation of the model](#chapter3.4.3.3)
            * [3.4.3.4 Visualizing The Result](#chapter3.4.3.4)
        * [3.4.4 Machine Learning Dataset Three](#chapter3.4.4)
            * [3.4.4.1 Training the model](#chapter3.4.4.1)
            * [3.4.4.2 Scoring the model](#chapter3.4.4.2)
            * [3.4.4.3 Evaluation of the model](#chapter3.4.4.3)
            * [3.4.4.4 Visualizing The Result](#chapter3.4.4.4)
        * [3.4.5 Summary](#chapter3.4.5)

    * [3.5. Decision Tree](#chapter3.5)
        * [3.5.1 Theory](#chapter3.5.1)
        * [3.5.2 Machine Learning Dataset One](#chapter3.5.2)
            * [3.5.2.1 Training the model](#chapter3.5.2.1)
            * [3.5.2.2 Scoring the model](#chapter3.5.2.2)
            * [3.5.2.3 Evaluating the model](#chapter3.5.2.3)
            * [3.5.2.4 Visualizing The Result](#chapter3.5.2.4)
        * [3.5.3 Machine Learning Dataset two](#chapter3.5.3)
            * [3.5.3.1 Training the model](#chapter3.5.3.1)
            * [3.5.3.2 Scoring the model](#chapter3.5.3.2)
            * [3.5.3.3 Evaluating the model ](#chapter3.5.2.3)
            * [3.5.3.4 Visualizing The Result](#chapter3.5.3.4)
        * [3.5.4 Machine Learning Dataset Three](#chapter3.5.4)
            * [3.5.4.1 Training the model](#chapter3.5.4.1)
            * [3.5.4.2 Scoring the model](#chapter3.5.4.2)
            * [3.5.4.3 Evaluating the model ](#chapter3.5.4.3)
            * [3.5.4.4 Visualizing The Result](#chapter3.5.4.4)
        * [3.5.5 Summary](#chapter3.5.5)
    * [3.6. Prediction Performance Comparator](#chapter3.6)
        * [3.6.1 Dataset One](#chapter3.6.1)
            * [3.6.1.1 All Zero Prediction - dataset one](#chapter3.6.1.1)
            * [3.6.1.2 All One Prediction - dataset one](#chapter3.6.1.2)
            * [3.6.1.3 Random Prediction - dataset one](#chapter3.6.1.3)
        * [3.6.2 Dataset Two](#chapter3.6.2)
            * [3.6.2.1 All Zero Prediction - dataset two](#chapter3.6.2.1)
            * [3.6.2.2 All One Prediction - dataset two](#chapter3.6.2.2)
            * [3.6.2.3 Random Prediction - dataset two](#chapter3.6.2.3)
        * [3.6.3 Dataset Three](#chapter3.6.3)
            * [3.6.3.1 All Zero Prediction - dataset three](#chapter3.6.3.1)
            * [3.6.3.2 All One Prediction - dataset three](#chapter3.6.3.2)
            * [3.6.3.3 Random Prediction - dataset three](#chapter3.6.3.3)
        * [3.6.4 Summary](#chapter3.6.4)
    * [3.7 Final Summary](#chapter3.7)
* [4. Visualization](#chapter4)
    * [4.1 Setup](#chapter4.1)
    * [4.2 Charting data set one](#chapter4.2)
    * [4.3 Charting with Yahoo Finance](#chapter4.3)
* [5. Deployment of solution](#chapter5)
    * [5.1 Saving the models](#chapter5.1)
    * [5.2 Defining the Flask Server](#chapter5.2)
    * [5.3 Running the application](#chapter5.3)
* [6. Project Conclusion](#chapter6)

## Links to the different stages of the project development
[Stage 1: Foundation of a business case](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE1.md)  
[Stage 2: Data acquisition and exploration](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE2.md)  
[Stage 3: Using the data and the exploration results for building predictive models](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE3.md)  
[Stage 4: Visualization](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE4.md)  
[Stage 5: Exam Project](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE5.md)
