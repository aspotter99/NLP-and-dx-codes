# QUERIES USED IN THIS PROJECT (TO BE FILLED IN ON COMPLETION OF FINAL REPO)


def expanded_notes_data:
    SELECT adm.subject_id, 
        pt.gender,
        adm.insurance,
        adm.language,
        adm.religion,
        adm.marital_status,
        adm.ethnicity,
        adm.hadm_id,
        admission_type,
        admission_location,
        notes.chartdate,
        notes.charttime,
        notes.category,
        notes.description,
        notes.iserror,
        notes.text,
        adm.diagnosis
        FROM admissions as adm
        JOIN notes on adm.subject_id = notes.subject_id
                AND adm.hadm_id = notes.hadm_id
        JOIN patients pt on adm.subject_id = pt.subject_id
        WHERE adm.diagnosis in ('GASTROINTESTINAL BLEED','INTRACRANIAL HEMORRHAGE') 
        ORDER BY adm.subject_id, adm.hadm_id, chartdate
        
