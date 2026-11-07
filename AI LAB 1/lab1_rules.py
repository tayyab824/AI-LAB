"""
Lab 1 - Transparent Scholarship Eligibility Rule System
Run: python lab1_rules.py
All thresholds are explicit and can be changed in one place.
"""

MIN_SCORE = 70
MAX_MONTHLY_HOUSEHOLD_INCOME = 60000  # PKR; inclusive
MIN_ATTENDANCE = 75                   # percent; inclusive


def evaluate_application(score, documents_complete, monthly_income, attendance):
    """Return (decision, reasons) using transparent, explainable rules."""
    reasons = []

    if score < MIN_SCORE:
        reasons.append(f"Score {score} is below the minimum {MIN_SCORE}.")
    if not documents_complete:
        reasons.append("Required documents are incomplete.")
    if monthly_income > MAX_MONTHLY_HOUSEHOLD_INCOME:
        reasons.append(
            f"Monthly household income PKR {monthly_income} exceeds "
            f"the limit PKR {MAX_MONTHLY_HOUSEHOLD_INCOME}."
        )
    if attendance < MIN_ATTENDANCE:
        reasons.append(
            f"Attendance {attendance}% is below the minimum {MIN_ATTENDANCE}%."
        )

    if reasons:
        return "NOT ELIGIBLE", reasons
    return "ELIGIBLE", ["All four conditions are satisfied."]


def run_tests():
    # Four required cases: overall pass, failure of each new condition,
    # and a boundary case at the stated thresholds.
    tests = [
        {
            "name": "Case 1 - All conditions pass",
            "score": 82, "documents_complete": True,
            "monthly_income": 45000, "attendance": 88,
            "expected": "ELIGIBLE"
        },
        {
            "name": "Case 2 - Income condition fails",
            "score": 85, "documents_complete": True,
            "monthly_income": 70000, "attendance": 90,
            "expected": "NOT ELIGIBLE"
        },
        {
            "name": "Case 3 - Attendance condition fails",
            "score": 78, "documents_complete": True,
            "monthly_income": 50000, "attendance": 70,
            "expected": "NOT ELIGIBLE"
        },
        {
            "name": "Case 4 - Threshold boundary",
            "score": 70, "documents_complete": True,
            "monthly_income": 60000, "attendance": 75,
            "expected": "ELIGIBLE"
        },
    ]

    print("SCHOLARSHIP RULE SYSTEM - TEST RESULTS")
    print("-" * 60)
    for test in tests:
        actual, reasons = evaluate_application(
            test["score"], test["documents_complete"],
            test["monthly_income"], test["attendance"]
        )
        status = "PASS" if actual == test["expected"] else "FAIL"
        print(f'\n{test["name"]}: {status}')
        print(
            f'Input: score={test["score"]}, '
            f'documents_complete={test["documents_complete"]}, '
            f'monthly_income=PKR {test["monthly_income"]}, '
            f'attendance={test["attendance"]}%'
        )
        print(f'Expected: {test["expected"]} | Actual: {actual}')
        print("Reason: " + " ".join(reasons))


if __name__ == "__main__":
    run_tests()
