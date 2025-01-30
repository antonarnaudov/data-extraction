import re
import os
import pandas as pd

"""
!!! IMPORTANT To start project run the following commands in terminal:
    - python3 -m venv .venv
    - .venv/bin/activate
    - pip install -r requirements.txt

!!! Set the following variables listed bellow:
    - TXT_FILE_PATH to point to your txt file
    - EXPORT_XLSX to export to export as excel file
    - EXPORT_CSV to export to csv
    - EXPORT_JSON to export to json

FINALLY to run the file, either use vscode/pycharm or just run `python3 src/extract_from_txt.py` in terminal
"""

# Your Settings

TXT_FILE_PATH = "input/example.txt"

EXPORT_XLSX = True
EXPORT_CSV = True
EXPORT_JSON = True


# Code
FILE_NAME = TXT_FILE_PATH.split("/")[1].split(".")[0]
OUTPUT_DIR = f"output/{FILE_NAME}"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Extraction started 🦄\n")

# Read txt file
with open(TXT_FILE_PATH, 'r', encoding='utf-8') as file:
    text = file.read()

print(f"File {TXT_FILE_PATH} read successfully 🚀")
print("Extracting...")

correct_answers = []
questions_and_answers = []

# Split the text into questions and answers
questions = re.split(r'\n\s*\n', text.strip())

for question in questions:
    lines = question.strip().split('\n')
    
    # Extract the correct answer
    for line in lines:
        if line.startswith("**Верен отговор:**"):
            correct_answers.append(line.split('**')[2].strip()[3:])  # Extract the correct answer

    if len(lines) < 2:
        continue

    # Filter out the lines containing "Верен отговор:"
    filtered_lines = [line for line in lines if not line.startswith("**Верен отговор:**")]

    if filtered_lines:
        answers = {}
        question_text = filtered_lines[0][3:]  # The first line is the question

        # Fill answers dict
        for line in filtered_lines[1:]:
            line = line.strip()
            answer_letter = line[2]
            answer = line[5:]
            
            answers[answer_letter] = answer
   
        # Append the question and answers to the result
        questions_and_answers.append({"въпрос": question_text, **answers})


if len(questions_and_answers) != len(correct_answers):
    raise Exception(
        f"🚨ERROR: You have {len(questions_and_answers)} questions and answers, "
        f"which does not match the number of correct answers {len(correct_answers)}\n"
        "This is probably due to poor formatting of the word/txt file.\n"
        "Look for questions or answers that belong on one line but are split across multiple lines with ↵"
    )


# Create DataFrame
df = pd.DataFrame(questions_and_answers)
df['верен отговор'] = correct_answers

output_path = f"{OUTPUT_DIR}/{FILE_NAME}"

# Export to Excel
if EXPORT_XLSX:
    df.to_excel(f'{output_path}.xlsx', index=False)
    print(f"Data has been saved to {output_path}.xlsx. ✅")

# Export to CSV
if EXPORT_CSV:
    df.to_csv(f'{output_path}.csv', index=False, encoding='utf-8')
    print(f"Data has been saved to {output_path}.csv. ✅")

# Export to JSON
if EXPORT_JSON:
    df.to_json(f'{output_path}.json', orient='records', force_ascii=False, indent=4)
    print(f"Data has been saved to {output_path}.json. ✅")

print("\nExtraction finished 🎉")
