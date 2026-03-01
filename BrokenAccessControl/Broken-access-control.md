# Broken Access Control – Path Traversal Vulnerability

## Overview

This project demonstrates a vulnerable HTTP server affected by Broken Access Control, specifically a Path Traversal (also known as Directory Traversal) vulnerability.

Path traversal occurs when a web application allows user-controlled input to determine file paths without properly validating or restricting access. This enables attackers to access files outside the intended directory.

This vulnerability falls under Broken Access Control in the OWASP Top 10.

---

## How the Application Works

1. A local HTTP server is running.
2. The server allows users to view files stored inside a specific directory (e.g., `/files`).
3. Users request files using a query parameter:

```
http://example.com/download?file=info.txt
```

4. The server reads the requested file from the filesystem and returns its contents in the HTTP response.

---

## The Vulnerability

The application directly concatenates user input into a file path without validating it.

Example malicious request:

```
http://example.com/download?file=../../../../../../../etc/passwd
```

The `../` sequences move up directories in the filesystem.  
If not properly restricted, this allows attackers to escape the intended directory and access sensitive system files.

This is known as **Path Traversal**.

---

## Why This Is Dangerous

This vulnerability can expose:

- Application source code
- Database files
- Configuration files containing credentials
- System files (e.g., `/etc/passwd` on Linux)
- Any file accessible to the server's operating system user

In many deployments, the web server runs with elevated privileges.  
As a result, the attacker may gain access to sensitive data belonging to the system administrator or application owner.

---

## Root Cause

The vulnerability exists because:

- User input is trusted
- File paths are constructed dynamically
- No validation or normalization is performed
- The application does not verify that the resolved path remains inside the allowed directory

---

## Impact

If exploited, this vulnerability can lead to:

- Information disclosure
- Credential leakage
- Source code exposure
- Full system compromise (depending on server permissions)

---

## OWASP Classification

- Category: Broken Access Control
- Vulnerability Type: Path Traversal / Directory Traversal
- OWASP Top 10 Reference: Broken Access Control

---

## Educational Purpose

This project is intentionally vulnerable and is provided for educational and security research purposes only.

Do not deploy this application in production.

## How to run

```cmd
pip install -r requirements.txt
flask run app
```
