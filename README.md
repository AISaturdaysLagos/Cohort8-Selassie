# Diabetes Risk Prediction 
 
According to the World Health Organization, the number of people with diabetes has risen from 108 million in 1980 to over 422 million in 2014. This number is expected to continue rising, making it one of the most pressing public health challenges of the 21st century.
Diabetes is a chronic health condition characterized by elevated blood sugar levels resulting from the body's inability to produce enough insulin or effectively use the insulin it produces. There are two main types of diabetes: Type 1, which is an autoimmune condition where the body attacks and destroys its insulin-producing cells, and Type 2, which is often linked to lifestyle factors such as diet and exercise.

Diabetes Risk Prediction is a machine-learning application that predicts the risk of an individual being diabetic or not. A user can enter their information such as gender, age, BMI, cholesterol level, and others to get a prediction about their diabetes risk level.

The project methodology included

- Data Collection: The dataset was sourced from Kaggle(looking to link the original data source)
- Data preprocessing and cleaning: In this step, the dataset was transformed and cleaned to fix data inconsistencies such as missing values and outliers, preparing the data for further analysis.
- Model training: The cleaned data was passed into the random forests algorithm to learn patterns from the data in order to make predictions on unseen data.
- Model Evaluation: After training the model, the model was evaluated  with the accuracy metric and confusion matrix to check the performance of the model on unseen data.
- Model Deployment: The model was deployed as a web application on Streamlit.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/AISaturdaysLagos/Cohort8-Selassie.git
   ```
2. Navigate to the project directory:
   ```
   cd Cohort8-Selassie
   ```
3. Setup a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate (Linux/Mac) # On Windows use venv\Scripts\activate 
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Acknowledgments
Pandas
Matplotlib
Scikit-learn

We are grateful to our mentor, Seun Ajayi, for his guidance and support throughout the Cohort.

## Contact
Funbi Bolarinwa

Ebunoluwa Amoo

Ayodeji Adesegun

Abraham Ugwa

Oyindamola Olatunji




