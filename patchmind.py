from agents import (
    TriageAgent,
    DiagnosisAgent,
    PatchAgent,
    ValidationAgent,
)


def banner():
    print("=" * 60)
    print("PatchMind")
    print("Autonomous Bug Triage & Repair Prototype")
    print("=" * 60)


def summary(issue, file_path, success):
    print("\n" + "=" * 60)
    print("Execution Summary")
    print("=" * 60)

    title = "Unknown"

    for line in issue.splitlines():
        if line.startswith("Title:"):
            title = line.replace("Title:", "").strip()
            break

    print(f"Issue          : {title}")
    print(f"Modified File  : {file_path}")

    if success:
        print("Validation     : PASSED")
        print("Status         : READY FOR PULL REQUEST")
    else:
        print("Validation     : FAILED")
        print("Status         : MANUAL REVIEW REQUIRED")

    print("=" * 60)


def main():

    banner()

    triage = TriageAgent()
    diagnosis = DiagnosisAgent()
    patch = PatchAgent()
    validation = ValidationAgent()

    issue = triage.process_issue("issue.txt")

    file_path = diagnosis.identify_file(issue)

    patch.repair(issue, file_path)

    success = validation.validate()

    summary(issue, file_path, success)


if __name__ == "__main__":
    main()