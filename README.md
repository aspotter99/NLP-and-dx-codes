# Using Natural Language Processing to Determine ICD-10 Diagnosis Code
Model and analysis by Amanda S. Potter 

## Table of Contents
- [Repo Structure and Directory](#Repo-Structure-and-Directory)
- [Introduction](#Introduction)
- [Goal](#Goal)
- [Data Set](#Data-Set)
- [Definitions](#Definitions)
- [Methodology](#Methodology)
- [Summary of Model](#Summary-of-Model)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
- [Reproducing this Project](#Reproducing-this-Project)

## Repo Structure and Directory
- [Notebooks](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/Notebooks)
- [Data](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/Data)
- [References](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/References)
- [Reports](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/Reports)
- [src](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/src)
- [Presentation](https://github.com/aspotter99/NLP-and-dx-codes/Reports/Using_NLP_to_Identify_Diagnosis_Codes.pdf)
- [Project Conda Environment](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/NLP.yml)

## Introduction 

Hospitals depend on having accurate medical coding that reflects all events in a patient encounter from the time of admission to discharge.  Coding inaccuracies can cause claim denials and result in lost revenue for a hospital.  This is primarily a concern for a hospital's revenue cycle executive.  

## Goal 
This project aims to use Natural Language Processing to correctly predict an ICD-10 code using physician notes from a patient's medical record. 

## Data Set
Data used in this project was obtained from https://mimic.physionet.org

MIMIC-III, a freely accessible critical care database. Johnson AEW, Pollard TJ, Shen L, Lehman L, Feng M, Ghassemi M, Moody B, Szolovits P, Celi LA, and Mark RG. Scientific Data (2016). DOI: 10.1038/sdata.2016.35. Available from: http://www.nature.com/articles/sdata201635

Additional information on the specific data used for this project is outlined [here](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/Data/README.md)

## Definitions
- Medical Record: A complete recording of an individual patient's key clinical data and medical history.  This includes demographics, vital signs, diagnoses, procesured, medications, treatment plans, notes, diagnostic tests, immunizations, etc.
- Medical Coding:  Transformation of clinical data from sources such as physician notes into universal alphanumeric codes.  The currently used code set is ICD-10. 
- ICD:  nternational Classification of Diseases and is the global health information standard for mortality and morbidity statistics.
- DRG: A diagnosis-related group (DRG) is a patient classification system that standardizes prospective payment to hospitals and encourages cost containment initiatives. In general, a DRG payment covers all charges associated with an inpatient stay from the time of admission to discharge. (hmsa.com)

## Methodology
This project will utilize Natural Language Processing and a Naive Bayes Multinomial classification algorithm.  
The dataset was labeled with both a diagnosis and a diagnosis code which were used in the initial models.  Text of physician notes from a patient was processed and used to train and predict the correct diagnosis/diagnosis code.

Because we are concerned with accurately predicting both of the diagnosis codes, the model will use accuracy to evaluate performance.

## Model Summary 
The first model was built using two diagnoses (GASTROINTESTINAL BLEED and INTRACRANIAL HEMORRHAGE).  Using a count vectorizer, the first model performed fairly well, with an accuracy score of .77 - running the model with a tfidf vectorizer instead of a count vectorizer did not improve the accuracy of the model.


The first model used diagnoses that were on the patient admission record, using this with the discharge summary notes resulted in a very accurate model, because the diagnosis was in that discharge summary.  Because of this, 2 ICD-10 codes that related to the initial diagnoses were chosen and then the model was trained using those.  The final model utilizes a count vectorizer and only considers discharge summary notes to identify 2 ICD-10 codes - I61.9 and K92.2.  This binary classification model has an accuracy of .94.


Additional information on model building and iterations can be found [here](Reports/Report_Notebook/MVP_report.ipynb)


## Conclusions and Recommendations 
It is possible to use NLP to identify the correct ICD-10 code from physician discharge summary notes.  
Some next steps would be to bring in additional codes to train and test the model - rarely is medical coding a binary decision.  In addition, this type of processing of physician notes could be used to determine if a DRG should have a CC/MCC - these indicate that a patient had additional underlying conditions that require a higher level of care.  Missing CC/MCC DRG can cost hospitals a great deal of money due to lower reimbursements than were appropriate for the level of care that was received.  

## Reproducing This Project
#### Creating an environment from an environment.yml file
Use the terminal or an Anaconda Prompt for the following steps:

Create the environment from the NLP.yml file:

conda env create -f NLP.yml
The first line of the yml file sets the new environment's name. For details see Creating an environment file manually.
Activate the new environment: conda activate myenv


#### Creating the database:
Information on downloading and creating the database used for this project can be found [here](https://github.com/aspotter99/NLP-and-dx-codes/tree/master/Data/README.md)

