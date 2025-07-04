import pandas as pd
import numpy as np

# List of columns
columns = [
    "Dental examination", "Abdominal palpation for organomegaly", "Rectal examination",
    "Forced vital capacity", "Expiratory flow rates", "Tidal volume at rest",
    "Exercise stress test", "Resting pulses, BP, Heart rhythm",
    "Post-exercise pulses, BP, Heart rhythm", "General muscle tone",
    "Deep tendon reflexes", "Muscle power", "Sensations (touch, pain, heat)",
    "Neural tension tests", "Passive movements of limbs", "Active movements of limbs",
    "Resisted movements of limbs", "Estimation of body mass index",
    "Joint hypo/hypermobility", "Ligament integrity in ankle joints",
    "Ligament integrity in knee joints", "Palpation of lymph nodes",
    "Visual acuity, field, and color vision", "Scrotal examination",
    "Weight/Height measurement", "HB/PCV", "HB genotype", "Complete blood testing",
    "Abdominal testing", "U", "Ultrasound",
    "Echocardiography", "Exercise ECG", "Urinalysis", "Nasal swabs for testing",
    "Hepatitis B test", "CHepatitis", "CT", "HIV testing",
    "Radiographs of previously injured", "Radiographs for knee",
    "R of ankles",
    "k", "Radiographs of chest",  "C T",
    "of knee", "of CT", "of ankle",
    "CT of previously injured ", "of CT",
    "MRI of knee ", "s j", "o", "MRI of injured",
 " ", "of MRI","Dope testing"
]

# Response options
responses = ["ALWAYS", "SOMETIMES", "NEVER"]

# Generate random data
data = np.random.choice(responses, size=(300, len(columns)))

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel or CSV
df.to_excel("Mr John data.xlsx", index=False)
# df.to_csv("random_responses_300.csv", index=False)
