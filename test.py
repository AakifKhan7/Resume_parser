from pyresparser import ResumeParser
import os

resume_path = "17337508371464.pdf"

data = ResumeParser(resume_path).get_extracted_data()
print(data)
