import requests
from bs4 import BeautifulSoup


def main():
    ifsc_url_ao = "https://www.ifsc-climbing.org/index.php?option=com_ifsc&task=athlete.display&id=1364"

    response = requests.get(ifsc_url_ao)

    if response.status_code == 200:
        print(f"Received 200 response from provided url: {ifsc_url_ao}")
        html_content = response.text

    personal_info_div = soup.find("div", class_="personal_info")
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.prettify())


if __name__ == "__main__":
    main()
