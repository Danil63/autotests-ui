from playwright.sync_api import expect
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    TITLE = "[data-test-id='create-course-title']"
    CREATE_BUTTON = "[data-test-id='create-course-button']"
    IMAGE_PREVIEW_EMPTY = "[data-test-id='image-preview-empty-view']"
    IMAGE_UPLOAD_VIEW = "[data-test-id='image-upload-view']"
    FORM = "[data-test-id='create-course-form']"
    EXERCISES_TITLE = "[data-test-id='exercises-title']"
    CREATE_EXERCISE_BUTTON = "[data-test-id='create-exercise-button']"
    EXERCISES_EMPTY_VIEW = "[data-test-id='exercises-empty-view']"
    FILE_INPUT = "[data-test-id='upload-input']"

    def check_visible_create_course_title(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Create course")

    def check_disabled_create_course_button(self):
        expect(self.page.locator(self.CREATE_BUTTON)).to_be_disabled()

    def check_visible_image_preview_empty_view(self):
        expect(self.page.locator(self.IMAGE_PREVIEW_EMPTY)).to_be_visible()

    def check_visible_image_upload_view(self, is_image_uploaded=False):
        locator = self.page.locator(self.IMAGE_UPLOAD_VIEW)
        expect(locator).to_be_visible()
        if is_image_uploaded:
            expect(locator).to_have_text("Uploaded successfully")
        else:
            expect(locator).to_have_text("Upload image")

    def check_visible_create_course_form(self, title, description, estimated_time, max_score, min_score):
        form = self.page.locator(self.FORM)
        expect(form.locator("input[name='title']")).to_have_value(title)
        expect(form.locator("textarea[name='description']")).to_have_value(description)
        expect(form.locator("input[name='estimated_time']")).to_have_value(estimated_time)
        expect(form.locator("input[name='max_score']")).to_have_value(max_score)
        expect(form.locator("input[name='min_score']")).to_have_value(min_score)

    def check_visible_exercises_title(self):
        expect(self.page.locator(self.EXERCISES_TITLE)).to_have_text("Exercises")

    def check_visible_create_exercise_button(self):
        expect(self.page.locator(self.CREATE_EXERCISE_BUTTON)).to_be_visible()

    def check_visible_exercises_empty_view(self):
        expect(self.page.locator(self.EXERCISES_EMPTY_VIEW)).to_be_visible()

    def upload_preview_image(self, file_path):
        self.page.locator(self.FILE_INPUT).set_input_files(file_path)

    def fill_create_course_form(self, title, estimated_time, description, max_score, min_score):
        self.page.fill("input[name='title']", title)
        self.page.fill("input[name='estimated_time']", estimated_time)
        self.page.fill("textarea[name='description']", description)
        self.page.fill("input[name='max_score']", max_score)
        self.page.fill("input[name='min_score']", min_score)

    def click_create_course_button(self):
        self.page.locator(self.CREATE_BUTTON).click()