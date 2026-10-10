from environments import base_url
import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

# User story -skapa timer 
#Add Timer - knappen 
#Som en användare vill jag kunna skapa en timer 
#Så att jag får möjlighet att starta en timer 
 
#AT en timer med möjlighet att starta visas  
 
#Testscenario A: 
#Surfa till websidan https://lejonmanen.github.io/timer-vue/ 
#Klicka på Add Timer 
#15:00 min Break visas 
#Startknapp visas

def test_timer_change(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

     # 1. Lägg till en timer
    page.get_by_role("button", name="Add timer").click()

    # 2. Kontrollera ursprungsvärdet
    timer = page.locator("div.row.time")
    expect(timer).to_have_text("15:00")

    # 3. Öppna timerinställningarna
    page.locator("div.icon.settings").click()

    page.locator(".ball").first.click()
   

    # 4. Hitta Counting down / Counting up
    counting_mode = page.locator("label").filter(
        has_text=re.compile(r"Counting (down|up)")
    )

    # 5. Kontrollera att kontrollen nu är synlig
    expect(counting_mode).to_be_visible()

    # 6. Växla från Counting down till Counting up
    counting_mode.click()

    # 7. Verifiera att timern börjar på 00:00
    expect(timer).to_have_text("00:00")
    
   