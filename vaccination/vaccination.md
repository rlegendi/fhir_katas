# **FHIR Kata: Patient Vaccination Tracker**

## **Scenario:**
You are building a simple system to track patient vaccinations using FHIR resources. Your task is to create a program that manages a patient's vaccination history. This involves creating a `Patient` resource and linking it to `Immunization` resources that record the details of the vaccines the patient has received.

This exercise is a bit more meaningful rather than simply calling the API because it simulates a real-world healthcare use case. It also introduces the concept of linking FHIR resources (e.g., `Patient` and `Immunization`), which is a core part of working with FHIR in practice. Have fun coding! 😊


---

## **Objective:**
1. Create a `Patient` resource to represent a patient.
2. Create multiple `Immunization` resources to represent the vaccines the patient has received.
3. Link the `Immunization` resources to the `Patient` resource using the `patient` field.
4. Write functions to:
   - Add a new vaccination record for the patient.
   - Retrieve and display the patient's vaccination history.

---

## **FHIR Resources to Use:**
1. **Patient**: Represents the patient.
   - Fields: `id`, `name`, `gender`, `birthDate`.

2. **Immunization**: Represents a vaccination event.
   - Fields: `id`, `vaccineCode`, `patient`, `occurrenceDateTime`, `status`.

---

## **Example Workflow:**

1. **Create a Patient:**
   - Name: Alice Johnson
   - Gender: Female
   - Birth Date: 1990-05-15

2. **Add Vaccination Records:**
   - Vaccine: COVID-19 (Pfizer), Date: 2022-01-15, Status: Completed
   - Vaccine: Influenza, Date: 2021-10-01, Status: Completed

3. **Retrieve Vaccination History:**
   Output:
   ```
   Patient: Alice Johnson
   Vaccination History:
   - COVID-19 (Pfizer) on 2022-01-15 (Status: Completed)
   - Influenza on 2021-10-01 (Status: Completed)
   ```

---

## **Sample Output**

Patient created successfully:
{'resourceType': 'Patient', 'id': '801104', 'meta': {'versionId': '1', 'lastUpdated': '2025-07-09T14:50:52.010+00:00'}, 'text': {'status': 'generated', 'div': '<div xmlns="http://www.w3.org/1999/xhtml"><div class="hapiHeaderText">Alice <b>JOHNSON </b></div><table class="hapiPropertyTable"><tbody><tr><td>Date of birth</td><td><span>15 May 1990</span></td></tr></tbody></table></div>'}, 'name': [{'family': 'Johnson', 'given': ['Alice']}], 'gender': 'female', 'birthDate': '1990-05-15'}

Immunization created successfully:
{'resourceType': 'Immunization', 'id': '801108', 'meta': {'versionId': '1', 'lastUpdated': '2025-07-09T14:54:43.948+00:00', 'source': '#l2Ze2WxC5ZQeqoHv'}, 'status': 'completed', 'vaccineCode': {'coding': [{'system': 'http://hl7.org/fhir/sid/cvx', 'code': 'COVID-19 (Pfizer)', 'display': 'COVID-19 (Pfizer)'}]}, 'patient': {'reference': 'Patient/801104'}, 'occurrenceDateTime': '2022-01-15'}

Immunization created successfully:
{'resourceType': 'Immunization', 'id': '801109', 'meta': {'versionId': '1', 'lastUpdated': '2025-07-09T14:54:45.245+00:00', 'source': '#bbgl3mm3eWfe8U6e'}, 'status': 'completed', 'vaccineCode': {'coding': [{'system': 'http://hl7.org/fhir/sid/cvx', 'code': 'Influenza', 'display': 'Influenza'}]}, 'patient': {'reference': 'Patient/801104'}, 'occurrenceDateTime': '2021-10-01'}

Vaccination history for patient 801104:
- COVID-19 (Pfizer) on 2022-01-15 (Status: completed)
- Influenza on 2021-10-01 (Status: completed)

---

## **Extensions:**
1. **Validation:**
   - Ensure the `occurrenceDateTime` is a valid date.
   - Validate that the `status` is one of the allowed values (`completed`, `entered-in-error`, etc.).

2. **Search Functionality:**
   - Add a function to search for vaccinations by vaccine name or date.

3. **Integration with a FHIR Server:**
   - Use a FHIR library (e.g., `fhirclient` in Python) to send and retrieve resources from a FHIR server.

4. **User Interaction:**
   - Build a simple command-line interface to allow users to add patients, record vaccinations, and view vaccination histories.
