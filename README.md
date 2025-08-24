# Project Title
Understanding the Impact of Trading Volume on Short‑Term Market Price Movements

## Problem Statement
Understanding what makes stock prices go up or down is very important for making smart investment decisions. One factor that might affect prices is trading volume,the number of shares bought and sold in a day. Higher or lower trading volume could sometimes signal short-term price changes, but this relationship is not always clear and can vary between assets.

This project looks at how daily changes in trading volume affect short-term returns of a major market index, using historical data from April 2018 to March 2023. Using the Yahoo Finance dataset, we will measure how much and in what direction trading volume affects prices, and whether the effect happens immediately or with a delay. The results will help investors understand real patterns versus random price movements, so they can make better trading decisions.

The analysis concluded that there is no statistically significant or practically useful relationship between daily volume changes and the next day's price returns or volatility. The findings suggest that, for this dataset, daily trading volume is not a reliable standalone indicator for making short-term trading decisions.

## Stakeholder & User
Primary Stakeholders: Retail investors, financial analysts, portfolio managers

End Users: Retail investors (seek simplified, evidence-based insights for regular trades)

Financial analysts/portfolio managers — require statistically robust findings for strategy design and risk assessment.

## Useful Answer & Decision
Type of Answer: Primarily descriptive and causal, with an optional predictive component.

Metric Deliverables:
- Correlation coefficient between daily volume change and daily return.
- Regression statistics (slope, p-value, R²) to assess relationship strength.
  
Artifact Deliverables:
- Scatter plots and time series visualizations of volume vs. returns.
- Summary table of statistical test results.

## Assumptions & Constraints
Assumptions:

- Historical daily Open, High, Low, Close, Adjusted Close, and Volume data is accurate and complete for 2018–2023.

- Trading volume is recorded consistently across the dataset with no structural breaks.

- Market conditions during the sample period are representative of typical trading environments.

Constraints:

- Dataset granularity is daily; intraday patterns cannot be studied.

- Single asset / index focus may not generalize to all securities.

- Analysis must run efficiently in a lightweight computing environment (laptop).

## Known Unknowns / Risks
The detected relationship might be statistically weak or insignificant.
External macroeconomic or geopolitical events may confound observed relationships.
Stock market trends can change over time, making historical relationships less predictive for the future.
Lag effects beyond 1–2 days could exist but are not captured in our initial scope.

## Lifecycle Mapping
Goal → Stage → Deliverable

Identify key volume–price relationship → Stage 01: Problem Framing & Scoping → Problem statement, stakeholder memo, project plan.

Quantify and visualize relationship → Stage 02: Data Exploration & Analysis → Descriptive metrics and scatter plots.

Assess predictive potential → Stage 03: Modeling → Regression/causality models with performance evaluation.

Summarize insights for stakeholders → Stage 04: Reporting → Visual dashboards, interpretive report. 

## Repo Plan
/data/        # Raw and cleaned Yahoo Finance dataset  
/src/         # Scripts for preprocessing, analysis, plotting  
/notebooks/   # Jupyter notebooks for exploration and model building  
/docs/        # Stakeholder-facing artifacts (e.g., memo, framing slide)

## Project Overview & Methodology
The project's objective was to determine if daily changes in trading volume could reliably predict the direction or magnitude of the next day's price movement. The methodology involved several key stages:

Data Ingestion & Cleaning: Historical daily data (Open, High, Low, Close, Volume) was loaded, cleaned, and processed for analysis.

Feature Engineering: Key metrics were engineered from the raw data, including:

- Daily Return (%): The daily percentage change in the closing price.

- Volume Change (%): The daily percentage change in trading volume.

- Volatility (%): The daily price range as a percentage of the closing price.

- Modeling & Analysis: Three primary experiments were conducted to test the hypothesis:

Experiment 1 (Regression): 

A linear regression model was built to predict Daily Return using the previous day's Volume Change.

Experiment 2 (Advanced Regression):

A second regression model was built using a "smarter" feature that compared the daily volume to its 50-day moving average.

Experiment 3 (Classification): 

A logistic regression model was trained to predict whether the next day would be a "high volatility" or "low volatility" day based on the previous day's Volume Change.

## Key Findings & Evidence
Across all three experiments, the results consistently showed a lack of predictive power from the volume-based features.

Finding 1: 

Trading Volume Fails to Predict Price Returns
Both regression models found no meaningful link between volume changes and price returns. The models had an R-squared value near zero, indicating that volume changes explained virtually none of the variation in daily returns. The relationship is visualized in the scatter plot below, which shows no discernible pattern and a flat trendline, confirming the lack of a linear relationship.

Finding 2: 

Trading Volume Fails to Predict Volatility
The classification model, designed to predict whether the next day would be calm or choppy, performed no better than a random guess. The model achieved a final accuracy of 51.65% on unseen test data, which is statistically indistinguishable from a 50% coin flip. This indicates that volume change is not a reliable signal for forecasting periods of high volatility.

## Conclusion & Recommendations

Final Conclusion: The central hypothesis of this project is not supported by the evidence. For the Dow Jones Industrial Average during the period studied, daily changes in trading volume are not a reliable predictor of either short-term price returns or next-day volatility.

## Limitations:

- This analysis was limited to a single market index and may not generalize to individual stocks or other asset classes.

- The use of daily data may miss important intraday relationships between volume and price.

- The models were primarily linear and may not capture more complex, non-linear dynamics.

## Recommendations for Future Work:

- Test the same hypothesis on different assets, such as high-growth tech stocks or cryptocurrencies, which may exhibit different behaviors.

- Explore more complex, non-linear models (e.g., machine learning models like Gradient Boosting or LSTMs) to capture more intricate patterns.

- Incorporate additional data sources, such as market sentiment from news headlines, to potentially improve predictive power.