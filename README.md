**1. Project Overview**

This project implements a feature store using Feast for a Curriculum-Industry Skill Gap dataset.

The objective is to demonstrate how student-related features can be prepared, registered, retrieved, and served using a feature store. The project covers feature engineering, entity creation, data source configuration, FeatureView creation, historical feature retrieval, materialization, online feature retrieval, and machine learning prediction.

The final model predicts the student's Employability Level based on curriculum, technical skills, soft skills, assessments, and industry-readiness features.

**2. Dataset Description**

The dataset used in this project is:

Curriculum_Industry_Readiness_Employability(4519).xlsx

The sheet used for the implementation is:

Balanced_Skill_Alignment

The dataset contains 1000 student records and 28 columns.

The dataset provides information about academic performance, technical skills, soft skills, projects, internships, certifications, coding assessment, aptitude score, resume score, mock interview performance, curriculum coverage, industry-required skills, skill gap, industry readiness, employability score, and employability level.

**3. Problem Statement**

The main problem addressed by this project is identifying the gap between students' curriculum-based skills and the skills expected by industry.

Students may perform well academically but may still have gaps in technical skills, soft skills, practical experience, communication, problem solving, or interview readiness.

This project uses student skill and readiness information to create machine-learning features and predict the student's overall employability level.

**4. Objectives**

The objectives of this project are:

To preprocess the Curriculum-Industry Skill Gap dataset.
To perform feature engineering.
To create a Feast entity for students.
To configure a Feast data source.
To create a Feast FeatureView.
To register the feature definitions using feast apply.
To retrieve historical features for machine learning.
To materialize features into the online store.
To retrieve online features.
To train a machine learning model.
To predict the Employability Level of students.
To demonstrate the complete offline-to-online feature store workflow.

**5. Feature Engineering**

Feature engineering is performed to transform the raw dataset into useful machine-learning features.

**5.1 Technical Skill Average**

The technical skill average is calculated using Programming, DSA, DBMS, Web Development, AI/ML, Cloud, and Cybersecurity.

Technical Skill Average = (Programming + DSA + DBMS + Web Development + AI/ML + Cloud + Cybersecurity) / 7

This feature represents the student's overall technical skill level.

**5.2 Soft Skill Average**

The soft skill average is calculated using Communication, Problem Solving, and Teamwork.

Soft Skill Average = (Communication + Problem Solving + Teamwork) / 3

This feature represents the student's overall soft-skill capability.

**5.3 Career Readiness Average**

The career readiness average is calculated using Coding Assessment, Aptitude Score, Resume Score, and Mock Interview.

Career Readiness Average = (Coding Assessment + Aptitude Score + Resume Score + Mock Interview) / 4

This feature represents the student's overall career readiness.

**5.4 Internship Encoding**

The Internship column contains categorical values such as Yes and No.

These values are converted into numerical values:

Yes = 1

No = 0

The resulting feature is called internship_encoded.

**6. Feast Entity**
The entity used in this project is:

Entity Name: student

Join Key: Student_ID

The student entity represents an individual student.

Student_ID is used as the unique identifier to associate the student's features with the correct student.

**7. Feast Data Source**

The engineered feature data is stored in Parquet format.

Data source:

data/student_features.parquet

The Feast data source uses event_timestamp and created_timestamp.

The event timestamp represents when the feature information was available.

**8. Feast FeatureView**

The FeatureView created in this project is:

student_skill_features

The FeatureView stores the features required for student employability prediction.

The features stored in the FeatureView are:

CGPA – Student's academic performance.

Attendance – Student attendance.

Programming_Skill – Programming ability.

DSA_Skill – Data Structures and Algorithms ability.

DBMS_Skill – Database Management Systems knowledge.

Web_Development – Web development ability.

AI_ML_Skill – Artificial Intelligence and Machine Learning skill.

Cloud_Skill – Cloud computing skill.

Cybersecurity_Skill – Cybersecurity knowledge.

Communication – Communication ability.

Problem_Solving – Problem-solving ability.

Teamwork – Teamwork ability.

Projects – Number of projects completed.

internship_encoded – Internship status converted into numerical form.

Certifications – Number of certifications.

Coding_Assessment – Coding assessment performance.

Aptitude_Score – Aptitude performance.

Resume_Score – Resume quality score.

Mock_Interview – Mock interview performance.

Curriculum_Coverage – Percentage of curriculum covered.

Industry_Required_Skill – Skill level required by industry.

Skill_Gap – Gap between student skills and industry requirements.

Industry_Readiness – Overall industry readiness.

technical_skill_average – Average technical skill score.

soft_skill_average – Average soft skill score.

career_readiness_average – Average career readiness score.

**9. Feature Service**

The Feature Service created for this project is:

student_employability_service

It contains the student_skill_features FeatureView.

The Feature Service provides a consistent group of features for model training and prediction.

**10. Feast Architecture**

The overall workflow of the project is:

 Curriculum-Industry Skill Gap Dataset

            ↓

    Data Preprocessing

            ↓

    Feature Engineering

            ↓

    Student Feature Dataset

            ↓

    Feast Data Source

            ↓

       FeatureView

            ↓

 Historical Feature Retrieval / Materialization

            ↓

   Model Training / Online Store

            ↓

    Online Feature Retrieval

            ↓

    Employability Prediction

**11. Offline Store**

The offline store contains historical feature data.

In this project, the feature data is stored in:

data/student_features.parquet

The offline store is used for historical feature retrieval, creating the training dataset, training the machine learning model, and accessing historical feature values.

**12. Online Store**

The online store contains feature values required for online prediction.

SQLite is used as the online store in this local Feast implementation.

The workflow is:

Offline Store → Materialization → SQLite Online Store → Online Feature Retrieval

**13. Purpose of feast apply**

The command:

feast apply

is used to register and apply the Feast definitions.

It registers components such as the Entity, Data Source, FeatureView, and Feature Service.

The command applies the feature-store configuration and definitions to the Feast registry.

**14. Historical Feature Retrieval**

Historical features are retrieved using Feast's get_historical_features() method.

Historical retrieval is used to create the feature dataset required for machine-learning model training.

The historical retrieval process combines the student entity information, timestamps, and registered Feast features.

**15. Machine Learning Model**

A Decision Tree Classifier is used for predicting the student's Employability Level.

The target variable is:

Employability_Level

The target contains three classes:

Low

Medium

High

The historical features retrieved from Feast are used as input to the machine-learning model.

**16. Model Training**

The dataset is divided into training and testing datasets using an 80:20 split.

Training Data: 80%

Testing Data: 20%

The Decision Tree Classifier is trained using the historical features retrieved from Feast.

**17. Model Accuracy**

The Decision Tree model achieved approximately 99.5% accuracy in the reproduced implementation.

The final accuracy should be verified from the output of the final notebook execution.

**18. Materialization**

Materialization transfers historical feature values from the offline store to the online store.

The process is:

 Parquet Offline Store

         ↓

 Materialization

         ↓

 SQLite Online Store

After materialization, the latest feature values can be retrieved quickly for prediction.

Example command:

feast materialize 2026-01-01T00:00:00 2026-01-01T00:16:40

**19. Online Feature Retrieval**

Online features are retrieved using get_online_features().

This retrieves the latest available features for the selected student from the online store.

For example, features can be retrieved using Student_ID such as CSE1025.

**20. Final Prediction**

The online feature values are passed to the trained machine-learning model.

Example:

Student ID: CSE1025

Predicted Employability Level: High

The model predicts one of the following:

Low

Medium

High

**21. Difference Between Original Dataset and Feature Dataset**

The original dataset contains complete student-related information including academic performance, technical skills, soft skills, projects, internships, certifications, assessments, industry requirements, recommendations, employability score, and employability level.

The feature dataset is a cleaned and transformed version of the original dataset. It contains the features required for machine learning and Feast retrieval, along with the required timestamps.

Feature engineering is also performed to create additional features such as Technical Skill Average, Soft Skill Average, Career Readiness Average, and Internship Encoded.

The target variable Employability_Level is used separately as the prediction label.

**22. Advantages of Using Feast**

Using Feast instead of manually calculating features separately provides several advantages:

Features can be defined and managed centrally.
The same features can be reused during training and prediction.
Historical feature retrieval is supported.
Online feature retrieval is supported.
It reduces inconsistencies between training and serving.
It reduces duplicate feature-engineering code.
It provides a structured feature-store workflow.

**23. Limitations**
    
Limitation 1: Dataset Limitations

The dataset contains a limited number of student records and may not fully represent students from every institution, academic background, or industry.

Limitation 2: Missing Values

The dataset contains missing values in several attributes. These values require preprocessing and imputation before using the data for machine learning.

**24. Future Improvements**

The feature store can be improved when additional curriculum and industry evidence becomes available.

**24.1 Real Industry Data**

Future versions can include real job descriptions, company skill requirements, job postings, industry-specific skills, and recruitment requirements.

**24.2 Real Placement Data**

The system can be improved by adding placement results, interview outcomes, job offers, internship performance, and actual employment outcomes.

**24.3 Time-Based Student Features**

Student skills can be tracked across multiple semesters:

Semester 1 → Semester 2 → Semester 3 → Semester 4 → Final Year

This would allow the feature store to track how student skills change over time.

**25. Project Structure**

The project repository contains the following files:

README.md

feature_store.yaml

features.py

requirements.txt

data/student_features.parquet

notebooks/Feast_SkillGap.ipynb

outputs/historical_features.csv

outputs/online_predictions.csv

**26. How to Run the Project**

**Step 1:** Clone the repository.

git clone https://github.com/Ruchitha-2005/231FA04519-MLOps-Feast-SkillGap

**Step 2:** Open the project directory.

cd <RegisterNumber>MLOps-Feast-SkillGap

**Step 3:** Install the required packages.

pip install -r requirements.txt

**Step 4:** Prepare the feature dataset.

Run the preprocessing and feature-engineering code to create:

data/student_features.parquet

**Step 5:** Apply Feast.

feast apply

**Step 6:** Retrieve historical features using get_historical_features().

**Step 7:** Train the Decision Tree Classifier.

**Step 8:** Materialize the features.

feast materialize 2026-01-01T00:00:00 2026-01-01T00:16:40

**Step 9:** Retrieve online features using get_online_features().

**Step 10:** Use the retrieved features to predict the Employability Level.

**27. Results**

The project demonstrates successful historical feature retrieval using Feast.

Feature engineering creates technical skill, soft skill, and career readiness features from the original dataset.

A Decision Tree Classifier is used to predict Employability Level.

The reproduced implementation achieved approximately 99.5% accuracy.

Online student features can be retrieved from the SQLite online store after materialization.

Example final prediction:

Student ID: CSE1025

Predicted Employability Level: High

**28. Conclusion**

This project demonstrates the use of Feast as a feature store for a Curriculum-Industry Skill Gap dataset.

The project performs data preprocessing and feature engineering and creates reusable student features. Feast is used to define the student entity, register the data source, create the FeatureView, retrieve historical features, materialize features into the online store, and retrieve online features for prediction.

A Decision Tree Classifier is trained using the historical features and predicts the student's Employability Level as Low, Medium, or High.

The project demonstrates how a feature store can provide a consistent and reusable feature pipeline for both machine-learning training and online prediction.

**29. Author**

**Name:** Tiyyagura Ruchitha

**Course:** B.Tech – Computer Science Engineering

**University:** Vignan's Foundation for Science, Technology and Research (VFSTR)

**Project:** Curriculum-Industry Skill Gap Feature Store Using Feast
