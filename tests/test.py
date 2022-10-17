import time

def test_opening_social_media(navigation_menu):
    navigation_menu.open_twitter()

def test_leave_feedback(feedback):
    feedback.leave_feedback()
    time.sleep(5)