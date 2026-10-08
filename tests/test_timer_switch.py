from environments import Page
from environments import base_url
import time
import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

# User story ta bort timer 

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
#Pausa timer
#Lägg till en timer
#Byt plats på timern

def test_add_timer_switch(page: Page):
    page.goto(base_url)

    # Lägg till två timers
    page.get_by_role("button", name="Add timer").click()
    page.get_by_role("button", name="Add timer").click()

    # Hämta timers efter att de skapats
    timers = page.locator("div.timer")
    timer_1 = timers.nth(0)
    timer_2 = timers.nth(1)

    # Starta timer 1
    timer_1.get_by_role("button", name="Start").click()

    time.sleep(10)

    # Pausa timer 1
    timer_1.get_by_role("button", name="Pause").click()

    # Spara timer 1:s tid, t.ex. 14:50
    timer_1_time = timer_1.locator("div.row.time").inner_text()

    # Flytta timer 2 upp
    timer_2.locator("div.icon.up").click()

    # Hämta timers igen efter omordningen
    timers = page.locator("div.timer")

    first_timer = timers.nth(0)
    second_timer = timers.nth(1)

    # Timer 2 ska nu ligga först och ha 15:00
    expect(first_timer.locator("div.row.time")).to_have_text("15:00")

    # Timer 1 ska nu ligga på andra platsen
    expect(second_timer.locator("div.row.time")).to_have_text(timer_1_time)