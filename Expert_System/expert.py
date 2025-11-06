import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def recommend_courses():
    interest = interest_var.get()
    skill = skill_var.get()
    try:
        gpa = float(gpa_var.get())
        semester = int(sem_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for GPA and Semester.")
        return

    recommendations = {}

    # Rule-based logic with weighted scores
    if interest == "AI":
        if gpa >= 8:
            recommendations["Machine Learning"] = 90
            recommendations["Deep Learning"] = 85
            recommendations["Neural Networks"] = 80
        elif gpa >= 6.5:
            recommendations["AI Fundamentals"] = 70

    elif interest == "Web":
        if skill == "Design":
            recommendations["UI/UX Design"] = 88
            recommendations["Frontend Frameworks (React, Vue)"] = 85
            recommendations["Responsive Design"] = 80
        elif skill == "Coding":
            recommendations["Backend Development (Node.js, Django)"] = 92
            recommendations["Full-Stack Web Development"] = 89
            recommendations["API Integration"] = 83
        elif skill == "Database":
            recommendations["Web Databases (MySQL, MongoDB)"] = 84

    elif interest == "Data Science":
        if gpa >= 8:
            recommendations["Machine Learning"] = 90
            recommendations["Data Mining"] = 85
            recommendations["Data Visualization"] = 82
            recommendations["Big Data Analytics"] = 80
        else:
            recommendations["Statistics for Data Science"] = 72

    elif interest == "Cybersecurity":
        if skill == "Networking":
            recommendations["Network Security"] = 92
            recommendations["Ethical Hacking"] = 88
            recommendations["Incident Response"] = 83
        elif skill == "Coding":
            recommendations["Penetration Testing"] = 86
            recommendations["Security Automation"] = 81
        else:
            recommendations["Cyber Threat Analysis"] = 78

    elif interest == "Cloud":
        if semester >= 6:
            recommendations["Cloud Computing"] = 91
            recommendations["DevOps Fundamentals"] = 87
            recommendations["Containerization (Docker/Kubernetes)"] = 84
            if skill == "Cloud Setup":
                recommendations["AWS/GCP Essentials"] = 88
        else:
            recommendations["Cloud Basics"] = 75

    # Display recommendations
    if not recommendations:
        messagebox.showinfo("Result", "No strong matches found. Try improving your GPA or adding more skills!")
    else:
        msg = "\n• ".join([f"{k}" for k in recommendations.keys()])
        messagebox.showinfo("Recommended Courses", f"Based on your profile, you should explore:\n\n• {msg}")

        # Visualization
        show_chart(recommendations)

def show_chart(recommendations):
    courses = list(recommendations.keys())
    scores = list(recommendations.values())

    y_pos = np.arange(len(courses))
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(courses)))

    plt.figure(figsize=(9, 6))
    bars = plt.barh(y_pos, scores, color=colors, edgecolor="white")
    plt.yticks(y_pos, courses)
    plt.xlabel("Relevance Score (%)", fontsize=12)
    plt.title("📊 Course Recommendation Confidence Chart", fontsize=16, fontweight="bold")
    plt.suptitle("Higher scores indicate stronger alignment with your skills, GPA, and interests.", fontsize=10, y=0.94)

    # Add score labels on bars
    for bar, score in zip(bars, scores):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f"{score}%", 
                 va='center', ha='left', fontsize=10, color='white')

    # Add legend-like explanation at bottom
    plt.figtext(0.1, 0.02,
                "🧩 Explanation:\n"
                "Each bar shows how relevant a course is to your profile. "
                "A higher score means stronger suitability based on your GPA, semester, and chosen skill area.",
                fontsize=9, color='white', wrap=True)

    plt.grid(axis='x', linestyle='--', alpha=0.4)
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

# ---------------- UI Setup ----------------
app = ctk.CTk()
app.title("Course Recommendation Expert System")
app.geometry("600x550")

frame = ctk.CTkFrame(app)
frame.pack(pady=30, padx=20, fill="both", expand=True)

ctk.CTkLabel(frame, text="🎓 Course Recommendation Expert System", font=("Arial", 20, "bold")).pack(pady=20)

interest_var = ctk.StringVar(value="AI")
skill_var = ctk.StringVar(value="Coding")
gpa_var = ctk.StringVar()
sem_var = ctk.StringVar()

ctk.CTkLabel(frame, text="Interest:").pack()
ctk.CTkOptionMenu(frame, values=["AI", "Web", "Data Science", "Cybersecurity", "Cloud"], variable=interest_var).pack(pady=5)

ctk.CTkLabel(frame, text="Skill Preference:").pack()
ctk.CTkOptionMenu(frame, values=[
    "Coding", "Design", "Research", "Networking", "Database", "Cloud Setup"
], variable=skill_var).pack(pady=5)

ctk.CTkLabel(frame, text="GPA:").pack()
ctk.CTkEntry(frame, textvariable=gpa_var).pack(pady=5)

ctk.CTkLabel(frame, text="Semester:").pack()
ctk.CTkEntry(frame, textvariable=sem_var).pack(pady=5)

ctk.CTkButton(frame, text="Get Recommendations", command=recommend_courses).pack(pady=20)

app.mainloop()
