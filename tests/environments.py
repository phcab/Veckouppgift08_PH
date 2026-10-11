import time
import re
# re == reguljära uttryck == "regex"

from playwright.sync_api import Page, expect

base_url = "https://lejonmanen.github.io/timer-vue/"

# Vanligt smoke test
def test_has_title(page: Page):
    page.goto(base_url)
    # TODO: flytta page.goto till en gemensam funktion i environment.py i stället - nästa vecka

    expect(page).to_have_title(re.compile("Timer app"))
    print ("Sidan har rätt titel")