from environments import Page, expect
from environments import base_url

#AT en notering med fritext har sparats  
 
#Testscenario: 
#Surfa till websidan 
#Klicka på Add Note 
#Klicka på inmatningsfält 
#Skriv in valfri text 
#Klicka Add Note 

def test_add_note(page: Page):
    page.goto(base_url)

    button_locator = page.get_by_role("button")
    button_add_note = button_locator.get_by_text("Add note")
    button_add_note.click()

    page.get_by_text("Click to change text").click()
    page.locator("input").fill("testtext nr 1")

    expect(page.locator("input")).to_be_visible()
  