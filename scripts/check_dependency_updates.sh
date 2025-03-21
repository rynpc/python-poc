#!/bin/bash
set -e

# Check for outdated dependencies
pip list --outdated > outdated_dependencies.txt

# Backup current requirements
cp requirements.txt requirements_backup.txt

# Update dependencies in a temporary file
pip install pip-tools
pip-compile --upgrade > requirements_updated.txt

# Check for vulnerabilities in current dependencies
echo "Checking for vulnerabilities in current dependencies..."
safety scan --file requirements.txt --full-report > current_vulnerabilities.txt

# Check for vulnerabilities in updated dependencies
echo "Checking for vulnerabilities in updated dependencies..."
safety scan --file requirements_updated.txt --full-report > updated_vulnerabilities.txt

# Compare vulnerabilities
if diff current_vulnerabilities.txt updated_vulnerabilities.txt > /dev/null; then
    echo "No new vulnerabilities found. Applying updates..."
    mv requirements_updated.txt requirements.txt
else
    echo "New vulnerabilities detected. Reverting to original dependencies..."
    mv requirements_backup.txt requirements.txt
    rm requirements_updated.txt
    exit 1
fi

# Clean up
rm requirements_backup.txt outdated_dependencies.txt current_vulnerabilities.txt updated_vulnerabilities.txt