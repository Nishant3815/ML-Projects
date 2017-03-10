# American-Express-Analyze-This- 2016
This was a PAN-IIT data science competition in which I secured 30th rank finally on the leaderboard.The competition was attended by more than 900 students.
Background

The Island of Hoenn is gearing up for upcoming polls. Citizens are waiting with bated breath as news agencies reveal their predictions on which party is likely to emerge victorious. Much to the disappointment of all the citizens, there are discrepancies in these poll predictions amongst news channels. So many inconsistent predictions did not go down well with an inquisitive bunch of students. Wondering how difficult it might be to crack it, comes their 'Eureka' moment. An idea to create their own ‘Start Up’ to analyze poll sentiments and predict the winner. A start up called - Analyze This. They gather data for a sample of citizens of Island of Hoenn and get started. Information on historical voting pattern, rally attendance and demographics is what they have at hand to predict the winner amongst the 5 competing parties.

Can you help these students crack this puzzle? Do you have it in you to start your own Analyze This?

Problem Statement

You have to predict the party for which each citizen will vote for in the upcoming polls. 

Source: https://in.axpcampus.com/AnalyzeThis/campusactivity/problem-statement.php

Data for Analysis

Following files can be downloaded for your analysis. 

1. Training_Dataset.csv: This data has all the information for a sample of citizens. The information includes: 
    a. Past history of voting for all citizens 
    b. Who they will vote for in upcoming polls 
    c. Donation, Rally Attendance 
    d. Demographics of these citizens 

2. Leaderboard_Dataset.csv: This data has information on the historical vote for a different set of citizens, along with donation, rally attendance and demographics. The vote in the upcoming polls is not present in the data. 

3. Final_Dataset.csv: This data has information on the historical vote for a different set of citizens, along with donation, rally attendance and demographics. The vote in the upcoming polls is not present in the data. 

4. Data_Dictionary.xlsx: This sheet will give you the description of all the variables contained in the 3 datasets above. 

Please note that you can make multiple submissions corresponding to the Leaderboard Dataset. However, for the Final dataset you can submit only one solution. For further details, please refer to the submission guidelines document available at the link below: http://in.axpcampus.com/AnalyzeThis/campusactivity/guidelines-and-submission.php 


Tips on Data Analysis

Following are some tips for the uninitiated on how you can approach this data analysis game. 
Any exercise in the field of data analytics would start with understanding the data. So, start off by understanding the datasets and descriptions provided to you. 
Once you are familiar with the data, try to answer these questions: 
    1. What all data do I have? 
    2. What all data is useful and what is junk? 
    3. How can I organize this data to solve my problem? 


Then, try to build the variables on the training dataset, define dependent and independent variables and then start modeling on the Training Dataset. You need to match the citizen’s choice of vote. 

Once you are satisfied with your model, use it on the Leaderboard dataset and come up with your estimates of poll results for each citizen. Follow the submission guidelines and upload your estimates. Your submission will be evaluated in real time and you can compare how well you have estimated against other participants. 

Keep fine tuning your estimates by trying to increase your leader board scores. Once satisfied, use the same logic to estimate the vote preference of citizens in the final dataset. 

You can use any tool, write your own algorithms, and implement any predictive modeling/Data analysis methods you may want to. For your final submission, you will have to provide details of the techniques you have used. 


Evaluation Criteria

Leader board Submission 
The dataset for Leader board evaluation would be evaluated on the basis of the estimation that you provide. The score is calculated as: 
    a. If Actual Vote = Predicted Vote and Actual Vote = Historical Vote, then score = 50 
    b. If Actual Vote = Predicted Vote and Actual Vote ^= Historical Vote, then score = 100 
    c. If Actual Vote ^= Predicted Vote and Actual Vote = Historical Vote, then score = 0 
    d. If Actual Vote ^= Predicted Vote and Actual Vote ^= Historical Vote, then score = -50 

Your final score will depend on the following parameters: 
    1. 20% weight for highest score achieved on LeaderBoard submission 
    2. 60% weight for score achieved on Final Dataset 
    3. 20% weight for the technique(s) chosen and the associated reasons for the same.
