# Test strategy

## Scope

The suite covers public, non-destructive user journeys on `bhaktilounge.org.nz`:

- homepage availability and critical content;
- primary navigation destinations;
- What's On discovery flow and calendar entry point;
- location, email and embedded map;
- newsletter controls without sending production data;
- a representative mobile viewport;
- Instagram, Facebook and TikTok opening in a new tab from all seven main pages;
- validation of every visible BOOK HERE destination and a representative Eventbrite navigation;
- one documented known issue in the footer phone link.

Educational tests are marked `learning` and kept out of portfolio CI runs.

## Test pyramid and risks

This repository can only observe the public UI, so it deliberately contains end-to-end tests. In a product team, most business rules should be covered below the UI through unit and API tests. UI coverage should stay focused on critical journeys.

The site has duplicated desktop/mobile markup and frequently changing event content. Tests therefore avoid event names and positional CSS selectors. Assertions target accessible roles, stable calls to action and URL contracts.

## Environments

`BASE_URL` defaults to production and can point to a staging deployment. Any test that submits, books, purchases or emails must run only against an approved test environment with disposable data.

## CI policy

- Pull requests: smoke suite in Chromium and Firefox, plus Ruff.
- Weekdays: full regression in Chromium with two parallel workers to avoid overloading the public site.
- Failure evidence: Playwright trace, screenshot and video uploaded as artifacts.
- Recommended branch rule: require `smoke (chromium)`, `smoke (firefox)` and `lint` before merge.

## Known issue

The footer displays `+642041915046`, while the `tel:` target is `+642041915064`. The strict `xfail` test records the defect. If the site is fixed, XPASS fails the build and prompts removal of the workaround.
