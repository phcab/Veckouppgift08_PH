import pytest
from environments import Page
from environments import base_url
import time
import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

#
#
#

#Light, Dark, Forest, Orange, Christmas
#div.data.component "Select theme"

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