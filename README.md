# Project Title
Understanding the Impact of Trading Volume on Short‑Term Market Price Movements

## Problem Statement
Understanding what makes stock prices go up or down is very important for making smart investment decisions. One factor that might affect prices is trading volume,the number of shares bought and sold in a day. Higher or lower trading volume could sometimes signal short-term price changes, but this relationship is not always clear and can vary between assets.

This project looks at how daily changes in trading volume affect short-term returns of a major market index, using historical data from April 2018 to March 2023. Using the Yahoo Finance dataset, we will measure how much and in what direction trading volume affects prices, and whether the effect happens immediately or with a delay. The results will help investors understand real patterns versus random price movements, so they can make better trading decisions.

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
