import os
import re
import subprocess

from dotenv import load_dotenv
from openai import OpenAI

from prompts import DIAGNOSIS_PROMPT, PATCH_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


class TriageAgent:
    def process_issue(self, issue_path: str) -> str:
        print("\n[Triage Agent]")
        print("Loading issue...")

        with open(issue_path, "r", encoding="utf-8") as f:
            issue = f.read()

        print("Issue loaded")

        return issue


class DiagnosisAgent:

    REPOSITORY_DESCRIPTION = """
Repository Structure

bookstore/

pricing.py
Responsible for calculating prices and discounts.

checkout.py
Handles the checkout workflow.

inventory.py
Stores the available books and their prices.
"""

    def identify_file(self, issue: str) -> str:

        print("\n[Diagnosis Agent]")
        print("Analyzing repository...")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": DIAGNOSIS_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
GitHub Issue

{issue}

{self.REPOSITORY_DESCRIPTION}
"""
                }
            ]
        )

        answer = response.choices[0].message.content.strip()

        match = re.search(r"bookstore[/\\\\][A-Za-z0-9_]+\.py", answer)

        if match:
            file_path = match.group(0)
        else:
            match = re.search(r"[A-Za-z0-9_]+\.py", answer)

            if match:
                file_path = "bookstore/" + match.group(0)
            else:
                raise Exception(
                    "Diagnosis Agent could not determine the relevant file."
                )

        print(f"Relevant file: {file_path}")

        return file_path


class PatchAgent:

    def repair(self, issue: str, file_path: str):

        print("\n[Patch Agent]")
        print("Generating candidate patch...")

        with open(file_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": PATCH_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
GitHub Issue

{issue}

Current Source Code

{source_code}
"""
                }
            ]
        )

        fixed_code = response.choices[0].message.content.strip()

        if fixed_code.startswith("```"):
            fixed_code = (
                fixed_code
                .replace("```python", "")
                .replace("```", "")
                .strip()
            )

        # Basic validation to ensure a Python file was returned
        if "class PricingService" not in fixed_code:
            raise Exception(
                "Patch Agent returned an invalid response instead of Python code."
            )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        print("Patch generated and applied")


class ValidationAgent:

    def validate(self) -> bool:

        print("\n[Validation Agent]")
        print("Running test suite...\n")

        result = subprocess.run(
            ["pytest", "-q"],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.returncode == 0:
            print("Validation Successful")
            return True

        print("Validation Failed")

        if result.stderr:
            print(result.stderr)

        return False