from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class FindUsPage(BasePage):
    PATH = "/find-us/"

    @property
    def address(self) -> Locator:
        return self.page.get_by_text("175 Vivian Street", exact=False).first

    @property
    def map_frame(self) -> Locator:
        return self.page.locator("iframe[src*='maps.google.com']").first

    @property
    def email_link(self) -> Locator:
        return self.page.locator("a[href^='mailto:']").first

    def open_page(self) -> None:
        self.open(self.PATH)

    def assert_loaded(self) -> None:
        self.assert_title_contains("Find Us")
        expect(self.address).to_be_visible()
        expect(self.email_link).to_have_attribute("href", "mailto:bhakti.lounge.nz@gmail.com")
        expect(self.map_frame).to_be_attached()
