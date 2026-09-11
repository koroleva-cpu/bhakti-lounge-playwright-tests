import os

import pytest
from playwright.sync_api import Page

from pages.event_booking_page import EventBookingPage
from pages.find_us_page import FindUsPage
from pages.home_page import HomePage
from pages.whats_on_page import WhatsOnPage


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.bhaktilounge.org.nz")


@pytest.fixture
def home_page(page: Page, base_url: str) -> HomePage:
    return HomePage(page, base_url)


@pytest.fixture
def whats_on_page(page: Page, base_url: str) -> WhatsOnPage:
    return WhatsOnPage(page, base_url)


@pytest.fixture
def find_us_page(page: Page, base_url: str) -> FindUsPage:
    return FindUsPage(page, base_url)


@pytest.fixture
def event_booking_page(page: Page, base_url: str) -> EventBookingPage:
    return EventBookingPage(page, base_url)
