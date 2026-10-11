from environments import Page, expect
from environments import base_url

#AT en notering med fritext har sparats och sedan ändrats och sparats
 
#Testscenario: 
#Surfa till websidan 
#Klicka på Add Note 
#Klicka på inmatningsfält 
#Skriv in valfri text 
#Klicka Add Note 
#Skriv in valfri text
#Klicka Add Note
#Välj en notering
#Klicka på texten
#Skriv in ny text

def test_add_note_change(page: Page):
    page.goto(base_url)

    button_add_note = page.get_by_role("button", name="Add note")
    button_add_note.click()

    first_note = page.locator("div.note").filter(has_text="Click to change text")
    first_note.get_by_role("heading", name="Click to change text").click()
    first_input = first_note.locator("input:visible")
    first_input.fill("testtext nr 5")
    page.get_by_role("button", name="Add note").click()

    second_note = page.locator("div.note").filter(has_text="Click to change text")
    second_note.get_by_role("heading", name="Click to change text").click()
    second_input = second_note.locator("input:visible")
    second_input.fill("testtext nr 6")
    page.get_by_role("button", name="Add note").click()
    
    first_note = page.locator("div.note").filter(has_text="testtext nr 5")
    first_note.get_by_role("heading", name="testtext nr 5").click()
    first_input = first_note.locator("input:visible")
    first_input.fill("ändrad testtext")
    page.get_by_role("button", name="Add note").click()

    expect(page.get_by_text("ändrad testtext")).to_be_visible()
    expect(page.get_by_text("testtext nr 6")).to_be_visible()
