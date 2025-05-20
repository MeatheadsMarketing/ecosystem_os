
def test_classify():
    from file_classifier import classify_file
    assert classify_file("sample_viewer.py") in ["tab_ui", "tool_logic"]
