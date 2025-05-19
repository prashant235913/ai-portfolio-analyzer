def generate_feedback(text):
    feedback = []

    if "Python" not in text:
        feedback.append("Consider adding Python to your skillset.")
    if "project" not in text.lower():
        feedback.append("Include details about projects you’ve worked on.")
    if "experience" not in text.lower():
        feedback.append("Mention relevant work or internship experiences.")

    return "\n".join(feedback) if feedback else "Your resume looks good!"
