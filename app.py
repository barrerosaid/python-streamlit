import streamlit as st
import openai
import os
from llm_client import LLMClient

# Load OpenAI key from secrets or env
openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

st.title("🤖 The Prompt Wrangler")
st.caption("LLM Tuning Playground for Clinical Notes")

# Prompt input
system_prompt = st.text_area("🔧 System Prompt", value="You are a medical data assistant. Extract structured JSON from clinical notes. Output only JSON.")
user_prompt_template = st.text_area("💬 User Prompt Template", value="Please extract structured data from the following note:\n\n{{input_text}}")

# Clinical note
input_text = st.text_area("📄 Clinical Note", height=150)

# Parameters
col1, col2 = st.columns(2)
temperature = col1.slider("Temperature", 0.0, 1.0, 0.5)
max_tokens = col2.slider("Max Tokens", 100, 2048, 512)

# Run button
if st.button("🚀 Run LLM"):
    if "{{input_text}}" not in user_prompt_template:
        st.error("Please include {{input_text}} in your user prompt.")
    else:
        final_user_prompt = user_prompt_template.replace("{{input_text}}", input_text)
        client = LLMClient()
        output, metrics = client.call_llm(system_prompt, final_user_prompt, temperature, max_tokens)

        st.subheader("🧾 Output")
        st.code(output, language="json" if output.strip().startswith("{") else "text")

        if metrics:
            st.subheader("📊 Metrics")
            st.write(metrics)