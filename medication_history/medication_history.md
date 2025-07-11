# **FHIR Kata: Finding Potential Source of Side Effects**

## **Scenario:**
Your grandma recently started feeling serious headaches. It started 2 weeks ago, when a new set of medications was prescribed for her. There is no other info than the recording of intake medication list upon admission to hospital.

You have access to a system to manage and track a patient's medication prescriptions. Your task is to create a program that handles a `Patient` resource and links it to `MedicationStatement` resources, which represent the medications prescribed to the patient.

---

## **Objective:**
1. Create a `Patient` resource to represent a patient.
2. Create multiple `MedicationStatement` resources to represent the medications prescribed to the patient.
3. Link the `MedicationStatement` resources to the `Patient` resource using the `subject` field.
4. Write functions to:
   - Add a new medication prescription for the patient.
   - Retrieve and display the patient's medication history.
   - Search for medications by name.

---

## **FHIR Resources to Use:**
1. **Patient**: Represents the patient.
   - Fields: `id`, `name`, `gender`, `birthDate`.

2. **MedicationStatement**: Represents a record of a medication that is being taken by a patient.
   - Fields: `id`, `medicationCodeableConcept`, `subject`, `status`.

---

## **Example Workflow:**

1. **Create a Patient:**
   - Name: Edith Smith
   - Gender: Female
   - Birth Date: 1942-03-12

2. **Add Medication Statements:**
   - Medication: Metformin, Status: Active
   - Medication: Lisinopril, Status: Active
   - Medication: Atorvastatin, Status: Active

3. **Retrieve Medication History:**
   Output:
   ```
   Patient: Edith Smith
   Medication History:
   - Metformin (Status: Active)
   - Lisinopril (Status: Active)
   - Atorvastatin (Status: Active)
   ```

4. **Search for Medications by Name:**
   Input: "Metformin"  
   Output:
   ```
   Search Results:
   - Metformin (Status: Active)
   ```

---

## **Extensions:**
1. **Validation:**
   - Ensure the medication status is valid (e.g., `active`, `completed`, `stopped`, etc.).

2. **Search by Status:**
   - Add a function to search for medications by their status (e.g., `active` or `completed`).

3. **Integration with a FHIR Server:**
   - Use a FHIR library (e.g., `fhirclient` in Python) to send and retrieve resources from a FHIR server.

4. **User Interaction:**
   - Build a simple command-line interface to allow users to add patients, record medications, and view/search medication histories.

