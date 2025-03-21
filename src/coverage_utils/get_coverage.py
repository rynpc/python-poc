import xml.etree.ElementTree as ET
import sys
import argparse
import re

def update_coverage_badge(coverage_value, readme_path):
    badge_url = f"https://img.shields.io/badge/coverage-{coverage_value}%25-brightgreen.svg"
    
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
        
        new_content = re.sub(
            r'\[!\[Coverage\]\([^)]*\)\]\([^)]*\)',
            f'[![Coverage]({badge_url})](https://rynpc.github.io/python-poc/)',
            content
        )
        
        with open(readme_path, 'w') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error updating README: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--coverage-xml', required=True)
    parser.add_argument('--readme', required=True)
    args = parser.parse_args()

    try:
        tree = ET.parse(args.coverage_xml)
        root = tree.getroot()
        coverage = int(float(root.attrib["line-rate"]) * 100)
        
        if coverage < 0 or coverage > 100:
            raise ValueError("Coverage must be between 0 and 100")
        
        if update_coverage_badge(coverage, args.readme):
            print(coverage)
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error processing coverage: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
