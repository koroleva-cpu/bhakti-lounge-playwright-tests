# Interview guide — Bhakti Lounge Playwright project

## 60-second introduction

I built a UI test automation portfolio project for the public Bhakti Lounge website using Python, Playwright and pytest. I used the Page Object Model to separate test scenarios from page-specific locators and actions. The portfolio suite covers critical navigation, event discovery, contact information, the newsletter UI, social links, Eventbrite booking links and a mobile viewport. GitHub Actions runs smoke checks sequentially in Chromium, Firefox and WebKit, plus a scheduled regression suite in Chromium. Failure evidence includes traces, screenshots and videos. Because this is a production website, the tests are non-destructive and never submit forms or create bookings.

## Architecture

> What is the difference between BasePage and HomePage?

`BasePage` contains shared browser and site behaviour, such as URL construction, navigation locators and title assertions. `HomePage` inherits that behaviour and adds only homepage-specific locators and actions, such as the hero and newsletter controls.

> Why use Page Objects?

They keep tests readable and reduce duplicated locator logic. If a page implementation changes, I usually update one Page Object instead of many tests.

> What are fixtures used for?

Pytest fixtures create reusable dependencies. The Playwright plugin provides the `page` fixture, my `base_url` fixture selects the environment, and page fixtures assemble ready-to-use Page Objects.

## Playwright

> What is Playwright?

Playwright is an open-source browser automation framework developed by Microsoft. It supports Chromium, Firefox and WebKit through one API and includes auto-waiting, isolated browser contexts, tracing, screenshots, video and network tooling.

> Why use role-based locators?

Role-based locators reflect how users and assistive technologies understand the interface. They are usually more readable and less coupled to layout than positional CSS or XPath selectors.

> What is auto-waiting?

Playwright waits for actionability conditions before interactions and retries web-first assertions until their timeout. I avoid hard-coded sleeps because they are slower and less reliable.

## Test strategy

> Why are there only a few UI tests?

UI tests are slower and more expensive than unit or API tests, so I focus them on critical user journeys. In a product team, business rules should mostly be tested at lower levels.

> Why do the tests not submit the newsletter or booking form?

The target is a real production site. Submitting test data could create spam or real bookings. Write scenarios should use an approved staging environment with disposable data.

> What does `xfail` mean here?

It records a known product defect without hiding it. I use strict mode so that if the defect is fixed, the resulting `XPASS` fails the build and tells us to review and remove the workaround.

## CI

> What is CI?

Continuous Integration automatically checks changes when code is pushed or a pull request is created. This project installs the environment, runs linting and executes smoke tests sequentially in Chromium, Firefox and WebKit through GitHub Actions. The sequential setup reduces unnecessary load on the public website.

> How do you debug CI failures?

I start with the failing job and assertion log, then inspect the uploaded Playwright trace, screenshot and video. The trace shows actions, locators, DOM snapshots and network activity around the failure.

## A debugging example

The newsletter test initially timed out while locating a textbox by the accessible name `Email Address`. I inspected the DOM and found that the label `for` attribute did not match the input `id`, and the responsive layout duplicated the input. I documented the accessibility issue and changed the Page Object to select the visible email input by its stable ID. I chose a visible filter instead of blindly using `first`, because it expresses which element the user can actually interact with.
