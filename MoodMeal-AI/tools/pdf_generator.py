from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase.pdfmetrics import stringWidth
import re


def clean_text(text):
    # Emojis aur unsupported symbols hata do
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    return text


def generate_recipe_pdf(recipe_text, filename="MoodMeal_Recipe.pdf"):

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("MoodMeal AI Recipe", title_style))
    story.append(Spacer(1, 20))

    lines = recipe_text.split("\n")

    for line in lines:

        line = clean_text(line.strip())

        if line == "":
            continue

        # Headings
        if (
            "Meal Name" in line
            or "Why" in line
            or "Required Ingredients" in line
            or "Recipe" in line
            or "Calories" in line
            or "Protein" in line
            or "Approx Cost" in line
            or "Cooking Time" in line
            or "Healthy Tip" in line
        ):
            story.append(Paragraph(f"<b>{line}</b>", heading_style))
            story.append(Spacer(1, 8))

        else:
            story.append(Paragraph(line, normal_style))
            story.append(Spacer(1, 5))

    pdf.build(story)

    return filename
    