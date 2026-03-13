# OWASP TOP 10 Vulnerable Lab

This lab provides a hands-on environment to explore and test the OWASP Top 10 web application security risks. You can either run the lab locally or download a pre-configured VirtualBox machine.


## Avilable Services & Ports
- Broken Access Controll                  5001
- Cryptographic Failures                  5004
- Injection                               5002
- Insecure Design                         5003
- Authentication Failures                 5000
- Software or Data Integrity Failures     5007
- Security Logging and Alerting Failures  5005
- Misshandling of Exceptions Conditions   5006

## Getting Started
### Option 1 Download VirtualBox machine
1. Download the pre-configured VirtualBox image `https://drive.google.com/file/d/1jygzh53cfODTk-apVGlGMqTjzBUSnZzp/view?usp=sharing`.
2. Import the machine into VirtualBox.
3. Start the VM and access services using the listed ports.
4. Login with `serverowasp:passwordowasp`
4. run `cd 2025-OWASP-TOP-10 && ./setup.sh`

### Option 2 Run locally
1. Clone the repository `git clone https://github.com/Adixtin/2025-OWASP-TOP-10.git && cd 2025-OWASP-TOP-10`
2. run the `setup.sh`
3. Acces each server via `htttp://localhost:<prot>

## Recommendations

Use in a safe, isolated environment only.
This lab contains intentionally vulnerable applications. Do not expose it to the internet.
Experiment & Learn. Focus on understanding each vulnerability and how to mitigate it.
Reference OWASP Documentation: OWASP Top 10 -> https://owasp.org/Top10/2025/

<img width="692" height="690" alt="image" src="https://github.com/user-attachments/assets/c832f4ef-5054-4964-a33e-d9680c585f01" />
