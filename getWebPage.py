import requests

def get_web_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        with open("grabbedPage.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Web page saved to grabbedPage.html")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Please enter the URL of the web page you want to grab: ")
    get_web_page(url)