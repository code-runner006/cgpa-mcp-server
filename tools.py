GRADE_BANDS = [
    (85, 4.0),
    (80, 3.7),
    (75, 3.3),
    (70, 3.0),
    (65, 2.7),
    (61, 2.3),
    (58, 2.0),
    (55, 1.7),
    (50, 1.0),
    (0, 0.0),
]

COURSES = {
 1: [("MS-251", "Probability & Statistics", 3.0),
 ("GE-160", "Applications of ICT", 3.0),
 ("GE-169", "Applied Physics", 3.0),
 ("GE-167", "Discrete Structures", 3.0),
 ("HQ-001", "Quran Translation - I", 0.5),
 ("GE-190", "Functional English", 3.0)],
 2: [("CC-112", "Programming Fundamentals", 3.0),
 ("CC-112-L", "Programming Fundamentals Lab", 1.0),
 ("CC-110", "Digital Logic Design", 2.0),
 ("CC-110-L", "Digital Logic Design Lab", 1.0),
 ("MS-252", "Linear Algebra", 3.0),
 ("GE-191", "Expository Writing", 3.0),
 ("GE-163", "Islamic Studies", 2.0),
 ("HQ-002", "Quran Translation - II", 0.5)],
 3: [("CC-211", "Object Oriented Programming", 3.0),
 ("CC-211-L", "Object Oriented Programming Lab", 1.0),
 ("CC-215", "Database Systems", 3.0),
 ("CC-215-L", "Database Systems Lab", 1.0),
 ("CC-210", "Computer Organization & Assembly Language", 3.0),
 ("GE-162", "Calculus & Analytical Geometry", 3.0),
 ("GE-192", "Introduction to Management", 2.0),
 ("HQ-003", "Quran Translation - III", 0.5)],
 4: [("CC-213", "Data Structures", 3.0),
 ("CC-213-L", "Data Structures Lab", 1.0),
 ("CC-312", "Information Security", 3.0),
 ("CC-214", "Computer Networks", 3.0),
 ("CC-212", "Software Engineering", 3.0),
 ("DC-220", "Advanced Database Management Systems", 3.0),
 ("HQ-004", "Quran Translation - IV", 0.5)],
 5: [("CC-313", "Analysis of Algorithms", 3.0),
 ("CC-310", "Artificial Intelligence", 3.0),
 ("DC-320", "Theory of Automata and Formal Languages", 3.0),
 ("DC-321", "Human Computer Interaction", 3.0),
 ("DC-322", "Computer Architecture", 3.0),
 ("EC-330", "Web Technologies / Elective", 3.0),
 ("HQ-005", "Quran Translation - V", 0.5)],
 6: [("CC-311", "Operating Systems", 3.0),
 ("EC-333", "Mobile Application Development / Elective", 3.0),
 ("EC-324", "Software Construction & Development / Elective", 3.0),
 ("EC-335", "Machine Learning / Elective", 3.0),
 ("EC-334", "Game Design and Development / Elective", 3.0),
 ("MS-253", "Multivariable Calculus", 3.0),
 ("HQ-006", "Quran Translation - VI", 0.5)],
 7: [("CC-411", "Final Year Project - I", 2.0),
 ("DC-328", "Parallel & Distributed Computing", 3.0),
 ("EC-345", "Computer Vision / Elective", 3.0),
 ("EC-425", "Software Quality Engineering / Elective", 3.0),
 ("MS-254", "Technical and Business Writing", 3.0),
 ("GE-263", "Entrepreneurship", 2.0),
 ("GE-262", "Professional Practices", 2.0),
 ("HQ-007", "Quran Translation - VII", 0.5)],
 8: [("CC-412", "Final Year Project - II", 4.0),
 ("DC-421", "Compiler Construction", 3.0),
 ("UE-272", "Introduction to Marketing", 3.0),
 ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
 ("GE-363", "Civics and Community Engagement", 2.0),
 ("HQ-008", "Quran Translation - VIII", 0.5)],
}

def marks_to_grade_points(marks: int) -> float | str:
    """Convert a raw numeric mark (0-100) into its PUCIT grade point. Use this whenever the student gives a raw mark for a course, before 
    computing a semester GPA — grade points are required input for 
    calculate_semester_gpa, not marks themselves."""

    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"
    for threshold, grade_point in GRADE_BANDS:
        if marks >= threshold:
           return grade_point

def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float | str:
    """Calculate one semester's credit-weighted GPA from a list of grade points and the matching list of credit hours (same course order in both lists). Use this once you have grade points for every course in the semester — either given directly by the student, or produced by marks_to_grade_points — together with each course's credit hours."""

    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours should be the same length."

    if not grade_points or not credit_hours:
        return "Error: At least one course is required."

    total_credit_hours = sum(credit_hours)
    if total_credit_hours == 0:
        return "Error: Total credit hours cannot be zero"

    weighted_sum = 0
    for i in range(len(grade_points)):
        weighted_sum += grade_points[i] * credit_hours[i]

    semester_gpa = weighted_sum / total_credit_hours
    return semester_gpa

def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float, semester_gpa: float, semester_credit_hours: float) -> float | str:
    """Project a student's overall CGPA after one more semester is added to
    their record. Use this once you already know the student's current CGPA,
    how many credit hours they've completed so far, and the GPA they got (or
    are projecting) for the upcoming/just-finished semester — typically right
    after calculate_semester_gpa has produced that semester's GPA, or when the
    student states it directly."""
    if completed_credit_hours < 0 or semester_credit_hours <= 0:
        return "Error: credit hours must be positive."
    if completed_credit_hours > 134.0:
        return "Error: completed credit hours cannot exceed the program total (134.0)."
    if semester_credit_hours > 18.5:
        return "Error: semester credit hours cannot exceed 18.5."
    if not (0.0 <= current_cgpa <= 4.0):
        return "Error: current_cgpa must be between 0.0 and 4.0."
    if not (0.0 <= semester_gpa <= 4.0):
        return "Error: semester_gpa must be between 0.0 and 4.0."

    total_credit_hours = completed_credit_hours + semester_credit_hours

    new_cgpa = (current_cgpa * completed_credit_hours + semester_gpa * semester_credit_hours) / total_credit_hours
    return new_cgpa

def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float, remaining_credit_hours: float) -> float | str:
    """Work out the GPA a student needs from here to hit a target CGPA.
    Needs current CGPA, completed credit hours, and remaining credit hours
    (get remaining hours from get_remaining_credit_hours if not given).
    Can return a value above 4.0 — that's not an error, it means the target
    isn't reachable in that many credit hours, so try a wider horizon."""
    if completed_credit_hours < 0 or remaining_credit_hours <= 0:
        return "Error: credit hours must be positive."
    if completed_credit_hours > 134.0:
        return "Error: completed credit hours cannot exceed the program total (134.0)."
    if completed_credit_hours + remaining_credit_hours > 134.0:
        return "Error: completed and remaining credit hours together cannot exceed the program total (134.0)."
    if not (0.0 <= current_cgpa <= 4.0):
        return "Error: current_cgpa must be between 0.0 and 4.0."
    if not (0.0 <= target_cgpa <= 4.0):
        return "Error: target_cgpa must be between 0.0 and 4.0."

    total_credit_hours = completed_credit_hours + remaining_credit_hours
    required_gpa = (target_cgpa * total_credit_hours - current_cgpa * completed_credit_hours) / remaining_credit_hours
    return required_gpa

def get_semester_courses(semester: int) -> str:
    """Return the courses and credit hours for a given semester (1-8).
    Use this when the student asks what's in a semester, or when the agent
    needs a semester's course list and credit hours to help build the
    grade_points/credit_hours lists for calculate_semester_gpa."""

    if semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    courses = COURSES[semester]

    lines = [f"Semester {semester}:"]
    total_ch = 0.0
    for code, name, credit_hours in courses:
        lines.append(f"{code} — {name} ({credit_hours} ch)")
        total_ch += credit_hours
    lines.append(f"Total credit hours: {total_ch}")

    return "\n".join(lines)

def get_remaining_credit_hours(current_semester: int) -> float | str:
    """Add up credit hours from the current semester through semester 8.
    Use this when you know a student's current semester but need their
    remaining credit hours for required_gpa_for_target or calculate_new_cgpa,
    and they haven't given that number directly, or the student just simple asked for their remaining credit hours."""

    if current_semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    total_ch = 0.0
    for semester in range(current_semester, 9):
        courses = COURSES[semester]
        for code, name, credit_hours in courses:
            total_ch += credit_hours

    return total_ch

import os

def save_report(filename: str, content: str) -> str:
    """Save a summary report to a text file. Use this only after producing
    something worth keeping — a semester GPA, a projected CGPA, or a plan
    for reaching a target CGPA — and only when the student has actually
    asked to save it. Never call this after a clarifying question or a
    single grade lookup, and never save without being asked."""

    if not filename.strip():
        return "Error: filename cannot be empty."

    filename = filename.strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError as e:
        return f"Error: could not save report ({e})"

    return f"Report saved to {filename}"
