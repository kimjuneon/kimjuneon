import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def page_text(driver):
    return driver.find_element(By.TAG_NAME, "body").text


def require_page(driver, host):
    if urlsplit(driver.current_url).netloc != host or urlsplit(driver.current_url).scheme != "https":
        raise RuntimeError("Unexpected website during Programmers sign-in")
    if "request could not be satisfied" in page_text(driver).lower():
        raise RuntimeError("Programmers returned a CloudFront denial on the web page")


def fetch_record():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--lang=ko-KR")
    with webdriver.Chrome(options=options) as driver:
        driver.set_page_load_timeout(45)
        wait = WebDriverWait(driver, 25)
        driver.get("https://programmers.co.kr/account/sign_in")
        require_page(driver, "programmers.co.kr")
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=email], input[autocomplete=username], input[placeholder*='이메일']")))
        password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=password]")))
        require_page(driver, "programmers.co.kr")
        email.send_keys(os.environ["PROGRAMMERS_TOKEN_ID"])
        password.send_keys(os.environ["PROGRAMMERS_TOKEN_PW"])
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='로그인하기' or normalize-space()='Log in' or normalize-space()='Sign in']")))
        button.click()
        try:
            wait.until(lambda browser: urlsplit(browser.current_url).path != "/account/sign_in")
        except TimeoutException:
            raise RuntimeError("Programmers sign-in form did not complete; verify email login on the website") from None
        driver.get("https://school.programmers.co.kr/learn/challenges")
        require_page(driver, "school.programmers.co.kr")

        def statistics(browser):
            text = page_text(browser)
            fields = {}
            for label, unit in (("해결한 문제", "개"), ("점수", "점"), ("순위", "위")):
                match = re.search(label + r"\s*([0-9][0-9,]*)\s*" + unit, text)
                if not match:
                    return False
                fields[label] = int(match[1].replace(",", ""))
            return {"codingTest": {"solved": fields["해결한 문제"]},
                    "ranking": {"score": fields["점수"], "rank": fields["순위"]}}

        return wait.until(statistics, "Signed-in coding statistics were not visible")


def update_card(path, record, today):
    solved = record["codingTest"]["solved"]
    score = record["ranking"]["score"]
    rank = record["ranking"]["rank"]
    for value in (solved, score, rank):
        if type(value) is not int or value < 0:
            raise ValueError("Invalid Programmers statistic")
    if rank == 0:
        raise ValueError("Ranking unavailable")

    ET.register_namespace("", "http://www.w3.org/2000/svg")
    tree = ET.parse(path)
    labels = {e.get("id"): e for e in tree.iter() if e.get("id")}
    values = {"solved": f"{solved:,}개", "score": f"{score:,}점", "rank": f"{rank:,}위"}
    print(f"Programmers: {solved:,} solved, {score:,} points, rank {rank:,}")
    if all(labels[key].text == text for key, text in values.items()):
        return
    for key, text in values.items():
        labels[key].text = text
    labels["updated"].text = today.strftime("%Y.%m.%d 기준")
    labels["desc"].text = (f"{today.year}년 {today.month}월 {today.day}일 기준, "
                           f"해결한 문제 {values['solved']}, 점수 {values['score']}, 순위 {values['rank']}")
    path.write_text(ET.tostring(tree.getroot(), encoding="unicode") + "\n", encoding="utf-8")


if __name__ == "__main__":
    update_card(Path("assets/programmers.svg"), fetch_record(), datetime.now(ZoneInfo("Asia/Seoul")).date())
