import sys
import os
import smtplib
import requests
from email.mime.multipart import MIMEMultipart as mmp
from email.mime.text import MIMEText as mmt
from email_validator import validate_email, EmailNotValidError
from newsapi import NewsApiClient


def main():
    """main function"""
    recipient, api = check_cla()
    send_email(recipient, api)


def check_cla():
    """function to check user input arguments"""
    possible_apis = ["news", "dict"]

    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        sys.exit(
            """\n\33[1m\33[101mUsage:\33[0m python script.py <email> <news|dict>\n
            """
        )

    if len(sys.argv) != 3 or sys.argv[2] not in possible_apis:
        sys.exit("WRONG command-line argument: Read help by passing '-h' argument")
    recipient = check_email(sys.argv[1])
    api = sys.argv[2]
    return recipient, api


def check_email(email):
    """check if email format is valid and return email"""

    try:
        # check_deliverability=True == pinging email, unnecessary
        emailinfo = validate_email(email, check_deliverability=False)
        email = emailinfo.normalized

    except EmailNotValidError as e:
        sys.exit(str(e))

    return email


def hide_passw():
    """get password from system variable"""

    passw = os.environ["TEST_GMAIL_PASS"]
    if passw is None:
        sys.exit("PASSWORD not found. Check system variable.")
    else:
        return passw


def apis(n):
    """act on chosen api"""

    if n == "news":
        topic = input("Enter topic: ")
        newsapi = NewsApiClient(api_key="5b99928f31dc4ad4adfd66e30986a2ab")
        top_headlines = newsapi.get_everything(q=topic, language="en")

        html_table = """
        <table style="border-collapse: collapse; width: 100%; height: 36px;" border="1">
        <tbody>
        <tr style="height: 18px;">
        <td style="width: 20%; height: 18px;">Image</td>
        <td style="width: 30%; height: 18px;">Title</td>
        <td style="width: 35%; height: 18px;">Description</td>
        <td style="width: 10%; height: 18px;">Published</td>
        <td style="width: 5%; height: 18px;">URL</td>
        </tr>
        """

        for article in top_headlines["articles"]:
            html_table += f"""
            <tr style="height: 18px;">
            <td style="width: 20%; height: 18px;"><img src="{article['urlToImage']}" alt="Image" style="width:160px;height:100px;"></td>
            <td style="width: 30%; height: 18px;">{article['title']}</td>
            <td style="width: 35%; height: 18px;">{article['description']}</td>
            <td style="width: 10%; height: 18px;">{article['publishedAt']}</td>
            <td style="width: 5%; height: 18px;"><a href="{article['url']}">Link</a></td>
            </tr>
            """

        html_table += "</tbody></table>"
        return html_table
    else:
        word = input("Enter word: ")
        response = requests.get(
            "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        )

        if response.status_code != 200:
            sys.exit("Error: Unable to get the definition.")

        json_data = response.json()
        print(json_data)
        html_content = "<div>"
        for entry in json_data:
            html_content += f"<h2>{entry.get('word', 'Unknown')} - {entry.get('phonetic', 'N/A')}</h2>"
            for phonetic in entry.get("phonetics", []):
                html_content += f"<p><b>Phonetic:</b> {phonetic.get('text', 'N/A')} "
                if "audio" in phonetic:
                    html_content += f"<a href='https:{phonetic['audio']}'>Listen</a>"
                html_content += "</p>"
            html_content += f"<p><b>Origin:</b> {entry.get('origin', 'No origin information available')}</p>"
            for meaning in entry.get("meanings", []):
                html_content += f"<p><b>Part of Speech:</b> {meaning.get('partOfSpeech', 'N/A')}</p>"
                for definition in meaning.get("definitions", []):
                    html_content += (
                        f"<p><b>Definition:</b> {definition.get('definition', 'N/A')}"
                    )
                    if "example" in definition:
                        html_content += (
                            f"<br><b>Example:</b> {definition.get('example', 'N/A')}"
                        )
                    html_content += "</p>"
        html_content += "</div>"
        return html_content


def send_email(r_email, subject):
    """sending the email with html format"""

    passw = hide_passw()
    s_email = "barturas.testing@gmail.com"

    msg = mmp("alternative")
    msg["From"] = s_email
    msg["To"] = r_email
    msg["Subject"] = subject

    html = apis(subject)

    message = mmt(html, "html")
    msg.attach(message)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(s_email, passw)
        server.sendmail(s_email, r_email, msg.as_string())

    except smtplib.SMTPException as e:
        print("SMTP error occurred: " + str(e))
    except Exception as e:
        print("An error occurred: " + str(e))
    finally:
        server.quit()


if __name__ == "__main__":
    main()

# 1. Command + *         = Run Script (custom)
# 2. Command + Shif + P  = Editor commands
# 3. Control + `         = Terminal (VS Code)
# 4. Command + \         = Split editor
# 5. Command + Shif + Click = find element
# 6. Command + F         = Find keyword in code
# ...