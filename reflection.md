1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest fixes:

Missing docstrings (C0114, C0116): Adding short descriptive docstrings was straightforward since each function’s purpose was clear.

Unused import (logging) (W0611 / F401): Simply removed the unused logging import line.

Formatting issues (E302, E305, W292): Adding blank lines and a final newline was easy and could be done automatically with tools like black or autopep8.

String formatting (C0209): Replaced old-style string concatenation with modern f-strings.

Hardest fixes:

Dangerous default argument [] (W0102): Required redesigning the function definition to use None and initialize inside safely.

Bare except (except:) (W0702 / E722): Needed careful changes to catch specific exceptions (like KeyError and Exception as e) without affecting logic.

Use of eval() (W0123 / B307): Replacing eval() with ast.literal_eval() required understanding how the data was evaluated to maintain the same behavior securely.

File handling (W1514 / R1732): Needed to update all file operations to use with open(..., encoding="utf-8") safely.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes — one minor false positive was reported by Pylint:

Issue: Missing module docstring (C0114)

Explanation: The original script was small and self-explanatory, and documentation was already covered elsewhere. Although not harmful, Pylint still flagged it for missing a top-level description.

Resolution: Added a short docstring for full compliance, even though the lack of one wouldn’t cause any runtime or readability issues.

3. How would you integrate static analysis tools into your actual software development workflow?

All tools were executed in the project directory:

/workspaces/Lab5_Static_Code_Analysis


Commands used:

pylint inventory_system.py > reports/pylint_report.txt 2>&1
flake8 inventory_system.py > reports/flake8_report.txt 2>&1
bandit -r inventory_system.py > reports/bandit_report.txt 2>&1


Recommended directory structure:

/workspaces/Lab5_Static_Code_Analysis/
│
├── inventory_system.py
├── reports/
│   ├── pylint_report.txt
│   ├── flake8_report.txt
│   ├── bandit_report.txt
│   ├── pylint_report_after.txt
│   ├── flake8_report_after.txt
│   └── bandit_report_after.txt
└── .github/workflows/static_analysis.yml


Continuous Integration (CI) Integration:
A GitHub Actions workflow can automatically run these tools for every push or pull request:

name: Static Code Analysis

on:
  push:
    branches: [ main, fix/static-analysis ]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install tools
        run: |
          pip install pylint flake8 bandit

      - name: Run pylint
        run: pylint inventory_system.py

      - name: Run flake8
        run: flake8 inventory_system.py

      - name: Run bandit
        run: bandit -r .


Summary:
This ensures static analysis runs automatically in the CI pipeline, catching issues before merging. Locally, pre-commit hooks can also be used to run pylint, flake8, and bandit before every commit.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying all the fixes, the code became much cleaner, safer, and fully compliant with modern Python standards.

Aspect	Before Fixes	After Fixes	Improvement
Code Readability	Inconsistent naming, missing docstrings	Used consistent snake_case naming and added clear docstrings	Easier to understand and maintain
Security	Used eval() and bare except: blocks	Replaced with ast.literal_eval() and specific exception handling	Eliminated major security and logic risks
Reliability	Unsafe default arguments, no file context	Used safe argument defaults and with open(..., encoding="utf-8")	Improved safety and reliability
Maintainability	Unstructured and inconsistent	Standardized formatting and clear error messages	Easier to debug and extend
Tool Compliance	Multiple medium/high warnings	All major issues resolved; clean linting reports	Code passes all static analysis tools