import re
import PyPDF2

pdf_path = "17337508371464.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

data = {}

name_pattern = r"^[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+"
name_match = re.search(name_pattern, text)
data["name"] = name_match.group(0) if name_match else "Name not found"

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_match = re.search(email_pattern, text)
data["email"] = email_match.group(0) if email_match else "Email not found"

phone_pattern = r'\b(?:\+?\d{1,3})?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b'
phone_match = re.search(phone_pattern, text)
data["mobile_number"] = phone_match.group(0).replace("\n", " ") if phone_match else "Mobile number not found"

skills_pattern = r'(?i)(?:skills|technologies|expertise)[:\-\s]*(.*?)(?:\n|$)'
skills_match = re.search(skills_pattern, text)
data["skills"] = skills_match.group(1).strip() if skills_match else "Skills not found"

college_pattern = r'\b[A-Z][a-zA-Z&.\s]*(University|Institute|College|Academy|School|Campus)\b'
college_match = re.search(college_pattern, text)
data["college_name"] = college_match.group(0) if college_match else "College name not found"

degree_pattern = r'\b(B\.?E\.?|B\.?Tech|M\.?E\.?|M\.?Tech|PhD|Bachelor|Master|Diploma|Certificate)\b'
degree_match = re.search(degree_pattern, text)
data["degree"] = degree_match.group(0) if degree_match else "Degree not found"

designation_pattern = r'\b(?:Developer|Engineer|Manager|Consultant|Analyst|Specialist|Lead|Intern)\b'
designation_match = re.search(designation_pattern, text)
data["designation"] = designation_match.group(0) if designation_match else "Designation not found"

company_pattern = r'\b[A-Z][a-zA-Z&.\s]*(?:Limited|Ltd|Inc|Corporation|Group|Technologies|Solutions|Services)\b'
companies = re.findall(company_pattern, text)
data["company_names"] = ", ".join(set(companies)) if companies else "Company names not found"

data["no_of_pages"] = len(reader.pages)

experience_pattern = r'(\d+)\s+(?:years?|yrs?)\s*(?:of)?\s*(?:experience)?'
experience_matches = re.findall(experience_pattern, text)
total_experience = sum(map(int, experience_matches)) if experience_matches else 0
data["total_experience"] = f"{total_experience} years" if total_experience > 0 else "Experience not found"

print("Name:", data["name"])
print("Email:", data["email"])
print("Mobile Number:", data["mobile_number"])
print("Skills:", data["skills"])
print("College Name:", data["college_name"])
print("Degree:", data["degree"])
print("Designation:", data["designation"])
print("Company Names:", data["company_names"])
print("No Of Pages:", data["no_of_pages"])
print("Total Experience:", data["total_experience"])
