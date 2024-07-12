# The Impact of Food Waste and Emissions on the Environment :herb:

## Table of Contents

- [Project Context](#project-overview)
- [Introduction](#introduction)
- [Hypotheses](#hypotheses)
- [Visualizations](#visualizations)
- [Datasets used and useful links](#datasets-used-and-useful-links)



### Project Context:

- The global food supply chain is a complex system that involves various stages from production to consumption. Each stage of the supply chain, including farming, processing, transportation, retail, and consumption, is associated with food loss and waste. This wastage not only represents a loss of valuable resources but also contributes significantly to greenhouse gas emissions, impacting the environment and sustainability efforts.

### Introduction:

- This project aims to tackle the critical issue of food waste and emissions throughout the food supply chain. By addressing food waste, we can make significant strides in reducing environmental impact, conserving resources, improving food security and fighting worldwide hunger.

- The main objective is to identify critical stages in the food chain where interventions can significantly reduce waste and emissions, thereby enhancing sustainability practices within the industry.


## Hypotheses :bulb:

**1️⃣ Hypothesis**
- Retail and wholesales market activities are the value chain stage that most contribute to food loss and corresponding emissions;

**2️⃣ Hypothesis**
- Different commodities have loss percentages across different stages, indicating potential inefficiencies specific to each stage;

**3️⃣ Hypothesis**
- Emissions reduction potential by targeting specific supply chain stages-



## Visualizations :chart_with_upwards_trend: 



### **EDA - 1️⃣ Hypothesis**

**Variables used:**

-loss_percentage;
-food_supply_stage;
-emissions_quantity.


![Data Visualization](EDA/EDA_visualizations/Countplot1.png)
*Countplot with the Average Loss Percentage by Stage*

![Data Visualization](EDA/EDA_visualizations/Stackedplot1.png)
*Stacked plot to better visualize the total emissions that go to waste because of the food loss*

![Data Visualization](EDA/EDA_visualizations/pivottable2.png)
*Pivot table used to obtain the values used in the stacked plot*



### **EDA - 2️⃣ Hypothesis**

**Variables used:**

-loss_percentage;
-food_supply_stage; 
-commodity.


![Data Visualization](EDA/EDA_visualizations/plotyexpress2.png)
*Interactive countplot to display the Average loss percentage by Commodity and Stage (Only work in the notebook)*

![Data Visualization](EDA/EDA_visualizations/heatmap2.png)
*Heatmap to better visualize where we have loss percentage incidence on the Commodity and Stage*

![Data Visualization](EDA/EDA_visualizations/Sunburstt2.png)
*Interactive Sunburst to showcase the relations between the two categorical variables, where through interactivity we can see the values*



### **EDA - 3️⃣ hypothesis**

**Variables used:**

-country (top10, by avg emission);
-food_supply_stage;
-emissions_quantity (mean).


![Data Visualization](EDA/EDA_visualizations/barpllot3.png)
*Bar plot with Mean Emissions er Crucial Stage*

![Data Visualization](EDA/EDA_visualizations/Barplotw:mean3.png)
*Countplot with the total Emissions per Stage and Country, with the means of each Stage to give depth to the analysis*



### Datasets used and useful links 

**Datasets:**
- [Food Waste FAO dataset](https://www.fao.org/platform-food-loss-waste/flw-data/en/)
- [Emissions FAO dataset](https://www.fao.org/faostat/en/#data/GT)

**Kaban and presentation:**
- [Notion Project Management](https://cactus-burrito-0dd.notion.site/The-Impact-of-Food-Waste-and-Emissions-on-the-Environment-aadb3a283d5743d09389e524ca726f27)
- [Project Presentation Google Slides](https://docs.google.com/presentation/d/19tk_YzKpnB7Ru_O-JEV524FCq9pPl2yMXOzMO9t66sM/edit?usp=sharing)

**Credits:**
- [Alexandre Ribeiro Linkedin](https://www.linkedin.com/in/alexandre-ribeiro-264445279/) :man_cook:
- [José Pedro Brandão Linkedin](https://www.linkedin.com/in/jos%C3%A9-pedro-barbosa-brand%C3%A3o-663a172b6/) :man_cook:














































