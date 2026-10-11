from environments import Page, expect
from environments import base_url
 
#AT två noteringar med fritext har sparats och sedan bytt plats
 
#Testscenario: 
#Surfa till websidan 
#Klicka på Add Note 
#Klicka på inmatningsfält 
#Skriv in valfri text 
#Klicka på Add Note
#Skriv in valfri text
#Klicka på Add Note
#Välj den senaste noteringen
#Klicka på ikonen med pil upp
#Ordningen på noteringarna är ändrad

def test_add_note_switch(page: Page):
    page.goto(base_url)

    # Klicka på Add note
    button_locator = page.get_by_role("button")
    button_add_note = button_locator.get_by_text("Add note")
    button_add_note.click()

    inputs = page.get_by_placeholder("Description")

    # Klicka i fältet och skriv text i noteringen
    page.get_by_text("Click to change text").click()
    inputs.nth(0).fill("testtext nr 3")

    # Spara noteringen
    button_add_note.click()

    # Klicka i fältet och skriv text i noteringen
    page.get_by_text("Click to change text").click()
    inputs.nth(1).fill("testtext nr 4")

     # Spara noteringen
    button_add_note.click()

    # Hitta rätt note genom texten
    note3 = page.locator("div.note").filter(has_text="testtext nr 3")
    note4 = page.locator("div.note").filter(has_text="testtext nr 4")
    
    #div.icon.up (flytta upp)
    note4.locator("div.icon.up").click()

    # Kontrollera att noten finns och att den ligger ovanför noten med texten "testtext nr 3"    
    notes = page.locator("div.note")

    expect(notes.nth(0)).to_contain_text("testtext nr 4")
    expect(notes.nth(1)).to_contain_text("testtext nr 3")



  
    
    