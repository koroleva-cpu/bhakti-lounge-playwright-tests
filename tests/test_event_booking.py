import re
from urllib.parse import urlparse

import pytest
from playwright.sync_api import expect

from pages.event_booking_page import EventBookingPage

EVENTBRITE_HOSTS = {"www.eventbrite.com", "www.eventbrite.co.nz"}


@pytest.mark.regression
def test_all_visible_book_here_buttons_have_valid_eventbrite_links(
    event_booking_page: EventBookingPage,
) -> None:
    event_booking_page.open_page()
    event_booking_page.assert_loaded()
    links = event_booking_page.book_here_links.all()

    assert links, "Expected at least one visible BOOK HERE link"

    destinations = []
    for link in links:
        href = link.get_attribute("href")
        assert href is not None, "BOOK HERE link has no href"

        destination = urlparse(href)
        assert destination.scheme == "https", f"Booking link is not HTTPS: {href}"
        assert destination.netloc in EVENTBRITE_HOSTS, f"Unexpected booking host: {href}"
        assert destination.path.startswith("/e/"), f"Unexpected Eventbrite path: {href}"
        destinations.append(href)

    assert len(destinations) == len(set(destinations)), "Duplicate visible booking links found"


@pytest.mark.regression
def test_first_book_here_button_opens_eventbrite(
    event_booking_page: EventBookingPage,
) -> None:
    event_booking_page.open_page()
    first_booking = event_booking_page.book_here_links.first

    with event_booking_page.page.expect_navigation(wait_until="commit", timeout=15_000):
        first_booking.click()

    expect(event_booking_page.page).to_have_url(
        re.compile(r"https://www\.eventbrite\.(com|co\.nz)/e/")
    )
