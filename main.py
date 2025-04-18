from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

import time


options = Options()
options.add_argument(r"user-data-dir=C:\chrome-automation-profile")
options.add_argument("profile-directory=Default")
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

course_require = {
    "Môn học Đạo Đức Người Lái Xe Ô Tô 2025": "8",
    "Cấu tạo và sửa chữa thông thường xe oto": "10",
    "Môn học kĩ thuật lái xe ô tô": "10",
    "Môn học Pháp Luật Giao thông Đường Bộ 2025": "63"
}

driver.get("https://hoclythuyetlaixe.eco-tek.com.vn/slides/all?my=1")
course_element = driver.find_elements(By.CLASS_NAME, "card-body")
course_time_element = driver.find_elements(By.CLASS_NAME, "card-footer")
courses = zip(course_element, course_time_element)

for index, (course, time_spent) in enumerate(courses):
    if(course.text not in course_require): continue

    time_already_spent = 0
    if time_spent and time_spent.text.strip():
        match = re.search(r"(\d+)\s*giờ", time_spent.text)
        time_already_spent = int(match.group(1))
    
    if(time_already_spent < int(course_require[course.text])):
        print("Chua du mon ",course.text, " voi so gio ", time_spent.text, index)
        course_element[index].click()
        break

lesson_elements = driver.find_elements(By.CLASS_NAME, "o_wslides_slides_list_slide")

for lesson in lesson_elements:
    lesson_link = lesson.find_elements(By.CLASS_NAME, "o_wslides_js_slides_list_slide_link")
    lesson_percent = lesson.find_elements(By.CLASS_NAME, "badge ")
    if lesson_link and lesson_percent:
        if(lesson_percent[0].text != "100 %"):
            print(lesson_link[0].text, lesson_percent[0].text)
            break

input("Press Enter to quit")