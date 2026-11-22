import json
import os
from datetime import datetime
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import HTTPCookieProcessor, HTTPRedirectHandler, Request, build_opener
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch_record():
    base = "https://programmers.co.kr/api/v1"
    session = build_opener(HTTPCookieProcessor(CookieJar()), NoRedirect())
    credentials = {"user": {"email": os.environ["PROGRAMMERS_TOKEN_ID"],
                            "password": os.environ["PROGRAMMERS_TOKEN_PW"]}}
    login = Request(f"{base}/account/sign-in", data=json.dumps(credentials).encode(),
                    headers={"Content-Type": "application/json", "Accept": "application/json"})
    with session.open(login, timeout=30):
        pass
    with session.open(f"{base}/users/record", timeout=30) as response:
        return json.load(response)


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
    try:
        record = fetch_record()
    except HTTPError as error:
        raise SystemExit(f"Programmers returned HTTP {error.code} at {error.filename}") from None
    update_card(Path("assets/programmers.svg"), record, datetime.now(ZoneInfo("Asia/Seoul")).date())
