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
#Klicka Add Note 

def test_add_note(page: Page):
    page.goto(base_url)

    button_locator = page.get_by_role("button")
    button_add_note = button_locator.get_by_text("Add note")
    button_add_note.click()

    page.get_by_text("Click to change text").click()
    page.locator("input").fill("testtext nr 1")

    expect(page.locator("input")).to_be_visible()

    #print(page.locator("input").input_value()) 