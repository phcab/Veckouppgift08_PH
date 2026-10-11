import pytest
from environments import base_url
from environments import Page, expect

##Testscenario: 
#Surfa till websidan 
#Klicka på den knapp som representerat temat du önskar
#Light, Dark, Forest, Orange, Christmas
#Valt tema visas

@pytest.mark.parametrize(
"theme",
["Light", "Dark", "Forest", "Orange", "Christmas"]
)
def test_change_theme(page: Page, theme: str):
    page.goto(base_url)

    body = page.locator("body")

    # Börja med ett annat tema än det som ska testas
    if theme == "Light":
        page.get_by_role("button", name="Dark").click()

    color_before = body.evaluate(
        "(el) => getComputedStyle(el).backgroundColor"
    )

    page.get_by_role("button", name=theme).click()

    expect(body).not_to_have_css(
        "background-color", color_before
    )