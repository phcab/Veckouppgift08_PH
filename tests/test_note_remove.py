from environments import Page
from environments import base_url
import time
import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

#Add Note - knappen 
#Som en användare vill jag kunna lägga till en notering  
 
#AT en notering med fritext har sparats  
 
#Testscenario B: 
#Surfa till websidan https://lejonmanen.github.io/timer-vue/ 
#Klicka på Add Note 
#Klicka på inmatningsfält 
#Skriv in valfri text 
#Klicka på delete-ikonen för noteringen
#Noteringen ska tas bort från sidan

#div.icon.close (delete)

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
