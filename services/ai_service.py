from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Use AsyncOpenAI configured for DeepSeek
print("Initializing AI Service with DeepSeek base_url...")
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

async def get_ai_advice(name, initial, contribution, rate, months, total):
    try:
        # Give the AI full context for better advice
        prompt = f"""
        Analyze this financial strategy for {name}:
        - Initial Investment: ${initial}
        - Monthly Contribution: ${contribution}
        - Annual Interest Rate: {rate}%
        - Duration: {months} months
        - Final Projected Balance: ${total}

        Give short, professional, and actionable financial advice based on these specific numbers.
        """

        response = await client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            timeout=30.0
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Service Error: {e}")
        return "Financial advice is currently unavailable, but your calculation is ready below."