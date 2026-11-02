from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_fail_example():
    # This is a dummy test. 
    # If you change '5' to '6', the pipeline will fail!
    assert add(2, 2) == 4