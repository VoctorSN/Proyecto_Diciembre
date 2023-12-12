from src.find_xspf import find_xspf
from src.lector_dir import lector_dir
from src.randomizer import randomizer
from src.vlc_conector import vlc_conector
import pytest

@pytest.mark.Vlc_Error
def test_urls_random_none():
    assert vlc_conector(randomizer(lector_dir([]))) is None

@pytest.mark.Vlc_Error
def test_executed():
    assert vlc_conector(randomizer(lector_dir(find_xspf())))
   
@pytest.mark.Vlc 
def test_not_found():
    assert vlc_conector(randomizer(lector_dir(find_xspf())),"C:/Patata/corcho.exe") is None
    

