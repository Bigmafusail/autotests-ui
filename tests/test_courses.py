import pytest
from playwright.sync_api import expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    """Тест для проверки пустого списка курсов"""
    page = chromium_page_with_state
    
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
    no_results_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_results_description).to_be_visible()
    expect(no_results_description).to_have_text("Results from the load test pipeline will be displayed here")
