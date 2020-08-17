## This folder houes all data used in this project.  
### The instructions for creating the database can be found in the SQL_tables_setup.jpynb notebook.  
### All .csv files that are generated in the notebooks will be housed here.

#### The data tables used in this project are as follows:

- Admissions - each row in this table is an individual hospital ICU admission.  Patients may have multiple admisions.
- Patients - each row in this table is an individual patient record, this can be linked to the admissions table using the 'subject_id' column in both tables
- Notes - each row in this table contains a set of notes from a patient's ICU stay.  Each admission will have multiple notes.  This table can be linked to the patient table using 'subject_id' and to the admissions table using 'hadm_id'
- dx_icd - each row in this table is one diagnosis code for a patient's admission.  Patients can have multiple diagnosis codes associated with each stay.  This table can be linked to the admissions table using subject_id and hadm_id.