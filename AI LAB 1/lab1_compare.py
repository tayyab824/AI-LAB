"""
Lab 1 - Simple comparison helper for a conversational-test demonstration.
This is a small scripted dialogue, not an implementation of a formal Turing test.
Run: python lab1_compare.py
"""

def scholarship_assistant(question):
    q = question.lower()

    if "minimum score" in q or "marks" in q:
        return "The minimum academic score is 70."
    if "documents" in q or "paperwork" in q:
        return "All required documents must be complete."
    if "income" in q or "family income" in q:
        return "The monthly household income limit is PKR 60,000."
    if "attendance" in q:
        return "Attendance must be at least 75 percent."
    if "eligible" in q or "apply" in q:
        return ("Eligibility requires score >= 70, complete documents, "
                "monthly household income <= PKR 60,000, and attendance >= 75%.")
    return "I can explain the score, documents, income, attendance, or eligibility rules."


if __name__ == "__main__":
    questions = [
        "What is the minimum score?",
        "What if my family income is PKR 55,000?",
        "Do I need complete documents?",
        "What attendance is required?",
        "Am I eligible if I meet all conditions?"
    ]
    print("SCRIPTED SCHOLARSHIP CONVERSATION")
    for question in questions:
        print(f"\nStudent: {question}")
        print(f"Assistant: {scholarship_assistant(question)}")
