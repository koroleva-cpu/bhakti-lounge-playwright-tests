import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.whats_on_page import WhatsOnPage


@pytest.mark.smoke
def test_home_page_has_critical_content(home_page: HomePage) -> None:
    home_page.open_page()
    home_page.assert_loaded()


@pytest.mark.smoke
def test_user_can_open_whats_on_from_home(home_page: HomePage) -> None:
    home_page.open_page()
    home_page.whats_on_call_to_action.click()

    expect(home_page.page).to_have_url(f"{home_page.base_url}whats-on/")
    WhatsOnPage(home_page.page, home_page.base_url).assert_loaded()


@pytest.mark.smoke
def test_primary_navigation_targets_exist(home_page: HomePage) -> None:
    home_page.open_page()

    expected_paths = {
        "Our Story": "/our-story/",
        "What's On": "/whats-on/",
        "Event Booking": "/event-booking/",
        "Food": "/food/",
        "Community": "/community/",
        "Find Us": "/find-us/",
    }
    for name, path in expected_paths.items():
        expect(home_page.navigation_link(name)).to_have_attribute("href", path)
