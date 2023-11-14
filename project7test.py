import pytest
from project7implement import Starship, XWing, TIEFighter, HyperdriveFailureError, ShieldFailureError, SublightEngineError

def test_starship_instantiation():
    xwing = XWing("Test XWing")
    tie_fighter = TIEFighter("Test TIE Fighter")
    assert xwing.name == "Test XWing"
    assert tie_fighter.name == "Test TIE Fighter"
    assert xwing.sublight_engines_operational == True
    assert tie_fighter.sublight_engines_operational == True

def test_status_report(capsys):
    red_five = XWing("Red Five")
    red_five.shields = False
    red_five.status_report()
    captured = capsys.readouterr()
    assert "Shields=Down" in captured.out

def test_is_fully_operational():
    xwing = XWing("Test XWing")
    tie_fighter = TIEFighter("Test TIE Fighter")
    assert xwing.is_fully_operational() == True
    xwing.shields = False
    assert xwing.is_fully_operational() == False
    assert tie_fighter.is_fully_operational() == True

def test_shield_failure_exception():
    xwing = XWing("Test XWing")
    xwing.shields = False
    with pytest.raises(ShieldFailureError):
        if not xwing.shields:
            raise ShieldFailureError(f"{xwing.name} has a shield failure.")

def test_no_sublight_engine_exception():
    tie_fighter = TIEFighter("Test TIE Fighter")
    tie_fighter.sublight_engines_operational = False
    with pytest.raises(SublightEngineError):
        if not tie_fighter.is_fully_operational():
            raise SublightEngineError(f"{tie_fighter.name} is not fully operational due to sublight engine failure.")
