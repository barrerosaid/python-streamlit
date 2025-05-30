# python-streamlit
Working with Python Steamlit and learning AI tools

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