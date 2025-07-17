import json
import requests
import os

ENDPOINT_URL = os.getenv("FHIR_ENDPOINT", "http://hapi.fhir.org/baseR5")
HEADERS = {"Content-Type": "application/fhir+json"}

# 1. Patient Registration
def create_patient(patient_id, mrn, first_name, last_name, gender, birth_date, address):
    patient_data = {
        "resourceType": "Patient",
        "identifier": [
            {"system": "http://hospital.org/mrn", "value": mrn}
        ],
        "name": [
            {"use": "official", "family": last_name, "given": [first_name]}
        ],
        "gender": gender,
        "birthDate": birth_date,
        "address": [address]
    }
    response = requests.post(f"{ENDPOINT_URL}/Patient", headers=HEADERS, data=json.dumps(patient_data))
    if response.status_code in (200, 201):
        print("Patient created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create patient: {response.status_code}")
        print(response.text)
        return None

# 2. Record Blood Pressure Observation
def create_blood_pressure_observation(patient_id, systolic, diastolic):
    obs_data = {
        "resourceType": "Observation",
        "status": "final",
        "code": {
            "coding": [
                {"system": "http://loinc.org", "code": "85354-9", "display": "Blood pressure panel with all children optional"}
            ]
        },
        "subject": {"reference": f"Patient/{patient_id}"},
        "component": [
            {
                "code": {"coding": [{"system": "http://loinc.org", "code": "8480-6", "display": "Systolic blood pressure"}]},
                "valueQuantity": {"value": systolic, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            },
            {
                "code": {"coding": [{"system": "http://loinc.org", "code": "8462-4", "display": "Diastolic blood pressure"}]},
                "valueQuantity": {"value": diastolic, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            }
        ]
    }
    response = requests.post(f"{ENDPOINT_URL}/Observation", headers=HEADERS, data=json.dumps(obs_data))
    if response.status_code in (200, 201):
        print("Blood pressure observation created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create observation: {response.status_code}")
        print(response.text)
        return None

# 3. Schedule Appointment
def create_appointment(patient_id, practitioner_id, start, end, description="General check-up"):
    appt_data = {
        "resourceType": "Appointment",
        "status": "booked",
        "description": description,
        "start": start,
        "end": end,
        "participant": [
            {"actor": {"reference": f"Patient/{patient_id}"}, "status": "accepted"},
            {"actor": {"reference": f"Practitioner/{practitioner_id}"}, "status": "accepted"}
        ]
    }
    response = requests.post(f"{ENDPOINT_URL}/Appointment", headers=HEADERS, data=json.dumps(appt_data))
    if response.status_code in (200, 201):
        print("Appointment created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create appointment: {response.status_code}")
        print(response.text)
        return None

# 4. Medication Prescription
def create_medication_request(patient_id, practitioner_id, med_code, med_display, dosage_text, frequency, period, period_unit, dose_value, dose_unit):
    med_req_data = {
        "resourceType": "MedicationRequest",
        "status": "active",
        "intent": "order",
        "medicationCodeableConcept": {
            "coding": [
                {"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": med_code, "display": med_display}
            ]
        },
        "subject": {"reference": f"Patient/{patient_id}"},
        "requester": {"reference": f"Practitioner/{practitioner_id}"},
        "dosageInstruction": [
            {
                "text": dosage_text,
                "timing": {"repeat": {"frequency": frequency, "period": period, "periodUnit": period_unit}},
                "route": {"coding": [{"system": "http://snomed.info/sct", "code": "26643006", "display": "Oral route"}]},
                "doseAndRate": [
                    {"doseQuantity": {"value": dose_value, "unit": dose_unit, "system": "http://unitsofmeasure.org", "code": f"{{{dose_unit}}}"}}
                ]
            }
        ]
    }
    response = requests.post(f"{ENDPOINT_URL}/MedicationRequest", headers=HEADERS, data=json.dumps(med_req_data))
    if response.status_code in (200, 201):
        print("MedicationRequest created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create medication request: {response.status_code}")
        print(response.text)
        return None

# 5. Share Patient Data (Bundle)
def create_patient_summary_bundle(patient, condition, observation):
    bundle_data = {
        "resourceType": "Bundle",
        "type": "document",
        "entry": [
            {"resource": patient},
            {"resource": condition},
            {"resource": observation}
        ]
    }
    response = requests.post(f"{ENDPOINT_URL}/Bundle", headers=HEADERS, data=json.dumps(bundle_data))
    if response.status_code in (200, 201):
        print("Patient summary bundle created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create bundle: {response.status_code}")
        print(response.text)
        return None

# 6. Discharge Summary (Composition)
def create_discharge_summary(patient_id, practitioner_id, title, date, sections):
    comp_data = {
        "resourceType": "Composition",
        "status": "final",
        "type": {
            "coding": [
                {"system": "http://loinc.org", "code": "18842-5", "display": "Discharge summary"}
            ]
        },
        "subject": {"reference": f"Patient/{patient_id}"},
        "author": [{"reference": f"Practitioner/{practitioner_id}"}],
        "title": title,
        "date": date,
        "section": sections
    }
    response = requests.post(f"{ENDPOINT_URL}/Composition", headers=HEADERS, data=json.dumps(comp_data))
    if response.status_code in (200, 201):
        print("Discharge summary created successfully:")
        print(response.json())
        return response.json()["id"]
    else:
        print(f"Failed to create discharge summary: {response.status_code}")
        print(response.text)
        return None

# Example usage (fill in IDs and values as needed)
if __name__ == "__main__":
    # 1. Register Grandpa
    address = {"line": ["123 Main St"], "city": "Springfield", "state": "IL", "postalCode": "62704"}
    grandpa_id = create_patient(None, "12345", "John", "Doe", "male", "1980-01-01", address)

    # 2. Record blood pressure
    obs_id = create_blood_pressure_observation(grandpa_id, 120, 80)

    # 3. Schedule appointment (practitioner_id is a placeholder)
    appointment_id = create_appointment(grandpa_id, "67890", "2023-11-01T10:00:00Z", "2023-11-01T10:30:00Z")

    # 4. Medication prescription
    med_req_id = create_medication_request(
        grandpa_id, "67890", "860975", "Amoxicillin 500mg capsule",
        "Take 1 capsule by mouth every 8 hours for 7 days", 3, 1, "d", 1, "capsule"
    )

    # 5. Share patient data (example patient, condition, observation)
    patient_resource = {
        "resourceType": "Patient",
        "id": grandpa_id,
        "name": [{"use": "official", "family": "Doe", "given": ["John"]}],
        "gender": "male",
        "birthDate": "1980-01-01"
    }

    condition_resource = {
        "resourceType": "Condition",
        "id": "condition1",
        "code": {
            "coding": [{"system": "http://snomed.info/sct", "code": "44054006", "display": "Diabetes mellitus type 2"}]
        },
        "subject": {"reference": f"Patient/{grandpa_id}"}
    }

    observation_resource = {
        "resourceType": "Observation",
        "id": "observation1",
        "status": "final",
        "code": {
            "coding": [{"system": "http://loinc.org", "code": "29463-7", "display": "Body weight"}]
        },
        "valueQuantity": {"value": 80, "unit": "kg", "system": "http://unitsofmeasure.org", "code": "kg"},
        "subject": {"reference": f"Patient/{grandpa_id}"}
    }

    bundle_id = create_patient_summary_bundle(patient_resource, condition_resource, observation_resource)

    # 6. Discharge summary
    sections = [
        {"title": "Reason for Admission", "text": {"status": "generated", "div": "<div>Admitted for management of type 2 diabetes.</div>"}},
        {"title": "Medications", "text": {"status": "generated", "div": "<div>Prescribed Metformin 500mg twice daily.</div>"}}
    ]

    discharge_id = create_discharge_summary(grandpa_id, "67890", "Discharge Summary for John Doe", "2023-11-01T12:00:00Z", sections)
    