import streamlit as st
from llm_client import LLMClient

# Initialize LLM client
llm_client = LLMClient()

st.title("🧠 The Prompt Wrangler")

# Text inputs
system_prompt = st.text_area("System Prompt", value=(
    "You are an AI assistant that extracts structured data from clinical notes and returns JSON. "
    "Return only JSON and include only fields present in the note."
))

input_text = st.text_area("Clinical Note Input", height=150)

# Model parameters
#temperature = st.slider("Temperature", 0.0, 1.0, 0.2, step=0.05)
#max_tokens = st.slider("Max Tokens", 50, 1000, 500, step=50)
temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.05,
    help="Controls randomness. Lower = more focused, higher = more creative."
)

max_tokens = st.sidebar.number_input(
    "Max Tokens",
    min_value=10,
    max_value=2000,
    value=500,
    step=50,
    help="Limits the length of the response."
)

# Submit button
if st.button("💬 Generate"):
    if not input_text.strip():
        st.warning("Please enter a clinical note.")
    else:
        # Automatically generate user prompt from template
        user_prompt = f"Extract structured JSON from the following clinical note:\n\n{input_text}"

        # Call LLM
        response_text, meta = llm_client.call_llm(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        # Display result
        st.subheader("📤 Structured Output")
        st.code(response_text, language="json")

        # Meta info
        if meta:
            st.markdown("---")
            st.text(f"⏱️ Response Time: {meta.get('response_time', 'N/A')}s")
            st.text(f"🔢 Tokens Used: {meta.get('total_tokens', 'N/A')}")
            st.sidebar.header("LLM Settings")

