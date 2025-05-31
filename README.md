# python-streamlit
Working with Python Steamlit and learning AI tools

# How to Run
python -m streamlit run app.py

Ensure you have python/pip, openai and streamlit packages installed

# Vocabulary and Concepts:
A distribution is the model’s internal ranking of next-word possibilities.

When you adjust the temperature, you’re reshaping this distribution:

    Lower temperature makes the distribution sharper → more confident, fewer surprises.

    Higher temperature flattens it → more randomness, more creativity.

In the context of LLMs (Large Language Models), a distribution refers to the probability distribution over all possible next tokens (words, subwords, or characters) that the model could generate at any point in a response.

- Temperature (0.0 to 1.0)

    Controls randomness / creativity.

    0.0 → more deterministic, consistent answers.

    1.0 → more creative, possibly inconsistent or verbose output.

In this context:
Use 0.0 to get reliable, structured JSON output — critical for prompt tuning.
- Max Tokens

    Controls the maximum number of tokens in the response (1 token ≈ ¾ word).

    Prevents super long outputs.

    Useful if your output needs to stay concise or you want faster response times.

For The Prompt Wrangler, where the goal is structured extraction, the most relevant are:

    - temperature: Control consistency.

    - max_tokens: Prevent overly long output.

    - stop: Can help terminate output before unwanted text.

# Project Outline
Users can update the User Prompt and System Prompt

system_prompt: tells the model how to think.
user_prompt: tells the model what to think about.

Example Usage:
Say the user enters this as their user prompt:

"Please extract the structured JSON from this clinical note: {{input_text}}"

And they paste this as the input text:

Patient has MS with significant mobility issues. Recommended a lightweight manual wheelchair with elevating leg rests. Ordered by Dr. Taub.

Your app will dynamically compose:

Please extract the structured JSON from this clinical note: 
Patient has MS with significant mobility issues. Recommended a lightweight manual wheelchair with elevating leg rests. Ordered by Dr. Taub.

Then send this to the LLM.

# Sample JSON/TestCase

System Template:
You are a medical data assistant. Extract structured JSON from clinical notes. Output only JSON.

Prompt Template:
Please extract structured data from the following note:

{{input_text}}

Input: Patient requires a full face CPAP mask with humidifier due to AHI > 20. Ordered by Dr. Cameron. 

{
  "patient_requirements": {
    "equipment": "full face CPAP mask with humidifier",
    "condition": "AHI > 20"
  },
  "order_details": {
    "ordered_by": "Dr. Cameron"
  }
}

Metrics:
{
"prompt_tokens":207
"completion_tokens":61
"total_tokens":268
"response_time":1.52
}

==

Example 2:
System Prompt:
"
You are an AI medical assistant that extracts structured JSON from clinical notes for DME (Durable Medical Equipment) orders. 

Your goal is to return a JSON object with the following fields:

- device: the main equipment (e.g. CPAP, nebulizer)
- mask_type: if applicable (e.g. full face)
- add_ons: additional components like humidifier
- qualifier: clinical reasoning or condition (e.g. "AHI > 20")
- ordering_provider: the name of the doctor who placed the order

Return only a valid JSON object, nothing else
"

==
Example 3:
Patient diagnosed with COPD, SpO2 measured at 87% on room air. Needs portable oxygen concentrator for use during exertion and sleep. Dr. Chase signed the order. 


System Prompt:
You are an AI assistant that extracts structured data from clinical notes and returns it as clean JSON. 

The clinical notes are unstructured but contain key medical information such as diagnosis, devices, usage context, and ordering providers. Your task is to:

- Read the clinical note.
- Extract relevant details into a structured JSON object.
- Match the format shown below.
- Do not add fields that are not present in the text.
- Only return the JSON, nothing else.

Expected JSON format:

{
  "device": string,
  "diagnosis": string,
  "SpO2": string,       // optional, if present
  "usage": [string],    // optional, if present
  "ordering_provider": string
}

Generic System Prompt:

You are an AI assistant that extracts structured data from clinical notes and outputs clean, consistent JSON.

Clinical notes describe the patient's condition, diagnoses, mobility status, devices or supplies needed, and the ordering provider.

Your task:
- Read the input clinical note carefully.
- Extract relevant details into a structured JSON object.
- Include only the fields that are explicitly stated in the note.
- Use arrays when multiple values apply (e.g., accessories or features).
- Return only the JSON and nothing else.

Possible JSON keys include:
- "device" or "product"
- "type"
- "features" or "components" or "accessories"
- "diagnosis"
- "SpO2"
- "usage"
- "compliance_status"
- "mobility_status"
- "qualifier"
- "ordering_provider"

Output format example:
{
  "device": "manual wheelchair",
  "type": "lightweight",
  "features": ["elevating leg rests"],
  "diagnosis": "MS",
  "ordering_provider": "Dr. Taub"
}

# Test Cases
1. CPAP with Humidifier

Input Text:

Patient requires a full face CPAP mask with humidifier due to AHI > 20. Ordered by Dr. Cameron.

Target Output:

{
  "device": "CPAP",
  "mask_type": "full face",
  "add_ons": ["humidifier"],
  "qualifier": "AHI > 20",
  "ordering_provider": "Dr. Cameron"
}

2. Portable Oxygen for COPD

Input Text:

Patient diagnosed with COPD, SpO2 measured at 87% on room air. Needs portable oxygen concentrator for use during exertion and sleep. Dr. Chase signed the order.

Target Output:

{
  "device": "portable oxygen concentrator",
  "diagnosis": "COPD",
  "SpO2": "87%",
  "usage": ["exertion", "sleep"],
  "ordering_provider": "Dr. Chase"
}

3. Manual Wheelchair for MS

Input Text:

Patient has MS with significant mobility issues. Recommended a lightweight manual wheelchair with elevating leg rests. Ordered by Dr. Taub.

Target Output:

{
  "device": "manual wheelchair",
  "type": "lightweight",
  "features": ["elevating leg rests"],
  "diagnosis": "MS",
  "ordering_provider": "Dr. Taub"
}

4. Nebulizer for Asthma

Input Text:

Asthma diagnosis confirmed. Prescribing nebulizer with mouthpiece and tubing. Dr. Foreman completed the documentation.

Target Output:

{
  "device": "nebulizer",
  "accessories": ["mouthpiece", "tubing"],
  "diagnosis": "Asthma",
  "ordering_provider": "Dr. Foreman"
}

5. Hospital Bed for ALS

Input Text:

Patient is non-ambulatory and requires hospital bed with trapeze bar and side rails. Diagnosis: late-stage ALS. Order submitted by Dr. Cuddy.

Target Output:

{
  "device": "hospital bed",
  "features": ["trapeze bar", "side rails"],
  "diagnosis": "ALS",
  "mobility_status": "non-ambulatory",
  "ordering_provider": "Dr. Cuddy"
}

6. CPAP Supplies with Accessories

Input Text:

CPAP supplies requested. Full face mask with headgear and filters. Patient has been compliant. Ordered by Dr. House.

Target Output:

{
  "product": "CPAP supplies",
  "components": ["full face mask", "headgear", "filters"],
  "compliance_status": "compliant",
  "ordering_provider": "Dr. House"
}

