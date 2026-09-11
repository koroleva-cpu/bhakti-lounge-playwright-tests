import re

import pytest
from playwright.sync_api import Page, expect

from pages.base_page import BasePage

MAIN_PAGES = {
    "home": "/",
    "our-story": "/our-story/",
    "whats-on": "/whats-on/",
    "event-booking": "/event-booking/",
    "food": "/food/",
    "community": "/community/",
    "find-us": "/find-us/",
}

SOCIAL_NETWORKS = {
    "instagram": r"instagram\.com",
    "facebook": r"facebook\.com",
    "tiktok": r"tiktok\.com",
}


@pytest.mark.regression
@pytest.mark.social
@pytest.mark.parametrize("page_name,path", MAIN_PAGES.items(), ids=MAIN_PAGES.keys())
@pytest.mark.parametrize(
    "network,domain_pattern",
    SOCIAL_NETWORKS.items(),
    ids=SOCIAL_NETWORKS.keys(),
)
def test_social_network_opens_from_every_main_page(
    page: Page,
    base_url: str,
    page_name: str,
    path: str,
    network: str,
    domain_pattern: str,
) -> None:
    site_page = BasePage(page, base_url)
    site_page.open(path)
    social_link = site_page.social_link(network)

    expect(social_link).to_be_visible()
    expect(social_link).to_have_attribute("target", "_blank")

    with page.expect_popup() as popup_info:
        social_link.click()

    social_page = popup_info.value
    try:
        social_page.wait_for_url(
            re.compile(rf"https?://(www\.)?{domain_pattern}/"),
            wait_until="commit",
            timeout=10_000,
        )
    finally:
        social_page.close()
