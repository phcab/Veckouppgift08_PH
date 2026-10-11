from environments import Page, expect
from environments import base_url#import time
import re
# re == reguljära uttryck == "regex"
 
#AT en timer med möjlighet att starta visas  
 
#Testscenario A: 
#Surfa till websidan https://lejonmanen.github.io/timer-vue/ 
#Klicka på Add Timer 
#15:00 min Break visas 
#Startknapp visas


def test_add_timer(page: Page):
    page.goto(base_url)

    button_locator = page.get_by_role("button")
    button_add_timer = button_locator.get_by_text("Add timer")
    button_add_timer.click()

    break_text = page.get_by_text(re.compile("Break"))
    button_start = button_locator.get_by_text("Start")

    expect(break_text).to_be_visible()
    expect(button_start).to_be_visible()




 