import json
import requests
import os

ENDPOINT_URL = os.getenv("FHIR_ENDPOINT", "http://hapi.fhir.org/baseR5")

# Create and send a Patient Resource to FHIR Endpoint

def create_patient(id, first_name, last_name, gender, birth_date):
    patient_data = {
        "resourceType": "Patient",
        "id": id,
        "name": [
            {
                "given": [first_name],
                "family": last_name
            }
        ],
        "gender": gender,
        "birthDate": birth_date
    }

    headers = {"Content-Type": "application/fhir+json"}
    response = requests.put(f"{ENDPOINT_URL}/Patient/{id}", headers=headers, data=json.dumps(patient_data))
    
    if response.status_code in (200, 201):
        print("Patient created successfully:")
        print(response.json())
    else:
        print(f"Failed to create patient: {response.status_code}")
        print(response.text)

# Create and send a MedicationStatement Resource to FHIR Endpoint

def create_medication_statement(id, patient_id, med_code, med_display, status="recorded"):
    med_statement_data = {
        "resourceType": "MedicationStatement",
        "id": id,
        "status": status,
        "medicationCodeableConcept": {
            "coding": [
                {
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                    "code": med_code,
                    "display": med_display
                }
            ]
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        }
    }

    headers = {"Content-Type": "application/fhir+json"}
    response = requests.put(f"{ENDPOINT_URL}/MedicationStatement/{id}", headers=headers, data=json.dumps(med_statement_data))
    
    if response.status_code in (200, 201):
        print(f"MedicationStatement for {med_display} created successfully:")
        print(response.json())
    else:
        print(f"Failed to create MedicationStatement: {response.status_code}")
        print(response.text)

# Query a patient's medication history from the FHIR endpoint

def get_medication_history(patient_id):
    headers = {"Accept": "application/fhir+json"}
    params = {"subject": patient_id}
    response = requests.get(f"{ENDPOINT_URL}/MedicationStatement", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Medication history for patient {patient_id}:")
        for entry in data.get("entry", []):
            resource = entry["resource"]
            med = resource["medicationCodeableConcept"]["coding"][0]["display"]
            status = resource["status"]
            print(f"- {med} (Status: {status})")
    else:
        print(f"Failed to retrieve medication history: {response.status_code}")
        print(response.text)

# Example Usage: Grandma
create_patient("grandma001", "Edith", "Smith", "female", "1942-03-12")

create_medication_statement("med1", "grandma001", "860975", "Metformin")
create_medication_statement("med2", "grandma001", "197361", "Lisinopril")
create_medication_statement("med3", "grandma001", "617314", "Atorvastatin")

get_medication_history("grandma001")
