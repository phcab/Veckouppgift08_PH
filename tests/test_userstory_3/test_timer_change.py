from environments import Page, expect
from environments import base_url
import time
import re
#re == reguljära uttryck == "regex"
 
#AT en timer har lagts till och är ändrat till Counting up
 
#Testscenario: 
#Surfa till websidan 
#Klicka på Add Timer 
#15:00 min visas som start för timer
#Välj ikon och ändra till Counting up
#00:00 min visas som start för timer

def test_timer_change(page: Page):
    page.goto(base_url)

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
     