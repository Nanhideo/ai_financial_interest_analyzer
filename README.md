# AI Financial Interest Analyzer

A powerful FastAPI-based application that calculates financial interest and provides AI-driven financial advice.

## Features
- **Interest Calculation**: Detailed breakdown of interest, total amount, and rates (monthly, daily, hourly, minute).
- **AI Advice**: Integration with OpenAI to provide personalized financial tips.
- **Data Persistence**: Stores records in MongoDB.
- **Modern UI**: Clean and responsive design.

## Project Structure
- `app.py`: Main application entry point.
- `routes/`: API and web routes.
- `services/`: Business logic and external integrations (AI, Database, Calculator).
- `models/`: Data models.
- `templates/`: HTML templates.
- `static/`: Static assets (CSS, JS, Images).

## Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure environment**:
   Create a `.env` file with:
   ```env
   MONGO_URL=mongodb://localhost:27017/
   OPENAI_API_KEY=your_api_key_here
   ```
3. **Run the application**:
   ```bash
   uvicorn app:app --reload
   ```
