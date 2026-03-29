# Security Vulnerabilities Found

## CRITICAL: Hardcoded AWS Credentials Exposure

**Severity:** 🔴 CRITICAL  
**File:** `secret_leak.py`  
**Type:** Secrets Management / Credential Exposure

### Description
AWS secret keys are hardcoded directly in the source code and printed to console output. This is a critical security vulnerability that violates AWS best practices and exposes sensitive credentials.

### Affected Code
```python
AWS_SECRET_KEY = "AKIA_FAKE_KEY_123456789_STUDENT_TEST"
def connect():
    print(f"Connecting with: {AWS_SECRET_KEY}")
```

### Security Impact
- Credentials visible in source code repositories
- Credentials printed to logs and console output  
- Credentials exposed in git history
- Any user with repository access can retrieve credentials
- If these were real credentials, attacker could access AWS resources

### Root Cause
- Secrets stored in code instead of environment variables or secrets manager
- Sensitive data logged without sanitization
- No .gitignore rule to prevent secrets from being committed

### Recommended Fix

**1. Remove hardcoded credentials:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def connect():
    if not AWS_SECRET_KEY:
        raise ValueError("AWS_SECRET_KEY environment variable not set")
    print("Connecting to AWS")  # Don't print the actual key!
```

**2. Create `.env` file (add to .gitignore):**
```
AWS_SECRET_KEY=your_actual_key_here
```

**3. Update `.gitignore`:**
```
.env
*.p12
*.pem
secrets/
```

**4. Scan git history:**
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secret_leak.py" \
  --prune-empty --tag-name-filter cat -- --all
```

### References
- [AWS Security Best Practices](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)
- [OWASP: Secrets Management](https://owasp.org/www-community/Sensitive_Data_Exposure)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
