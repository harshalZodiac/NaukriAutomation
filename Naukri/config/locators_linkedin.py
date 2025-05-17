class LinkedInLoginLocators:
    USERNAME = '[id="username"]'
    PASSWORD = '[id="password"]'
    SIGN_IN = '[aria-label="Sign in"]'
    KEEP_ME_LOGGED_IN = '[id="rememberMeOptIn-checkbox"]'

class LinkedInProfileLocators:
    FEED_PAGE_PROFILE_SECTION = '[class="profile-card-member-details"]'
    EDIT_BUTTON = '[href="#edit-medium"]'
    SAVE_PROFILE = '[data-view-name="profile-form-save"]'

class LinkedInJobSearchLocators:
    JOB_SECTION = '[type="job"]'
    JOB_TITLE= '[role="combobox"]'
    JOB_SECTION_SIDE_BAR = '[class="jobs-home-scalable-nav"]'
    DATE_POSTED_FILTER_OPTIONS = '[aria-label="Date posted filter. Clicking this button displays all Date posted filter options."]'
    DATE_POSTED_LAST_ONE_DAY = '//span[text()="Past 24 hours"]'
    APPLY_DATE_POSTED_FILTER = '[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml2"]'
    EASY_APPLY_FILTER = '[id="searchFilter_applyWithLinkedin"]'

class LinkedInApplicationLocators:
    JOB_POST = '[data-view-name="job-card"]'
    APPLY_BUTTON = '[id="jobs-apply-button-id"]'
    NEXT_BUTTON = '//span[@class="artdeco-button__text" and text()="Next"]'
    MANDATORY_NOT_FILLED_ERROR = 'li-icon[type="error-pebble-icon"]'
    REVIEW_BUTTON = '//span[@class="artdeco-button__text" and text()="Review"]'
    SUBMIT_APPLICATION = '//span[@class="artdeco-button__text" and text()="Submit application"]'
    CLOSE_APPLICATION = '[data-test-icon="close-medium"]'
    DONE_WITH_APPLICATION = '//span[text()="Done"]'
    SAVE_JOB = '//span[text()="Save"]'
    ALREADY_APPLIED = '[class="artdeco-inline-feedback__message"]'
    TERMS_AND_CONDITIONS = '[data-test-text-selectable-option__label="I Agree Terms & Conditions"]'