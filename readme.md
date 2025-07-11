# FHIR Katas
*By rlegendi*

**This repository contains hands-on exercises (katas) for learning and practicing Fast Healthcare Interoperability Resources (FHIR) concepts with hands-on coding.** Sample codes are Python, but the beauty of FHIR being a common protocoll is that practically you can use your preferred language. Anything from C++ through C# to Kotlin and Java.

Each kata is a self-contained scenario that guides you through building simple FHIR-based applications.

## What is FHIR and Why Does It Matter?

**FHIR** is a modern standard developed by HL7 for exchanging healthcare information electronically. It is designed to make it easier for different healthcare systems—like hospitals, clinics, labs, and pharmacies—to share and access patient data securely and efficiently.

The specification can be found here: https://hl7.org/fhir/index.html

### Why is FHIR Important?

- **Interoperability:** FHIR enables different Electronic Health Record (EHR) systems to "speak the same language," making it possible to transfer patient data seamlessly between hospitals, clinics, and even across countries.
- **Patient Access:** Thanks to FHIR, patients can access their health records through apps and portals, empowering them to manage their own care.
- **Rapid Response:** During the COVID-19 pandemic, FHIR played a key role in enabling quick data sharing for case tracking, vaccination records, and public health reporting.
- **Regulatory Compliance:** The 21st Century Cures Act (USA) requires healthcare providers to give patients access to their health data via standardized APIs—FHIR is the backbone of these APIs.

### Practical Examples

- When a patient moves to a new hospital, FHIR allows their medical history, medications, and allergies to be transferred instantly and accurately.
- Pharmacies can check for drug interactions by accessing up-to-date medication lists from EHRs using FHIR APIs.
- Public health agencies can aggregate anonymized data from many sources to track disease outbreaks in real time.
- The Office of the National Coordinator for Health Information Technology (ONC), which oversees the implementation of the [21st Century Cures Act](https://www.healthit.gov/curesrule/), has explicitly endorsed FHIR as a key standard for meeting the Act's interoperability requirements. For example:
  - The ONC's 2020 Cures Act Final Rule mandates the use of FHIR-based APIs to enable patient access to EHI.
  - Certified Health IT developers are required to implement FHIR Release 4 (R4) APIs to comply with the ONC's certification criteria.s


## Project Structure

- `medication_history/`  
  Contains the Medication History kata, where you manage a patient's medication prescriptions using FHIR resources.

- `vaccination/`  
  Contains the Vaccination Tracker kata, where you track patient vaccinations using FHIR resources.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd fhir_katas
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Read the kata instructions:**
   - Open the relevant `.md` file in each kata directory for the scenario and objectives.

4. **Implement your solution:**
   - Write your code in your favourite language, compile if needed, and run!

## Extensions
Each kata includes optional extensions, such as validation, search, FHIR server integration, and user interaction. Try implementing these for extra practice!

---

Happy coding and learning FHIR!
