# Phishing Triage Tool

A command-line tool written in Python that analyzes an email (sender, subject, body) and automatically flags common phishing red flags, then classifies the message as **Safe**, **Suspicious**, or **Malicious**.

**Author:** CyberTechSali

## Overview

This project was built to practice threat analysis and pattern detection using Python (string matching, regular expressions, dictionaries) while exploring the fundamentals of phishing and social engineering.

Rather than relying on a spam filter, this tool mimics a **human triage checklist**: it looks for the same signals a trained analyst would look for — urgency language, sender/domain mismatches, requests for sensitive information, suspicious links, and dangerous attachments — and turns them into a simple, explainable risk score.

## Features

- Detects 5 common phishing red flags:
  - Urgency / pressure language (e.g. "act now", "account locked")
  - Requests for sensitive information (passwords, MFA codes, wire transfers)
  - Sender display name / domain mismatch (e.g. "IT Security" sending from a free Gmail address)
  - Suspicious links (URL shorteners, raw IP addresses, unusual domain extensions)
  - Dangerous attachment extensions (.exe, .scr, .js, .iso, .bat, .vbs)
- Classifies each email as **SAFE**, **SUSPICIOUS**, or **MALICIOUS** based on the number of red flags found
- Recommends a concrete action for each level (Close / Warn User / Block & Escalate), following a standard triage decision tree
- Includes 3 built-in example emails to test the tool immediately
- Interactive mode to analyze your own custom email

## Requirements

- Python 3.x (no external libraries needed)

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/phishing-triage-tool.git
cd phishing-triage-tool
```

## Usage

Run the script:

```bash
python3 phishing_triage.py
```

You'll be prompted to choose between:

- `1` — Run the analysis on 3 built-in example emails (one safe, one suspicious, one malicious)
- `2` — Enter your own email (sender display name, sender email, subject, body) and see it analyzed live
- `quitter` — Exit the program

### Example output

```
====================================================
   PHISHING TRIAGE TOOL
   Author: CyberTechSali
   Analyzes an email and detects phishing red flags
   Type 'quitter' to exit
====================================================

Choice : [1] View examples  [2] Analyze your own email  [quitter] : 1

=== ANALYZING EXAMPLE EMAILS ===
--------------------------------------------------
Displayed sender : CEO Name
Real email        : hacker@gmail.com
Subject           : IMMEDIATE ACTION REQUIRED: Transfer Authorization
Risk level        : MALICIOUS
Red flags detected:
  - Urgency language detected: urgent, immediately
  - Sensitive information request: wire transfer
  - Display name 'CEO Name' suggests an official role, but the email comes from a free domain (hacker@gmail.com)
  - Dangerous attachment extension: .exe
-> Action: Block & Escalate (block the domain and report to the security team)
--------------------------------------------------
```

## How it works

Each email is checked against five independent detectors, each returning a description if a red flag is found:

1. `check_urgency()` — scans the text for a list of urgency-related keywords
2. `check_sensitive_request()` — scans for keywords tied to credentials, MFA, or financial info
3. `check_domain_mismatch()` — flags a mismatch between an official-sounding display name and a free email provider
4. `check_suspicious_links()` — uses a regular expression to detect raw IP-based links, plus URL shorteners and suspicious TLDs
5. `check_attachments()` — scans for mentions of dangerous file extensions

The total number of red flags found determines the risk level:

- 0 flags → **SAFE**
- 1–2 flags → **SUSPICIOUS**
- 3+ flags → **MALICIOUS**

Each level maps to a recommended action, following the industry-standard triage pattern: **Close**, **Warn User**, or **Block & Escalate**.

## Known limitations

This tool relies on fixed keyword lists and simple pattern matching, which means:

- **False negatives**: a well-written phishing email that avoids all listed keywords can go undetected
- **False positives**: a legitimate email that happens to mention "urgent" or "wire transfer" in a normal context may be over-flagged

These limitations are intentional and documented here to reflect real-world constraints of rule-based detection systems, as opposed to machine-learning-based spam filters.

## Possible improvements

- Weight red flags differently instead of counting them equally (e.g. a domain mismatch should count more than a single urgency keyword)
- Cross-reference multiple signals before triggering a high-risk classification, to reduce false positives
- Add detection for homoglyph and typosquatting domains (e.g. `amaz0n.com`, `paypa1.com`)
- Support reading `.eml` files directly instead of manual copy-paste
- Add a simple scoring log to track triage decisions over time

## License

This project is open source and available for learning purposes.
