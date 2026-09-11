import re
from urllib.parse import urljoin

from playwright.sync_api import Locator, Page, expect


class BasePage:
    """Shared navigation and stable site-wide elements."""

    SOCIAL_DOMAINS = {
        "instagram": "instagram.com",
        "facebook": "facebook.com",
        "tiktok": "tiktok.com",
    }

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/") + "/"

    @property
    def main_navigation(self) -> Locator:
        return self.page.locator("header, nav").first

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer").first

    def open(self, path: str = "") -> None:
        response = self.page.goto(urljoin(self.base_url, path.lstrip("/")))
        assert response is not None, "The browser did not receive an HTTP response"
        assert response.ok, f"Page returned HTTP {response.status}: {response.url}"
        self.page.wait_for_load_state("domcontentloaded")

    def assert_title_contains(self, expected: str) -> None:
        expect(self.page).to_have_title(re.compile(re.escape(expected), re.IGNORECASE))

    def navigation_link(self, name: str) -> Locator:
        return self.page.get_by_role("link", name=name, exact=True).first

    def social_link(self, network: str) -> Locator:
        """Return the accessible page link or fall back to the footer icon."""
        try:
            domain = self.SOCIAL_DOMAINS[network]
        except KeyError as error:
            raise ValueError(f"Unsupported social network: {network}") from error

        accessible_link = self.page.get_by_role(
            "link",
            name=re.compile(rf"^{re.escape(network)}$", re.IGNORECASE),
        ).filter(visible=True)
        if accessible_link.count() > 0:
            return accessible_link.first

        return self.footer.locator(f"a[href*='{domain}']").filter(visible=True)
