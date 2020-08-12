#create database object
conn = sl.connect('patient_data.db')
c = conn.cursor()

#create admissions table and populate
admissions = pd.read_csv('ADMISSIONS.csv', index_col=0, encoding='latin-1')

c.execute('CREATE TABLE ADMISSIONS (SUBJECT_ID int, HADM_ID int, ADMITTIME str, DISCHTIME str,DEATHTIME str,ADMISSION_TYPE str, ADMISSION_LOCATION str, DISCHARGE_LOCATION str,INSURANCE str, LANGUAGE str, RELIGION str, MARITAL_STATUS str, ETHNICITY str,EDREGTIME str,EDOUTTIME str,DIAGNOSIS str,HOSPITAL_EXPIRE_FLAG str,HAS_CHARTEVENTS_DATA str)')
conn.commit()

admissions.to_sql('ADMISSIONS',conn, if_exists='replace',index=False)

#create callout table
callout = pd.read_csv('CALLOUT.csv.gz', index_col=0,encoding='latin-1')

c.execute('CREATE TABLE CALLOUT (SUBJECT_ID int,  HADM_ID int,  SUBMIT_WARDID int,  SUBMIT_CAREUNIT str,CURR_WARDID str,  CURR_CAREUNIT str, CALLOUT_WARDID str, CALLOUT_SERVICE str,REQUEST_TELE str, REQUEST_RESP str, REQUEST_CDIFF str, REQUEST_MRSA str,REQUEST_VRE str, CALLOUT_STATUS str, CALLOUT_OUTCOME str, DISCHARGE_WARDID str,ACKNOWLEDGE_STATUS str, CREATETIME str, UPDATETIME str, ACKNOWLEDGETIME str,OUTCOMETIME str,  FIRSTRESERVATIONTIME str,CURRENTRESERVATIONTIME str)')
conn.commit()

callout.to_sql('CALLOUT',conn, if_exists='replace',index=False)

#create CPTEvents table 
CPTevents = pd.read_csv('CPTEVENTS.csv',index_col=1,encoding='latin-1')

c.execute('CREATE TABLE CPTEVENTS (ROW_ID int, HADM_ID int, COSTCENTER str, CHARTDATE str, CPT_CD str, CPT_NUMBER str,CPT_SUFFIX str, TICKET_ID_SEQ str, SECTIONHEADER str, SUBSECTIONHEADER str,DESCRIPTION str)')
conn.commit()

CPTevents.to_sql('CPTEVENTS',conn, if_exists='replace',index=False)

#create D_CPT table
D_CPT = pd.read_csv('D_CPT.csv.gz',index_col=0,encoding='latin-1')

c.execute('CREATE TABLE D_CPT (CATEGORY str, SECTIONRANGE str, SECTIONHEADER str, SUBSECTIONRANGE str,SUBSECTIONHEADER str, CODESUFFIX str, MINCODEINSUBSECTION str, MAXCODEINSUBSECTION str)')
conn.commit()

D_CPT.to_sql('D_CPT',conn, if_exists='replace',index=False)

#create DRGcodes table
DRGcodes = pd.read_csv('DRGCODES.csv.gz',index_col=0,encoding='latin-1')

c.execute('CREATE TABLE DRGCODES (SUBJECT_ID int, HADM_ID int, DRG_TYPE str, DRG_CODE str, DESCRIPTION str,DRG_SEVERITY str, DRG_MORTALITY str)')
conn.commit()

DRGcodes.to_sql('DRGCODES',conn, if_exists='replace',index=False)

#create ICUstay table
ICUstay = pd.read_csv('ICUSTAYS.csv.gz',index_col=0,encoding='latin-1')

c.execute('CREATE TABLE ICUSTAY (SUBJECT_ID int, HADM_ID int, ICUSTAY_ID int, DBSOURCE str, FIRST_CAREUNIT str,LAST_CAREUNIT str, FIRST_WARDID int, LAST_WARDID int, INTIME str, OUTTIME str,LOS str)') 
conn.commit()

ICUstay.to_sql('ICUSTAY',conn, if_exists='replace',index=False)

#create Notes table
notes = pd.read_csv(r'NOTEEVENTS.csv',index_col=0)

c.execute('CREATE TABLE NOTES (SUBJECT_ID int, HADM_ID int, CHARTDATE str, CHARTTIME str, STORETIME str,CATEGORY str, DESCRIPTION str, CGID str, ISERROR str, TEXT str)')
conn.commit()

notes.to_sql('NOTES',conn, if_exists='replace',index=False)

#create patients table
patients = pd.read_csv('PATIENTS.csv.gz',index_col=0,encoding='latin-1')

c.execute('CREATE TABLE PATIENTS (SUBJECT_ID int, GENDER str, DOB str, DOD str, DOD_HOSP str, DOD_SSN str,EXPIRE_FLAG str)')
conn.commit()

patients.to_sql('PATIENTS',conn, if_exists='replace',index=False)

#create services table
services = pd.read_csv('SERVICES.csv.gz',index_col=1,encoding='latin-1')

c.execute('CREATE TABLE SERVICES (ROW_ID int, HADM_ID int, TRANSFERTIME str, PREV_SERVICE str, CURR_SERVICE str)')
conn.commit()

services.to_sql('SERVICES',conn, if_exists='replace',index=False)
