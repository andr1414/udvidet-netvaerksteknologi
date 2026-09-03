from pathlib import Path
import shutil
import subprocess
import sys


def check(name, condition, detail=""):
    if condition:
        print(f" [OK] {name}")
        return True
    else:
        print(f" [FEJL] {name}")
        if detail:
            print(f"        {detail}")
        return False


print()
print("=" * 60)
print(" PYTHON DEVELOPMENT ENVIRONMENT - SELF TEST")
print("=" * 60)
print()

results = []

# 1. Python
results.append(
    check(
        "Python",
        sys.version_info >= (3, 10),
        f"Du bruger Python {sys.version.split()[0]}",
    )
)

# 2. Virtual environment
venv_active = sys.prefix != sys.base_prefix and ".venv" in sys.prefix
results.append(
    check(
        "Virtual environment (.venv)",
        venv_active,
        "Aktivér med: source .venv/bin/activate",
    )
)

# 3. pytest
pytest_available = shutil.which("pytest") is not None
results.append(
    check(
        "pytest",
        pytest_available,
        "Installer med: python -m pip install pytest",
    )
)

# 4. Git
git_available = shutil.which("git") is not None
results.append(
    check("Git", git_available, "Installer med: sudo apt install git")
)

# 5. Projektmappe
current_dir = Path.cwd()
project_ok = current_dir.name == "udvidet-netvaerksteknologi"
results.append(
    check(
        "Projektmappe",
        project_ok,
        "Kør: cd ~/udvidet-netvaerksteknologi",
    )
)

# 6. Git repository
git_repo = (current_dir / ".git").exists()
results.append(
    check(
        "Git repository",
        git_repo,
        "Opret eller clone dit GitHub repository.",
    )
)

# 7. Helloworld.py
hello_file = current_dir / "Helloworld.py"
results.append(
    check(
        "Helloworld.py",
        hello_file.exists(),
        "Læg Helloworld.py i projektmappen.",
    )
)

print()
print("-" * 60)
passed = sum(results)
total = len(results)

if passed == total:
    print(f" ALT OK - {passed}/{total} tests bestået!")
    print(" Dit udviklingsmiljø er klar.")
else:
    print(f" {passed}/{total} tests bestået.")
    print()
    print(" Ret fejlene markeret med [FEJL] og kør testen igen.")

print("-" * 60)
print()