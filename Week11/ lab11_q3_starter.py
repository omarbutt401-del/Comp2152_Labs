# ============================================================
#  WEEK 11 LAB — Q3: VULNERABILITY REPORT
#  COMP2152 — Omar Butt
# ============================================================
#
#  For the term project, each team member finds a vulnerability
#  and writes a report. This class represents those findings
#  and organizes them into a team report.
#
# ============================================================

class Finding:

    def __init__(self, subdomain, title, severity, description):
        self.subdomain = subdomain
        self.title = title
        self.severity = severity
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.subdomain} — {self.title}"


class Report:

    # TODO: Write the constructor
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    # TODO: Write add_finding(self, finding)
    def add_finding(self, finding):
        self.findings.append(finding)

    # TODO: Write get_by_severity(self, severity)
    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity]

    # TODO: Write summary(self)
    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")

        high = len(self.get_by_severity("HIGH"))
        medium = len(self.get_by_severity("MEDIUM"))
        low = len(self.get_by_severity("LOW"))

        print(f"  HIGH:   {high}")
        print(f"  MEDIUM: {medium}")
        print(f"  LOW:    {low}")
        print("  " + "-" * 40)

        for f in self.findings:
            print(f"  {f}")


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q3: VULNERABILITY REPORT")
    print("=" * 60)

    findings_data = [
        ("ssh.0x10.cloud",  "Default credentials admin:admin",      "HIGH",   "SSH server accepts admin:admin"),
        ("blog.0x10.cloud", "No HTTPS (cleartext)",                 "LOW",    "Blog served over HTTP"),
        ("ftp.0x10.cloud",  "Anonymous FTP access",                 "HIGH",   "FTP allows anonymous login"),
        ("api.0x10.cloud",  "Server version exposed in headers",    "MEDIUM", "API leaks version"),
        ("cdn.0x10.cloud",  "Missing security headers",             "LOW",    "No CSP headers"),
    ]

    print("\n--- Adding Findings ---")
    report = Report("CyberHunters")
    for sub, title, sev, desc in findings_data:
        f = Finding(sub, title, sev, desc)
        report.add_finding(f)
        print(f"  Added: {f}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    high = report.get_by_severity("HIGH")
    if high:
        for f in high:
            print(f"  {f}")
    else:
        print("  (none)")

    print("\n" + "=" * 60)