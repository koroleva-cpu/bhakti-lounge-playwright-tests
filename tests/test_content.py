import pytest
from playwright.sync_api import expect

from pages.find_us_page import FindUsPage
from pages.home_page import HomePage
from pages.whats_on_page import WhatsOnPage


@pytest.mark.regression
def test_whats_on_page_exposes_calendar(whats_on_page: WhatsOnPage) -> None:
    whats_on_page.open_page()
    whats_on_page.assert_loaded()
    expect(whats_on_page.calendar_link).to_have_attribute("href", "/calendar/")


@pytest.mark.regression
def test_find_us_shows_contact_details_and_map(find_us_page: FindUsPage) -> None:
    find_us_page.open_page()
    find_us_page.assert_loaded()


@pytest.mark.regression
def test_newsletter_has_email_field_and_submit_button(home_page: HomePage) -> None:
    """Checks the form UI without submitting data to the production website."""
    home_page.open_page()
    expect(home_page.newsletter_email).to_be_visible()
    expect(home_page.newsletter_submit).to_be_enabled()


@pytest.mark.mobile
@pytest.mark.regression
def test_home_hero_is_visible_on_mobile(page, base_url: str) -> None:
    page.set_viewport_size({"width": 390, "height": 844})
    home = HomePage(page, base_url)
    home.open_page()
    expect(home.hero_text).to_be_visible()
