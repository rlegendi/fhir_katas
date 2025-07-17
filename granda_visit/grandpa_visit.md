# **FHIR Kata: Zombie Infection Vaccination Tracker**

## **Scenario:**
Your grandpa visits you, but feels dizzy. He has been sent to the hospital where you work. Unfortunately, a system upgrade crashes most systems and docs/nurses cannot use the UI. You need to register him, record a blood pressure, schedule a follow-up appointment, do a perscription, share some of the data with the pharmacy, then discharge your grandpa. And you need to do this only through the REST APIs :-)


---

### **1. Patient Registration**
- **Scenario:** A new patient visits a clinic, and their information needs to be recorded in the system.
- **Steps:**
  1. Create a `Patient` resource with the patient's demographic details (e.g., name, gender, birthdate, address).
  2. Include an `identifier` for the patient, such as a medical record number (MRN).

- **Example Request:**
  ```http
  POST /fhir/Patient HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "Patient",
    "identifier": [
      {
        "system": "http://hospital.org/mrn",
        "value": "12345"
      }
    ],
    "name": [
      {
        "use": "official",
        "family": "Doe",
        "given": ["John"]
      }
    ],
    "gender": "male",
    "birthDate": "1980-01-01",
    "address": [
      {
        "line": ["123 Main St"],
        "city": "Springfield",
        "state": "IL",
        "postalCode": "62704"
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The patient is registered in the system, and the server returns a `201 Created` response with the `Patient` resource's unique ID.

---

### **2. Recording a Vital Sign Observation**
- **Scenario:** A nurse records a patient's blood pressure during a visit.
- **Steps:**
  1. Create an `Observation` resource to record the blood pressure.
  2. Link the `Observation` to the `Patient` using the `subject` field.

- **Example Request:**
  ```http
  POST /fhir/Observation HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "Observation",
    "status": "final",
    "code": {
      "coding": [
        {
          "system": "http://loinc.org",
          "code": "85354-9",
          "display": "Blood pressure panel with all children optional"
        }
      ]
    },
    "subject": {
      "reference": "Patient/12345"
    },
    "component": [
      {
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "8480-6",
              "display": "Systolic blood pressure"
            }
          ]
        },
        "valueQuantity": {
          "value": 120,
          "unit": "mmHg",
          "system": "http://unitsofmeasure.org",
          "code": "mm[Hg]"
        }
      },
      {
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "8462-4",
              "display": "Diastolic blood pressure"
            }
          ]
        },
        "valueQuantity": {
          "value": 80,
          "unit": "mmHg",
          "system": "http://unitsofmeasure.org",
          "code": "mm[Hg]"
        }
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The blood pressure observation is recorded, and the server returns a `201 Created` response with the `Observation` resource's unique ID.

---

### **3. Scheduling an Appointment**
- **Scenario:** A patient schedules an appointment with a doctor.
- **Steps:**
  1. Create an `Appointment` resource with details about the patient, practitioner, and time.
  2. Link the `Patient` and `Practitioner` resources using the `participant` field.

- **Example Request:**
  ```http
  POST /fhir/Appointment HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "Appointment",
    "status": "booked",
    "description": "General check-up",
    "start": "2023-11-01T10:00:00Z",
    "end": "2023-11-01T10:30:00Z",
    "participant": [
      {
        "actor": {
          "reference": "Patient/12345"
        },
        "status": "accepted"
      },
      {
        "actor": {
          "reference": "Practitioner/67890"
        },
        "status": "accepted"
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The appointment is scheduled, and the server returns a `201 Created` response with the `Appointment` resource's unique ID.

---

### **4. Medication Prescription**
- **Scenario:** A doctor prescribes medication for a patient.
- **Steps:**
  1. Create a `MedicationRequest` resource with details about the medication, dosage, and patient.
  2. Link the `Patient` and `Practitioner` resources using the `subject` and `requester` fields.

- **Example Request:**
  ```http
  POST /fhir/MedicationRequest HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "MedicationRequest",
    "status": "active",
    "intent": "order",
    "medicationCodeableConcept": {
      "coding": [
        {
          "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
          "code": "860975",
          "display": "Amoxicillin 500mg capsule"
        }
      ]
    },
    "subject": {
      "reference": "Patient/12345"
    },
    "requester": {
      "reference": "Practitioner/67890"
    },
    "dosageInstruction": [
      {
        "text": "Take 1 capsule by mouth every 8 hours for 7 days",
        "timing": {
          "repeat": {
            "frequency": 3,
            "period": 1,
            "periodUnit": "d"
          }
        },
        "route": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "26643006",
              "display": "Oral route"
            }
          ]
        },
        "doseAndRate": [
          {
            "doseQuantity": {
              "value": 1,
              "unit": "capsule",
              "system": "http://unitsofmeasure.org",
              "code": "{capsule}"
            }
          }
        ]
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The medication request is recorded, and the server returns a `201 Created` response with the `MedicationRequest` resource's unique ID.

---

### **5. Sharing Patient Data Between Systems**
- **Scenario:** A hospital shares a patient's summary with another healthcare provider.
- **Steps:**
  1. Create a `Bundle` resource of type `document` containing the patient's summary.
  2. Include resources like `Patient`, `Condition`, and `Observation` in the bundle.

- **Example Request:**
  ```http
  POST /fhir/Bundle HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "Bundle",
    "type": "document",
    "entry": [
      {
        "resource": {
          "resourceType": "Patient",
          "id": "12345",
          "name": [
            {
              "use": "official",
              "family": "Doe",
              "given": ["John"]
            }
          ],
          "gender": "male",
          "birthDate": "1980-01-01"
        }
      },
      {
        "resource": {
          "resourceType": "Condition",
          "id": "condition1",
          "code": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "44054006",
                "display": "Diabetes mellitus type 2"
              }
            ]
          },
          "subject": {
            "reference": "Patient/12345"
          }
        }
      },
      {
        "resource": {
          "resourceType": "Observation",
          "id": "observation1",
          "status": "final",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "29463-7",
                "display": "Body weight"
              }
            ]
          },
          "valueQuantity": {
            "value": 80,
            "unit": "kg",
            "system": "http://unitsofmeasure.org",
            "code": "kg"
          },
          "subject": {
            "reference": "Patient/12345"
          }
        }
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The patient summary is shared as a FHIR document, and the server returns a `201 Created` response with the `Bundle` resource's unique ID.

---

### **6. Discharge Summary**
- **Scenario:** A hospital generates a discharge summary for a patient after their stay.
- **Steps:**
  1. Create a `Composition` resource to represent the discharge summary.
  2. Link the `Patient`, `Practitioner`, and other relevant resources.

- **Example Request:**
  ```http
  POST /fhir/Composition HTTP/1.1
  Content-Type: application/fhir+json

  {
    "resourceType": "Composition",
    "status": "final",
    "type": {
      "coding": [
        {
          "system": "http://loinc.org",
          "code": "18842-5",
          "display": "Discharge summary"
        }
      ]
    },
    "subject": {
      "reference": "Patient/12345"
    },
    "author": [
      {
        "reference": "Practitioner/67890"
      }
    ],
    "title": "Discharge Summary for John Doe",
    "date": "2023-11-01T12:00:00Z",
    "section": [
      {
        "title": "Reason for Admission",
        "text": {
          "status": "generated",
          "div": "<div>Admitted for management of type 2 diabetes.</div>"
        }
      },
      {
        "title": "Medications",
        "text": {
          "status": "generated",
          "div": "<div>Prescribed Metformin 500mg twice daily.</div>"
        }
      }
    ]
  }
  ```

- **Expected Outcome:**
  - The discharge summary is recorded, and the server returns a `201 Created` response with the `Composition` resource's unique ID.

---

These **real-life scenarios** demonstrate how FHIR can be used in practical healthcare workflows, from patient registration to discharge summaries. They align with foundational FHIR concepts and are great preparation for your certification!