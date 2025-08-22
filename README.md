# Car Price Prediction with Machine Learning and GUI
# 📌 Project Overview
This project predicts the price of used cars based on multiple features such as brand, year, mileage, engine size, fuel type, and more.
The workflow of the project includes:
1.	Web Scraping car price data from online sources(https://www.cazoo.co.uk/).
2.	Data Preprocessing & Cleaning to prepare a structured dataset.
3.	Model Training using multiple machine learning models (Linear Regression, Random Forest, Decision Tree, XGBoost).
4.	GUI Application built with CustomTkinter for easy user interaction.
The trained model is deployed inside a desktop application, where users can input car details and instantly get the predicted price.
________________________________________
# 🚀 Features
•	Web scraping pipeline to gather real-world car data.
•	Exploratory Data Analysis (EDA) and feature engineering.
•	Regression models with performance evaluation.
•	Final model deployed with Random Forest Regressor.
•	User-friendly GUI with CustomTkinter:
o	Dropdowns and text fields for input.
o	Predict button to show price instantly.
o	Error handling with clear messages.
________________________________________
# 🛠️ Technologies Used
•	Python 3.12
•	Libraries:
o	pandas, numpy
o	scikit-learn
o	seaborn, matplotlib
o	xgboost
o	joblib
o	customtkinter
o	CTkMessagebox
________________________________________
# 📂 Project Structure
├── createData_WebScraping.ipynb		# Web Scraping and get data of cars
├── clean_datase.ipynb		# Clean all data and split to subgroups
├── finalCarDataset.csv          # Cleaned dataset
├── machineModel_AnalysisData.ipynb  # Jupyter Notebook for model training & evaluation
├── predict_carPrice_ML.ipynb      	# Create RandomForest Model to use
├── random_forest_carPrice.pkl   # Saved trained model
├── predict_carPrice_GUI.py      # GUI application script
└── README.md                    # Project documentation
________________________________________
# ⚙️ Installation & Usage
1.	Clone the repository:
git clone https://github.com/miladsafipy/car-price-prediction.git
cd car-price-prediction
2.	Install required packages:
pip install -r requirements.txt
3.	Run the GUI application:
python predict_carPrice_GUI.py
________________________________________
# 🎮 GUI Preview
•	Select the brand, year, control type, fuel type, location, etc.
•	Enter details like model, mileage, engine size, number of doors, emission.
•	Click Predict Car Price → instantly get the estimated price.
<img width="1149" height="615" alt="git1" src="https://github.com/user-attachments/assets/a2b89653-bbf5-41ce-808b-49c9be81a9a0" />

<img width="1079" height="615" alt="git2" src="https://github.com/user-attachments/assets/caf8d055-11a8-459a-ab00-69273fae6e94" />

________________________________________
📊 Model Performance
•	Random Forest Regressor achieved:
o	R² Score: ~0.84 on test data
o	MAE: ~3172
o	MSE: ~63570496
________________________________________
🔮 Future Improvements
•	Add more data points to improve generalization.
•	Deploy as a web app (Flask/Django + Streamlit).
•	Integrate with real-time scraping for live predictions.
________________________________________
👤 Author
Developed by Milad Safi
A project combining web scraping, machine learning, and GUI development to demonstrate real-world data science applications.

