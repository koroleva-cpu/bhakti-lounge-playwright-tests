# Bug reports

## BL-001 — Footer phone text and call target do not match

**Severity:** Medium  
**Status:** Reproducible  
**Area:** Site-wide footer

### Steps to reproduce

1. Open `https://www.bhaktilounge.org.nz/`.
2. Scroll to the footer.
3. Compare the visible phone number with the `href` of the phone link.

### Actual result

- Visible text: `+642041915046`
- Link target: `tel:+642041915064`

### Expected result

The visible phone number and `tel:` target should contain the same digits.

### Impact

A user clicking the link may call a different number from the one shown. The automated regression is recorded as a strict `xfail`, so an unexpected fix produces `XPASS` and prompts review.

## BL-002 — Newsletter label is not associated with the email field

**Severity:** Medium  
**Status:** Reproducible  
**Area:** Homepage newsletter

### Steps to reproduce

1. Open the homepage.
2. Inspect the newsletter email input and its label.
3. Compare the input `id` with the label `for` attribute.

### Actual result

```html
<input id="bhakti-newsletter-email" type="email">
<label for="e-form-email">Email Address:</label>
```

The values do not match, so the input has no accessible name derived from this label. Responsive markup also creates duplicate input IDs in the DOM.

### Expected result

The label `for` value should match one unique input `id`.

### Impact

Screen-reader users may not receive a useful label for the field. Role-based automation cannot locate it by the expected accessible name and must use a scoped implementation locator as a temporary workaround.

## BL-003 — Two event cards share one Eventbrite destination

**Severity:** High
**Status:** Fixed and retested (2026-09-28)
**Area:** Event Booking

### Steps to reproduce

1. Open `https://www.bhaktilounge.org.nz/event-booking/`.
2. Find the cards titled `Immersive Yoga: Oceanic Flow` and `Lessons from Anxiety`.
3. Compare the destinations of their visible `BOOK HERE` links.

### Actual result

Both cards link to the Eventbrite page for `Immersive Yoga: Oceanic Flow`.

### Expected result

Each event card should link to the Eventbrite page for its own event.

### Impact

A user attempting to book `Lessons from Anxiety` is sent to a different event. The uniqueness check is recorded as a strict `xfail`, so a site fix produces `XPASS` and prompts review.

### Retest

Retested on 2026-09-28: each event card now links to its own Eventbrite page. The strict `xfail` produced `XPASS`, confirming the fix. The uniqueness check was returned to the regular booking-link test in `tests/test_event_booking.py` as a regression guard.