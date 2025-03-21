import pytest
import os
import tempfile
import sys
from src.coverage_utils.get_coverage import update_coverage_badge, main

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
def invalid_coverage_xml():
    content = '''<?xml version="1.0" ?>
    <coverage line-rate="invalid">
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

def test_update_coverage_badge_different_formats(tmp_path):
    # Test with different README badge formats
    different_format = tmp_path / "different_readme.md"
    different_format.write_text("# Project\n![Coverage](old_badge.svg)")
    assert update_coverage_badge(75, str(different_format)) == True
    assert "coverage-75%25-brightgreen.svg" in different_format.read_text()

def test_update_coverage_badge_io_error(tmp_path):
    # Test file permission error
    readme_path = tmp_path / "readme.md"
    readme_path.write_text("# Project\n[![Coverage](old_badge.svg)](link)")
    os.chmod(str(readme_path), 0o600)  # Make file owner read/write only
    assert update_coverage_badge(85, str(readme_path)) == False

def test_main_success(sample_coverage_xml, sample_readme, monkeypatch):
    # Test successful execution
    testargs = ["prog", "--coverage-xml", sample_coverage_xml, "--readme", sample_readme]
    monkeypatch.setattr(sys, 'argv', testargs)
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0

def test_main_invalid_xml(invalid_coverage_xml, sample_readme, monkeypatch):
    # Test with invalid XML
    testargs = ["prog", "--coverage-xml", invalid_coverage_xml, "--readme", sample_readme]
    monkeypatch.setattr(sys, 'argv', testargs)
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

def test_main_invalid_coverage(sample_readme, monkeypatch):
    # Test invalid coverage value handling
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.xml') as f:
        f.write('<?xml version="1.0" ?><coverage line-rate="1.5"></coverage>')
        xml_path = f.name
    
    try:
        testargs = ["prog", "--coverage-xml", xml_path, "--readme", sample_readme]
        monkeypatch.setattr(sys, 'argv', testargs)
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1
    finally:
        os.unlink(xml_path)

def test_main_missing_args(monkeypatch):
    # Test missing arguments
    testargs = ["prog"]
    monkeypatch.setattr(sys, 'argv', testargs)
    with pytest.raises(SystemExit):
        main()

def test_coverage_range():
    # Test different coverage percentages
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
        f.write("# Project\n[![Coverage](old_badge.svg)](link)")
        temp_path = f.name
    
    try:
        for coverage in [0, 50, 100]:
            assert update_coverage_badge(coverage, temp_path) == True
            with open(temp_path) as f:
                content = f.read()
            assert f"coverage-{coverage}%25-brightgreen.svg" in content
    finally:
        os.unlink(temp_path)
