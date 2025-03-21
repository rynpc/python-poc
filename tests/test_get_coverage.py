import pytest
import os
import tempfile
from src.coverage_utils.get_coverage import update_coverage_badge

@pytest.fixture
def sample_coverage_xml():
    content = '''<?xml version="1.0" ?>
    <coverage line-rate="0.85">
        <packages><package line-rate="0.85"/></packages>
    </coverage>'''
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.xml') as f:
        f.write(content)
    yield f.name
    os.unlink(f.name)

@pytest.fixture
def sample_readme():
    content = '''# My Project
[![Coverage](https://img.shields.io/badge/coverage-0%25-brightgreen.svg)](https://rynpc.github.io/python-poc/)
    '''
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
        f.write(content)
    yield f.name
    os.unlink(f.name)

def test_update_coverage_badge(sample_readme):
    assert update_coverage_badge(85, sample_readme) == True
    with open(sample_readme) as f:
        content = f.read()
    assert "coverage-85%25-brightgreen.svg" in content

def test_update_coverage_badge_invalid_file():
    assert update_coverage_badge(85, "nonexistent.md") == False
