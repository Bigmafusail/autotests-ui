from playwright.sync_api import sync_playwright, expect

# Первая часть: регистрация и сохранение состояния
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    # Открываем страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем форму регистрации
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

# Вторая часть: создание новой сессии с сохраненным состоянием и проверка страницы курсов
with sync_playwright() as playwright:
    # Создаем новую сессию браузера
    browser = playwright.chromium.launch(headless=False)
    # В контекст подставляем сохраненное состояние
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    # Открываем страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем иконку
    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    # Проверяем наличие и текст блока "There is no results"
    no_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("There is no results")

    # Проверяем наличие и текст блока "Results from the load test pipeline will be displayed here"
    no_results_block = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("Results from the load test pipeline will be displayed here")
