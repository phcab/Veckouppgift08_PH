from environments import Page, expect
from environments import base_url
import time
import re
# re == reguljära uttryck == "regex"
  
#AT en timer kan startas och omstartas

#Testscenario: 
#Surfa till websidan 
#Klicka på Add Timer 
#15:00 min Break visas 
#Startknapp visas
#Starta timer
#Avvakta
#Starta om timer

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

    