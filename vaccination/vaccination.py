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

# Create and send an Immunization Resource to FHIR Endpoint

def create_immunization(id, vaccine_code, patient_id, date, status):
    immunization_data = {
        "resourceType": "Immunization",
        "id": id,
        "vaccineCode": {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/sid/cvx",
                    "code": vaccine_code,
                    "display": vaccine_code
                }
            ]
        },
        "patient": {
            "reference": f"Patient/{patient_id}"
        },
        "occurrenceDateTime": date,
        "status": status
    }
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(f"{ENDPOINT_URL}/Immunization", headers=headers, data=json.dumps(immunization_data))
    if response.status_code in (200, 201):
        print("Immunization created successfully:")
        print(response.json())
    else:
        print(f"Failed to create immunization: {response.status_code}")
        print(response.text)

# Query a patient's vaccination (immunization) history from the FHIR endpoint

def get_vaccination_history(patient_id):
    headers = {"Accept": "application/fhir+json"}
    params = {"patient": patient_id}
    response = requests.get(f"{ENDPOINT_URL}/Immunization", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Vaccination history for patient {patient_id}:")
        for entry in data.get("entry", []):
            resource = entry["resource"]
            vaccine = resource["vaccineCode"]["coding"][0]["display"]
            date = resource["occurrenceDateTime"]
            status = resource["status"]
            print(f"- {vaccine} on {date} (Status: {status})")
    else:
        print(f"Failed to retrieve vaccination history: {response.status_code}")
        print(response.text)

# Example Usage
create_patient("801104", "Alice", "Johnson", "female", "1990-05-15")
create_immunization("1", "COVID-19 (Pfizer)", "801104", "2022-01-15", "completed")
create_immunization("2", "Influenza", "801104", "2021-10-01", "completed")
get_vaccination_history("801104")
