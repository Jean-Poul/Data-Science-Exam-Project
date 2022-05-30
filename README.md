# The Medias Influence On The Stock Market  

This is an exam project for Data Science on CPH Business software developer bachelor.

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Nina Lisakowski, cph-nl163

## Brief introduction:  
Our focus will be to build a model which can analyze if news are negative or positive. The next step will be to evaluate if there is a direct correlation with these news articles and the stock price. We find it interesting to investigate the psychological aspect of news outlets and how they can affect peoples investment choices. Furthermore the stock market is notoriously unpredictable and therefore it is interesting to challange ourselves to build a model that can predict the trends in the market. We expect to find a correlation between news from well established news outlets and with some probability be able to predict the trend of the stock in focus. An end user of our results may be someone who wants to take the first step into investing/trading. Our model could be a tool to help newcommers to establish confidence in their investment/trade.  

## Table of Contents for notebook
* 1 Environment Setup
* 2 Import and cleaning of data

    * 2.1. Ticker Dataset
        * 2.1.1 Describing Dataset
        * 2.1.2 Initial cleaning of Dataset
        * 2.1.3 Exploring & visualizing the data
            * 2.1.3.1 Correlation & Heatmap
            * 2.1.3.2 Pairplots
            * 2.1.3.3 Histograms & Boxplots
            * 2.1.3.4 Exploring volume and close columns
            * 2.1.3.5 Exploring volume and close columns
        * 2.1.4 Preperation for machine learning
        
     * 2.2. News Dataset
        * 2.2.1 Describing Dataset
        * 2.2.2 Initial cleaning of Dataset
        * 2.2.3 Exploring & visualizing the data
            * 2.2.3.1 Date column
            * 2.2.3.2 Stock Column
            * 2.2.3.3 Nvda Stock
        * 2.2.4 Preperation for machine learning
            * 2.2.4.1 PCA
            
     * 2.3. Combining Dataset
         * 2.3.1 First Combined Dataset
         * 2.3.2 Second Combined Dataset
         * 2.3.3 Third Combined Dataset
         
* 3 Machine Learning

    * 3.1. Dataset preperation for machine learning
        * 3.1.1 Dataset one preperation
            * 3.1.1.1 Dataset Isolation in numpy
        * 3.1.2 Dataset two preperation
            * 3.1.2.1 Dataset Isolation in numpy
        * 3.1.3 Dataset three preperation
            * 3.1.3.1 Dataset Isolation in numpy
    
    * 3.2. K-means
        * 3.2.1 Theory
        * 3.2.2 Machine Learning Dataset One
            * 3.2.2.1 Training the model
            * 3.2.2.2 Evaluating the model
            * 3.2.2.3 Estimating the errors in prediction
            * 3.2.2.4 Second run of k-means with a more optimal value of k
            * 3.2.2.5 Conclusion
    
    * 3.3. K-Nearest Neighbors
        * 3.3.1 Theory
        * 3.3.2 Machine Learning Dataset One
            * 3.3.2.1 Training the model
            * 3.3.2.2 Evaluating the model
            * 3.3.2.3 Estimating the errors in prediction
            * 3.3.2.4 Visualizing data
            * 3.3.2.5 Validating with validation set
        * 3.3.3 Machine Learning Dataset two
            * 3.3.3.1 Training the model
            * 3.3.3.2 Evaluating the model
            * 3.3.3.3 Estimating the errors in prediction
            * 3.3.3.4 Visualizing data
            * 3.3.3.5 Validating with validation set
        * 3.3.4 Machine Learning Dataset Three
            * 3.3.4.1 Training the model
            * 3.3.4.2 Evaluating the model
            * 3.3.4.3 Estimating the errors in prediction
            * 3.3.4.4 Visualizing data
            * 3.3.4.5 Validating with validation set
        * 3.3.5 Summary

    * 3.4. Guassian Naive Bayes
        * 3.4.1 Theory
        * 3.4.2 Machine Learning Dataset One
            * 3.4.2.1 Training the model
            * 3.4.2.2 Evaluating the model
            * 3.4.2.3 Estimating the errors in prediction
            * 3.4.2.4 Visualizing data
            * 3.4.2.5 Validating with validation set
        * 3.4.3 Machine Learning Dataset two
            * 3.4.3.1 Training the model
            * 3.4.3.2 Evaluating the model
            * 3.4.3.3 Estimating the errors in prediction
            * 3.4.3.4 Visualizing data
            * 3.4.3.5 Validating with validation set
        * 3.4.4 Machine Learning Dataset Three
            * 3.4.4.1 Training the model
            * 3.4.4.2 Evaluating the model
            * 3.4.4.3 Estimating the errors in prediction
            * 3.4.4.4 Visualizing data
            * 3.4.4.5 Validating with validation set
        * 3.4.5 Summary
    * 3.5. Decision Tree
        * 3.5.1 Theory
        * 3.5.2 Machine Learning Dataset One
            * 3.5.2.1 Training the model
            * 3.5.2.2 Evaluating the model
            * 3.5.2.3 Estimating the errors in prediction
            * 3.5.2.4 Visualizing data
            * 3.5.2.5 Validating with validation set
        * 3.5.3 Machine Learning Dataset two
            * 3.5.3.1 Training the model
            * 3.5.3.2 Evaluating the model
            * 3.5.3.3 Estimating the errors in prediction
            * 3.5.3.4 Visualizing data
            * 3.5.3.5 Validating with validation set
        * 3.5.4 Machine Learning Dataset Three
            * 3.5.4.1 Training the model
            * 3.5.4.2 Evaluating the model
            * 3.5.4.3 Estimating the errors in prediction
            * 3.5.4.4 Visualizing data
            * 3.5.4.5 Validating with validation set
        * 3.5.5 Summary
    * 3.6 Summary

* 4 Visualization
* 5 Project Conclusion

## Links to the different stages of the project development
[Stage 1: Foundation of a business case](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE1.md)  
[Stage 2: Data acquisition and exploration](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE2.md)  
[Stage 3: Using the data and the exploration results for building predictive models](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE3.md)  
[Stage 4: Visualization](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE4.md)
[Stage 5: Exam Project](https://github.com/Jean-Poul/Data-Science-Exam-Project/blob/main/README-STAGE5.md)