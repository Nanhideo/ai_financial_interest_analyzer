from fastapi import APIRouter, HTTPException
from services.calculator_service import calculate_finance
from services.database_service import collection
from models.finance_model import FinanceRequest
from datetime import date

router = APIRouter()

@router.get("/api/history")
async def get_history():
    """
    Returns the last 10 financial calculations as JSON.
    """
    try:
        records = list(collection.find().sort("_id", -1).limit(10))
        for record in records:
            if "_id" in record:
                record["_id"] = str(record["_id"])
        return {
            "status": "success",
            "data": records
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.post("/api/calculate")
async def api_calculate(request: FinanceRequest):
    """
    Calculates financial interest based on start and end dates.
    """
    try:
        # 1. Use today's date if start_date is not provided
        start_dt = request.start_date if request.start_date else date.today()

        # 2. Calculate finance logic (Months derived internally from dates)
        result = calculate_finance(
            request.initial_balance,
            request.interest_rate,
            start_dt,
            request.end_date,
            request.monthly_contribution
        )

        # 3. Prepare data object for DB and response
        data = {
            "name": request.name,
            "initial_balance": request.initial_balance,
            "interest_rate": request.interest_rate,
            "monthly_contribution": request.monthly_contribution,
            **result
        }

        # 4. Save to Database
        try:
            db_data = data.copy()
            collection.insert_one(db_data)
        except:
            pass
        
        # 5. Return clean results (no 'months' field in output)
        return {
            "status": "success",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
