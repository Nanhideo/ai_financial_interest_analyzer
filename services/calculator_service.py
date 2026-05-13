from datetime import date

def calculate_finance(initial_balance, interest_rate, start_date, end_date, monthly_contribution=0):
    """
    Calculates final future value based on dates.
    Returns the total months calculated from the date range.
    """
    # Calculate months between dates
    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    if months <= 0:
        months = 1

    monthly_rate = (interest_rate / 100) / 12
    current_balance = initial_balance

    for _ in range(months):
        interest_this_month = current_balance * monthly_rate
        current_balance += interest_this_month + monthly_contribution

    total_contributions = monthly_contribution * months

    return {
        "total_months": months,
        "total_contributions": round(total_contributions, 2),
        "total_balance": round(current_balance, 2)
    }