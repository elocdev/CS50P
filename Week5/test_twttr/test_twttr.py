from twttr import shorten

def test_shorten():
    assert shorten("testing") == "tstng"
    assert shorten("this is my tweet!") == "ths s my twt!"
    assert shorten("CAPITALIZED") == "CPTLZD"
    assert shorten("someword123") == "smwrd123"