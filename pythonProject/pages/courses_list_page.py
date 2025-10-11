from playwright.sync_api import expect
from fixtures.base_page import BasePage

class CoursesListPage(BasePage):
    TITLE = "[data-test-id='courses-title']"
    CREATE_COURSE_BUTTON = "[data-test-id='create-course-button']"
    COURSE_CARD = "[data-test-id='course-card']"

    def check_visible_courses_title(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Courses")

    def check_visible_create_course_button(self):
        expect(self.page.locator(self.CREATE_COURSE_BUTTON)).to_be_visible()

    def check_visible_course_card(self, title, estimated_time, max_score, min_score):
        card = self.page.locator(self.COURSE_CARD)
        expect(card.locator("[data-test-id='title']")).to_have_text(title)
        expect(card.locator("[data-test-id='estimated_time']")).to_have_text(estimated_time)
        expect(card.locator("[data-test-id='max_score']")).to_have_text(max_score)
        expect(card.locator("[data-test-id='min_score']")).to_have_text(min_score)