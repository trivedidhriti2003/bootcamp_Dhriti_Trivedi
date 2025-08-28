# Lifecycle Framework Guide: Volume-Price Analysis

This document maps the project, "Understanding the Impact of Trading Volume on Short‑Term Market Price Movements," to a standard data science lifecycle framework.

### **Stage 1: Scoping & Problem Framing**
* **Problem Statement**: This project investigated if daily changes in trading volume could reliably predict the direction or magnitude of the next day's price movement for a major market index (DJIA).
* **Stakeholders**: The primary stakeholders are retail investors and financial analysts seeking evidence-based indicators for trading strategies.
* **Hypothesis**: A statistically significant relationship exists between a day's trading volume change and the next day's price return or volatility.

### **Stage 2: Data Acquisition & Preparation**
* **Data Source**: Historical daily stock data (Open, High, Low, Close, Volume) for the Dow Jones Industrial Average (DJIA) was acquired from the Yahoo Finance API.
* **Time Period**: The dataset covered the period from April 2018 to March 2023.
* **Feature Engineering**: Key metrics were engineered from the raw data, including Daily Return (%), Volume Change (%), and Volatility (%). Lagged features were created to associate the previous day's volume with the next day's return.

### **Stage 3: Modeling & Experimentation**
* **Methodology**: Three experiments were conducted to test the hypothesis:
    1.  **Linear Regression**: Modeled next-day `Daily_Return` using the previous day's `Volume_Change`.
    2.  **Advanced Regression**: Used a normalized volume feature (daily volume vs. 50-day moving average) to predict returns.
    3.  **Logistic Classification**: Predicted a binary outcome of "high volatility" vs. "low volatility" day based on volume change.
* **Results**: All experiments failed to support the hypothesis. The regression models yielded an R-squared value near zero, and the classification model's accuracy was 51.65%, statistically indistinguishable from a random guess.

### **Stage 4: Evaluation**
* **Conclusion**: The central hypothesis was not supported by the evidence. The evaluation of the metrics from all three models consistently showed that daily trading volume lacks meaningful predictive power for short-term price movements or volatility for this index in the period studied.
* **Limitations**: The analysis was limited to a single index, used daily (not intraday) data, and focused on linear relationships.

### **Stage 5: Deployment**
* **Deployment Artifact**: The project did not deploy a predictive model. Instead, it "deployed" a strategic conclusion: **the documented finding that daily volume is not a reliable standalone indicator for short-term trading decisions.**
* **Production System**: The system in production is the automated analysis pipeline designed to continuously validate this conclusion.

### **Stage 6: Monitoring & Maintenance**
* **Monitoring Strategy**: The analysis pipeline is designed to run on a weekly schedule.
* **Key Metric**: The primary monitored metric is the **R-squared value** from the regression analysis.
* **Alerting**: An alert is triggered for manual review by an analyst if the 90-day rolling R-squared value rises above a threshold of 0.05, suggesting that a predictive relationship may be emerging due to a market regime change.S