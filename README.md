# Microsoft Security Incident Prediction

This repository contains the code and report for the APA 2024-Q2 machine learning project. The project focuses on predicting cybersecurity incident triage outcomes using Microsoft’s GUIDE dataset — a large collection of real-world cybersecurity incidents that include over 13 million evidence pieces, 1.6 million alerts, and 1 million annotated incidents from more than 6,100 organizations. Our main goal is to aid Security Operations Centers (SOCs) with informed, context-rich recommendations rather than fully automating incident response. By employing machine learning, our models classify incidents into true positive (TP), benign positive (BP), and false positive (FP).

After evaluating multiple models, the Random Forest model was selected for its strong performance and efficiency, recording a precision of 0.84, recall of 0.794, and an F1-score of 0.809. This makes it well-suited for handling the inherent class imbalances in cybersecurity incident data.

## Repository Structure

- **src folder**: Contains two Jupyter notebooks:
  - **DataPreparation.ipynb**: Prepares the data by performing cleaning, feature engineering, and data transformation.
  - **ModelTraining.ipynb**: Trains the machine learning models, evaluates them, and saves the trained models.

- **data folder**: Contains the subset of the Microsoft Incident Prediction dataset (from Kaggle) used in this project.

- **models folder**: Stores the trained models for future use or evaluation.

- **requirements.txt**: Lists the libraries required to run the notebooks.

## How to Run the Notebooks

1. **Install the dependencies:**  
   Run the following command to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Preparation:**  
   Open and run the `DataPreparation.ipynb` notebook to clean, transform, and prepare the dataset.

3. **Model Training:**  
   Open and run the `ModelTraining.ipynb` notebook to train the machine learning models, evaluate their performance, and save the outputs in the models folder.

## Authors
- Muhammad Yasin Khokhar
- Momin Miah Begum

## References
- [GitHub Repository](https://github.com/yasin281/Microsoft-Security-Incident-Prediction)
- [Dataset from Kaggle](https://www.kaggle.com/datasets/Microsoft/microsoft-security-incident-prediction)
