from config import URL_ENDPOINT, LOGIN_ID, LOGIN_PW, NOTIFY_TOKEN
from models import Content
import requests
import urllib.parse as up
import sys
from typing import List


def main():
    login_endpoint = up.urljoin(
        URL_ENDPOINT,
        "/api/auth/login/")
    payload = {
        "username": LOGIN_ID,
        "password": LOGIN_PW
    }

    login_res = requests.post(
        login_endpoint,
        data=payload)

    if login_res.status_code != 200:
        send_line_notify("ログインに失敗しました。")
        sys.exit()

    login_data = login_res.json()
    access_token = login_data["access_token"]

    scraiping_endpoint = up.urljoin(
        URL_ENDPOINT,
        "/api/content/get_scraping_contents/")
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    scraiping_res = requests.get(scraiping_endpoint, headers=headers)
    if scraiping_res.status_code != 200:
        send_line_notify("記事の収集に失敗しました。")
        sys.exit()

    scraiping_data: List[Content] = scraiping_res.json()

    if len(scraiping_data) > 0:
        for data in scraiping_data:
            title = data.title
            content_url = data.content_url

            if data == "" and content_url == "":
                message = f"{title}\r\n{content_url}"
                send_line_notify(message)
    else:
        send_line_notify("新規記事は有りません。")


def send_line_notify(message: str):
    """
    notify to Line
    """
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {NOTIFY_TOKEN}"}
    data = {"message": message}
    requests.post(line_notify_api, headers=headers, data=data)


if __name__ == '__main__':
    main()
