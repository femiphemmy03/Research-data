import pandas as pd
import numpy as np

# List of columns
columns = [
    "Does your team have a doctor?",
"Team doctor travels with the team for away games",
"Is the team doctor a specialist in sports medicine?",
"Team has a physiotherapist",
"Team has a massage therapist",
"Team has a nurse or nurses",
"Club has a referral hospital",
"Previous heart illness",
"Previous concussion or head injury",
"Previous convulsions/seizures",
"Diabetes mellitus",
"Drug addiction",
"Alcohol use",
"Anabolic steroid use",
"Sickle cell (HB genotype status)",
"Immunization status (Hepatitis, Tetanus, Flu)",
"Current intake of prescription/non-prescription drugs",
"Overnight hospitalization",
"Recent illness or injury since last checkup",
"History of previous surgery",
"Supplement/vitamin use to improve weight or performance",
"History of high blood pressure or heart murmur",
"Skin problems (e.g., rashes, warts)",
"Eye trauma/surgery",
"History of sprain or strain",
"History of fractures/dislocation",
"Numbness/tingling in limbs",
"Visual problems",
"Wears glasses/contact lenses"

]

# Response options
responses = ["YES", "NO"]

# Generate random data
data = np.random.choice(responses, size=(300, len(columns)))

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel or CSV
df.to_excel("Mr John data.xlsx", index=False)
# df.to_csv("random_responses_300.csv", index=False)
