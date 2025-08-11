## 📁 Overview
This project analyzes Bangalore Metropolitan Transport Corporation (BMTC) bus route data to classify routes into predefined categories (Ordinary, Express, AC, etc.) and generate operational insights for route optimization and fleet management.
The solution integrates data cleaning, machine learning classification, and Power BI visualization to provide transport planners with actionable, data-backed recommendations.

## 📁 Contents

- `BMTC_Route_Prediction.ipynb`: Jupyter notebook with full data cleaning, feature engineering, model training, and export steps. https://github.com/Rimpa1999/BMTC-Bus-Route-Analysis-Prediction-Dashboard/blob/main/BMTC_Route_Prediction.ipynb
- `final_routes_data.csv`: Cleaned and enriched dataset used in Power BI.
- `BMTC_Dashboard.pbix`: Interactive Power BI dashboard with insights. [(https://github.com/Rimpa1999/BMTC-Bus-Route-Analysis-Prediction-Dashboard/blob/main/BMTC_Route_Analysis.pbix)] 
- `routes.csv`, `stops.csv`, `stop_times.csv`, `trips.csv`: Raw BMTC GTFS datasets.
  ## 📍 Data Source

Data is publicly available from the Kaggle:https://github.com/Rimpa1999/BMTC-Bus-Route-Analysis-Prediction-Dashboard/blob/main/bmtc_route_prediction_powerbi.py   
routes.txt – route IDs, short names, long names, route type.
trips.txt – trip IDs, route IDs, service IDs.
stops.txt – stop IDs, names, locations.
stop_times.txt – stop sequences, arrival/departure times.
 
  ## Business Problem
BMTC’s planning team lacked a centralized system to:
Classify routes based on service characteristics.
Identify underperforming or overlapping routes.
Make data-driven decisions on fleet allocation and scheduling.
This project delivers an end-to-end analytical solution to address these needs.

  ## Objectives
Merge multiple GTFS datasets (stops, trips, routes, schedules) into a clean, unified dataset.
Engineer features such as total stops, trip frequency, average trip time.
Build and evaluate machine learning models for route classification.
Develop a Power BI dashboard for decision-makers to explore operational KPIs.

  ## Tech Stack
Languages: Python, SQL
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Visualization: Power BI
Data Handling: CSV/GTFS format processing in Pandas

 ## Workflow
flowchart LR
A[Import GTFS datasets] --> B[Data Cleaning & Merging]
B --> C[Feature Engineering]
C --> D[EDA & Visualization]
D --> E[Model Training & Evaluation]
E --> F[Export Predictions]
F --> G[Power BI Dashboard]

 ## Approach
** 1. Data Preparation**
Imported GTFS data files.
Removed duplicates and handled missing values.
Converted time columns to datetime format.
Engineered additional features:
Number of stops per route.
Average trip duration.
Service frequency.

**2. Exploratory Data Analysis (EDA)**
Distribution of routes by type.

Correlation between route length and trip time.

Stop density heatmaps.

**3. Model Building**
Tested models: Logistic Regression, Random Forest, SVM.

Random Forest performed best:

Accuracy: 92%

F1 Score: 0.91

**4. Dashboard Development**
Created an interactive Power BI dashboard showing:
Route type distribution.
Peak vs. off-peak utilization.
Geographic route coverage.
Efficiency KPIs.

## Key Insights
Express routes were underutilized during non-peak hours.
Several Ordinary routes had high overlap, increasing operational costs.
IT corridor routes had the highest weekday demand.

 ## Business Recommendations
Reduce Express route frequency during off-peak hours to save costs.
Merge overlapping Ordinary routes to optimize fleet usage.
Increase service frequency for high-demand IT corridor routes.


## Impact
Centralized dashboard for planners to monitor KPIs in real-time.
Data-driven decisions to optimize schedules, reduce fuel consumption, and improve service coverage.
Framework can be extended to real-time GTFS feeds for live route classification.

## How to Run
Clone the repository:
git clone https://github.com/yourusername/BMTC-Bus-Route-Analysis-Prediction.git
cd BMTC-Bus-Route-Analysis-Prediction
Install dependencies:
pip install -r requirements.txt
Run preprocessing and model training:
python bmtc_analysis.py
Open the Power BI dashboard file: BMTC_Dashboard.pbix

## Screenshots
Power BI Dashboard
<img width="1321" height="742" alt="image" src="https://github.com/user-attachments/assets/95398710-a29a-4fbe-84c3-8e90ba475192" />

## Author
Rimpa Das
📧 rimpadas93828@gmail.com
🔗 LinkedIn | GitHub


