import requests

def mailgun(MAILGUN_KEY, msgText):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4c0b30d5574541faaec2a8613c4f641e.mailgun.org/messages",
        auth=("api", MAILGUN_KEY),
        data={"from": "Mailgun Sandbox <postmaster@sandbox4c0b30d5574541faaec2a8613c4f641e.mailgun.org>",
              "to": "Katie <katie@mcgnly.com>",
              "subject": "Amanda Palmer said something about Berlin",
              "text": msgText})