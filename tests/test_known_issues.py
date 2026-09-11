import re

import pytest
from playwright.sync_api import Page


@pytest.mark.known_issue
@pytest.mark.xfail(
    reason="Visible footer phone number differs from the tel: link target (site defect)",
    strict=True,
)
def test_footer_phone_text_matches_link(page: Page, base_url: str) -> None:
    page.goto(base_url)
    phone = page.locator("a[href^='tel:']").first
    visible_digits = "".join(re.findall(r"\d", phone.inner_text()))
    target_digits = "".join(re.findall(r"\d", phone.get_attribute("href") or ""))
    assert visible_digits == target_digits
