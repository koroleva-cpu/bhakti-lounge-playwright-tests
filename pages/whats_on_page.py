from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class WhatsOnPage(BasePage):
    PATH = "/whats-on/"

    @property
    def page_intro(self) -> Locator:
        return self.page.get_by_text("Come See What We're Up To", exact=True)

    @property
    def calendar_link(self) -> Locator:
        return self.page.get_by_role("link", name="VIEW THE CALENDAR").first

    def open_page(self) -> None:
        self.open(self.PATH)

    def assert_loaded(self) -> None:
        self.assert_title_contains("What's On")
        expect(self.page_intro).to_be_visible()
        expect(self.calendar_link).to_be_visible()
