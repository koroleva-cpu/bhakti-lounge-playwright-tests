import pytest
from playwright.sync_api import Page, expect

from pages.find_us_page import FindUsPage
from pages.home_page import HomePage

pytestmark = pytest.mark.learning


def test_home_page_opens(page: Page) -> None:
    page.goto("https://www.bhaktilounge.org.nz/")

    expect(page).to_have_title("Homepage - Bhakti Lounge")


def test_user_can_open_whats_on_page(page: Page) -> None:
    page.goto("https://www.bhaktilounge.org.nz/")

    whats_on_link = page.get_by_role(
        "link",
        name="SEE WHAT'S ON",
    ).filter(visible=True)

    expect(whats_on_link).to_be_visible()

    whats_on_link.click()

    expect(page).to_have_url("https://www.bhaktilounge.org.nz/whats-on/")


def test_home_page_using_page_object(
    page: Page,
    base_url: str,
) -> None:
    home_page = HomePage(page, base_url)

    home_page.open_page()

    home_page.assert_loaded()


def test_home_page_using_fixture(home_page: HomePage) -> None:
    home_page.open_page()

    home_page.assert_loaded()


def test_find_us_page_displays_contact_information(find_us_page: FindUsPage) -> None:
    find_us_page.open_page()
    find_us_page.assert_loaded()


def test_user_can_fill_newsletter_email_without_submitting(
    home_page: HomePage,
) -> None:
    home_page.open_page()

    email_input = home_page.newsletter_email
    submit_button = home_page.newsletter_submit

    expect(email_input).to_be_visible()
    email_input.fill("qa@example.com")

    expect(email_input).to_have_value("qa@example.com")
    expect(submit_button).to_be_enabled()
