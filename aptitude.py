from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# File name
file_path = "Python_AI_ML_Admission_Test.pdf"

# PDF setup
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("<b>Python & AI/ML Admission Test (MCQ)</b>", styles['Title']))
story.append(Spacer(1, 12))

# Questions
sections = {
    "Section A: Basics of Python (Q1–Q15)": [
        "1. Python was developed by (a) Guido van Rossum (b) Elon Musk (c) Bill Gates (d) Steve Jobs",
        "2. Python is (a) Compiled (b) Interpreted (c) Machine code (d) Assembly",
        "3. Which function shows output? (a) show() (b) echo() (c) print() (d) output()",
        "4. Function for input? (a) read() (b) scan() (c) input() (d) take()",
        "5. Comment symbol? (a) // (b) /* */ (c) # (d) %",
        "6. '=' is for (a) Assignment (b) Comparison (c) Printing (d) None",
        "7. '==' is for (a) Addition (b) Equality check (c) Assignment (d) Subtraction",
        "8. print(2+3) → (a) 23 (b) 5 (c) 2+3 (d) Error",
        "9. print(\"AI\") → (a) AI (b) \"AI\" (c) Error (d) None",
        "10. Multiplication operator? (a) * (b) x (c) mult (d) #",
        "11. Division operator? (a) / (b) // (c) % (d) ÷",
        "12. Data type examples? (a) int (b) float (c) str (d) All",
        "13. Conditional keyword? (a) if (b) for (c) while (d) loop",
        "14. Looping keyword? (a) for (b) switch (c) select (d) None",
        "15. Function keyword? (a) func (b) function (c) def (d) define",
    ],
    "Section B: Python in Data Science (Q16–Q22)": [
        "16. NumPy used for (a) Numbers & arrays (b) Images (c) Web (d) Games",
        "17. Pandas used for (a) Data analysis (b) Web (c) AI (d) None",
        "18. Matplotlib used for (a) Visualization (b) Audio (c) AI (d) None",
        "19. DataFrame belongs to (a) NumPy (b) Pandas (c) Matplotlib (d) None",
        "20. Bar charts library? (a) NumPy (b) Pandas (c) Matplotlib (d) None",
        "21. Arrays in Python → (a) NumPy (b) Pandas (c) Seaborn (d) None",
        "22. Common libraries? (a) NumPy, Pandas (b) Photoshop (c) Word (d) Excel",
    ],
    "Section C: AI/ML Basics (Q23–Q30)": [
        "23. AI stands for (a) Artificial Intelligence (b) Auto Intelligence (c) Applied Integration (d) None",
        "24. ML stands for (a) Machine Learning (b) Manual Logic (c) Multi Language (d) None",
        "25. AI is ability to (a) Think like humans (b) Only store data (c) Only play games (d) None",
        "26. ML learns from (a) Teachers (b) Data (c) Computers only (d) None",
        "27. Example of AI? (a) Google Maps (b) Siri (c) ChatGPT (d) All",
        "28. Supervised learning uses (a) Labeled data (b) Unlabeled (c) Random (d) None",
        "29. Unsupervised learning uses (a) Labeled (b) Unlabeled (c) Mixed (d) None",
        "30. Why Python in AI? (a) Easy + Libraries (b) Fast food (c) Hardware (d) None",
    ]
}

# Add questions
for section, qs in sections.items():
    story.append(Paragraph(f"<b>{section}</b>", styles['Heading2']))
    story.append(Spacer(1, 8))
    for q in qs:
        story.append(Paragraph(q, styles['Normal']))
        story.append(Spacer(1, 6))

story.append(Spacer(1, 20))
story.append(Paragraph("<b>Answer Key</b>", styles['Heading1']))
story.append(Spacer(1, 12))

# Answer key
answers = [
    "1.a  2.b  3.c  4.c  5.c  6.a  7.b  8.b  9.a  10.a",
    "11.a  12.d  13.a  14.a  15.c",
    "16.a  17.a  18.a  19.b  20.c  21.a  22.a",
    "23.a  24.a  25.a  26.b  27.d  28.a  29.b  30.a"
]

for ans in answers:
    story.append(Paragraph(ans, styles['Normal']))
    story.append(Spacer(1, 8))

# Build PDF
doc.build(story)
print(f"PDF generated: {file_path}")
