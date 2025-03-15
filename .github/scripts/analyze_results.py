import json
import sys

def check_vulnerabilities():
    try:
        with open("bandit_report.json", "r") as f:
            bandit_data = json.load(f)
    except FileNotFoundError:
        bandit_data = {"results": []}

    try:
        with open("gosec_report.json", "r") as f:
            gosec_data = json.load(f)
    except FileNotFoundError:
        gosec_data = {"Issues": []}

    # Extract critical vulnerabilities
    critical_vulnerabilities = [
        issue for issue in bandit_data.get("results", []) if issue["issue_severity"] == "CRITICAL"
    ] + [
        issue for issue in gosec_data.get("Issues", []) if issue["severity"] == "CRITICAL"
    ]

    if critical_vulnerabilities:
        print("Block")
        sys.exit(1)  # Block PR
    else:
        print("Successful")
        sys.exit(0)  # Allow PR

if __name__ == "__main__":
    check_vulnerabilities()
