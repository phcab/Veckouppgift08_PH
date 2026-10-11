from environments import Page, expect
from environments import base_url
  
#AT en notering med fritext har sparats och sedan tagits bort
 
#Testscenario: 
#Surfa till websidan 
#Klicka på Add Note 
#Klicka på inmatningsfält 
#Skriv in valfri text 
#Klicka på Add Note igen för att se noteringen sparad
#Klicka på delete-ikonen för noteringen
#Noteringen har tagits bort från sidan

def test_add_note_delete(page: Page):
    page.goto(base_url)

    # Klicka på Add note
    button_locator = page.get_by_role("button")
    button_add_note = button_locator.get_by_text("Add note")
    button_add_note.click()

    # Klicka i fältet och skriv text i noteringen
    page.get_by_text("Click to change text").click()
    page.locator("input").fill("testtext nr 2")

    # Spara noteringen
    button_add_note.click()

    # Hitta rätt note genom texten
    note = page.locator("div.note").filter(has_text="testtext nr 2")

    # Kontrollera att noten finns
    expect(note).to_be_visible()

    # Klicka på delete för just denna note
    click_delete = note.locator("div.icon.close")
    click_delete.click()

    # Kontrollera att noten är borta
    expect(note).not_to_be_visible()
