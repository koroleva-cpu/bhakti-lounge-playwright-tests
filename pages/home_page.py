from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class HomePage(BasePage):
    PATH = "/"

    @property
    def hero_text(self) -> Locator:
        return self.page.get_by_text(
            "Welly's Event Space",
            exact=True,
        ).filter(visible=True)

    @property
    def whats_on_call_to_action(self) -> Locator:
        return self.page.get_by_role("link", name="SEE WHAT'S ON")

    @property
    def newsletter_email(self) -> Locator:
        return self.page.locator("#bhakti-newsletter-email").filter(visible=True)

    @property
    def newsletter_submit(self) -> Locator:
        return self.page.get_by_role("button", name="SIGN ME UP")

    def open_page(self) -> None:
        self.open(self.PATH)

    def assert_loaded(self) -> None:
        self.assert_title_contains("Bhakti Lounge")
        expect(self.hero_text).to_be_visible()
        expect(self.whats_on_call_to_action).to_be_visible()
