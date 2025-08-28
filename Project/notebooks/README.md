### **Project Overview**
This project analyzes the relationship between daily changes in trading volume and the next day's price returns and volatility for the Dow Jones Industrial Average (DJIA) from April 2018 to March 2023. The goal was to determine if trading volume is a reliable standalone indicator for making short-term trading decisions.

---
### **Key Finding: No Significant Predictive Power** 
The central hypothesis of this project is **not supported by the evidence**. Across multiple regression and classification models, the analysis concluded that daily changes in trading volume are not a reliable predictor of either short-term price returns or next-day volatility for the DJIA during the period studied. The models performed no better than a random baseline, with R-squared values near zero.

### **Project Lifecycle**
This project followed a standard data science lifecycle, from **Scoping** the volume-price relationship to **Deploying** a final, evidence-based conclusion. The ongoing **Monitoring** phase consists of a weekly automated pipeline that re-validates the finding that daily trading volume is not a reliable short-term predictor by checking for any emerging statistical relationships.

---
### **Repository Structure**
* **/data/**: Contains the raw and processed datasets.
* **/notebooks/**: Jupyter notebooks for exploration and final analysis.
* **/src/**: Modular Python scripts for reusable tasks (e.g., feature engineering).
* **/reports/**: Includes a stakeholder-friendly summary of the project findings.S