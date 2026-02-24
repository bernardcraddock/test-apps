import runpy


def test_sample_prints_a_value(capfd):
    # execute the sample module as a script and capture stdout
    runpy.run_path("python/sample.py", run_name="__main__")
    out, err = capfd.readouterr()
    assert "a 10" in out
