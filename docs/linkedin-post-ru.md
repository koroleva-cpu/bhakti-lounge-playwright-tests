# Черновик поста для LinkedIn

Собрала pet-проект по UI-автоматизации реального сайта Bhakti Lounge на Python, Playwright и pytest.

Что реализовано:

✅ Page Object Model и pytest fixtures
✅ smoke и regression suites
✅ smoke-проверки в Chromium, Firefox и WebKit
✅ мобильный viewport
✅ параллельный запуск через pytest-xdist
✅ traces, screenshots и video при падении
✅ GitHub Actions для pull requests и nightly regression
✅ проверки навигации, социальных ссылок и переходов к Eventbrite
✅ безопасный подход: тесты не отправляют формы и не создают реальные бронирования в production

Во время исследования я также обнаружила несоответствие между видимым номером телефона и адресом `tel:` в footer и зафиксировала его как known issue через strict `xfail`.

Главный вывод: хороший UI-тест проверяет пользовательское поведение, не зависит от случайной структуры DOM и оставляет достаточно данных для быстрой диагностики падения.

Сейчас ищу позицию Junior QA Automation Engineer / QA Engineer. Буду рада обратной связи по архитектуре проекта и новым профессиональным знакомствам.

Репозиторий пока private; могу предоставить доступ для review по запросу.

#Python #Playwright #Pytest #TestAutomation #QA #GitHubActions #OpenToWork

## Что приложить к посту

1. Скриншот зелёного GitHub Actions pipeline.
2. Короткий GIF локального запуска в headed mode.
3. Схему структуры проекта или скриншот trace viewer.
4. После разрешения владельца сайта — ссылку на публичный GitHub repository с аккуратным README.
