from environments import Page, expect
from environments import base_url
import re
import pytest

# Vanligt smoke test
@pytest.mark.smoke
def test_has_title(page: Page):
    page.goto(base_url)
    # TODO: flytta page.goto till en gemensam funktion i environment.py i stället - nästa vecka

    expect(page).to_have_title(re.compile("Timer app"))
    print ("Sidan har rätt titel")