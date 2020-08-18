### This folder houes all data used in this project.  

# INSTRUCTIONS FOR DOWNLOADING DATA AND SETTING UP SQL FOR THIS PROJECT

- Data can be found at https://physionet.org/content/mimiciii/1.4/

- Researchers are required to formally request access via a process documented on the MIMIC website. There are two key steps that must be completed before access is granted:

- the researcher must complete a recognized course in protecting human research participants that includes Health Insurance Portability and Accountability Act (HIPAA) requirements.

- the researcher must sign a data use agreement, which outlines appropriate data usage and security standards, and forbids efforts to identify individual patients.

- Approval requires at least a week. Once an application has been approved the researcher will receive emails containing instructions for downloading the database from PhysioNetWorks, a restricted access component of PhysioNet. MIMIC-III is a large, freely-available database comprising deidentified health-related data associated with over forty thousand patients who stayed in critical care units of the Beth Israel Deaconess Medical Center between 2001 and 2012. The database includes information such as demographics, vital sign measurements made at the bedside (~1 data point per hour), laboratory test results, procedures, medications, caregiver notes, imaging reports, and mortality (including post-hospital discharge).

- MIMIC supports a diverse range of analytic studies spanning epidemiology, clinical decision-rule improvement, and electronic tool development. It is notable for three factors: it is freely available to researchers worldwide; it encompasses a diverse and very large population of ICU patients; and it contains highly granular data, including vital signs, laboratory results, and medications.

- Johnson, A., Pollard, T., & Mark, R. (2016). MIMIC-III Clinical Database (version 1.4). PhysioNet. https://doi.org/10.13026/C2XW26.
- Johnson, A. E. W., Pollard, T. J., Shen, L., Lehman, L. H., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Celi, L. A., & Mark, R. G. (2016). MIMIC-III, a freely accessible critical care database. Scientific Data, 3, 160035.
- Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

- Once you are granted access to the database, you can download the zip file that contains all of the tables and unzip to the data folder and run the cells in the SQL_tables_setup.jpynb notebook to create the SQL database.


### The instructions for creating the database can be found in the SQL_tables_setup.jpynb notebook.  
### All .csv files that are generated in the notebooks will be housed here.

#### The data tables used in this project are as follows:

- Admissions - each row in this table is an individual hospital ICU admission.  Patients may have multiple admisions.
- Patients - each row in this table is an individual patient record, this can be linked to the admissions table using the 'subject_id' column in both tables
- Notes - each row in this table contains a set of notes from a patient's ICU stay.  Each admission will have multiple notes.  This table can be linked to the patient table using 'subject_id' and to the admissions table using 'hadm_id'
- dx_icd - each row in this table is one diagnosis code for a patient's admission.  Patients can have multiple diagnosis codes associated with each stay.  This table can be linked to the admissions table using subject_id and hadm_id.