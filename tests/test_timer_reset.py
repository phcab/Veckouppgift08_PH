from environments import Page
from environments import base_url
import time
import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

# User story reset timer

# Förutsättning: En timer har lagts till på sidan
#Add Timer - knappen 
#Som en användare vill jag kunna skapa en timer 
#Så att jag får möjlighet att starta en timer  
#AT en timer med möjlighet att starta visas  
#Testscenario: 
#Surfa till websidan https://lejonmanen.github.io/timer-vue/ 
#Klicka på Add Timer 
#15:00 min Break visas 
#Startknapp visas
#Starta timer
#reset

def test_add_timer_switch(page: Page):
    page.goto(base_url)

    # Lägg till två timers
    page.get_by_role("button", name="Add timer").click()
    
    # Starta timer 
    page.get_by_role("button", name="Start").click()

    time.sleep(2)

    # Kontrollera timer
    expect(page.locator("div.row.time")).to_have_text(
    re.compile(r"^14:\d{2}$")
    )

    # Reset timer 
    page.get_by_role("button", name="Reset").click()

    # Timer ska nu ha 15:00
    expect(page.locator("div.row.time")).to_have_text("15:00")

    