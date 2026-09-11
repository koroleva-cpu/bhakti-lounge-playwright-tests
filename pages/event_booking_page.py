from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class EventBookingPage(BasePage):
    PATH = "/event-booking/"

    @property
    def book_here_links(self) -> Locator:
        return self.page.get_by_role("link", name="BOOK HERE", exact=True).filter(visible=True)

    def open_page(self) -> None:
        self.open(self.PATH)

    def assert_loaded(self) -> None:
        self.assert_title_contains("Event Booking")
        expect(self.book_here_links.first).to_be_visible()
