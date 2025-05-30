import openai
import time
import logging
from typing import Tuple, Optional, Dict

class LLMClient:
    def __init__(self, model="gpt-4o", mock_mode=False):
        self.model = model
        self.mock_mode = mock_mode

    def call_llm(self, system_prompt: str, user_prompt: str, temperature: float = 0.5, max_tokens: int = 512) -> Tuple[str, Optional[Dict]]:
        if self.mock_mode:
            return self._mock_response(), None

        start_time = time.time()
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            output_text = response.choices[0].message.content
            usage = response.usage.to_dict() if hasattr(response, "usage") else {}
            elapsed = round(time.time() - start_time, 2)
            return output_text, {**usage, "response_time": elapsed}
        except Exception as e:
            logging.exception("OpenAI API call failed.")
            return f"Error: {str(e)}", None

    def _mock_response(self) -> str:
        return '{"device": "CPAP", "mask_type": "full face", "add_ons": ["humidifier"], "ordering_provider": "Dr. Cameron"}'