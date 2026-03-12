from week2.project.EDA import survival_by_class
from pandas._libs.tslibs.offsets import YearOffset
Titanic Dataset EDA report
1. Overview of the dataset
    -Dataset contains 891 rows and 12 columns
    -missing values in Age(filled with median age) and Embarked columns(filled with mode)

2. Key Insights
    -Survival Rates are highest for first-class passengers(62%) and lowest for both second and third-class passengers(24%)
    -Majority of passegenrs are aged between 20-40 Years
    -A positive correlation exists between fare and survival_by_class

3.Visual Insights:
    -Screenshots of plots