import requests
import time
from urllib.parse import urlparse


# --------------------------------------------------
# Check whether the URL has a valid format
# --------------------------------------------------
def validate_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)

    if not parsed_url.netloc:
        return None

    return url


# --------------------------------------------------
# Get a readable status from HTTP status code
# --------------------------------------------------
def get_status_message(status_code):
    if 200 <= status_code < 300:
        return "ONLINE"
    elif 300 <= status_code < 400:
        return "REDIRECT"
    elif 400 <= status_code < 500:
        return "CLIENT ERROR"
    elif 500 <= status_code < 600:
        return "SERVER ERROR"
    else:
        return "UNKNOWN"


# --------------------------------------------------
# Check a single URL
# --------------------------------------------------
def check_url(url):
    url = validate_url(url)

    if not url:
        print("\nInvalid URL!")
        return None

    print("\nChecking URL...")
    print("-" * 50)

    try:
        start_time = time.time()

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        end_time = time.time()

        response_time = end_time - start_time

        status = get_status_message(response.status_code)

        https_status = "YES" if url.startswith("https://") else "NO"

        print(f"URL            : {url}")
        print(f"Status Code    : {response.status_code}")
        print(f"Status         : {status}")
        print(f"Response Time  : {response_time:.2f} seconds")
        print(f"HTTPS          : {https_status}")
        print(f"Redirects      : {len(response.history)}")

        return {
            "url": url,
            "status_code": response.status_code,
            "status": status,
            "response_time": response_time
        }

    except requests.exceptions.Timeout:
        print(f"URL            : {url}")
        print("Status         : TIMEOUT")
        print("Error          : The server took too long to respond.")

    except requests.exceptions.ConnectionError:
        print(f"URL            : {url}")
        print("Status         : OFFLINE")
        print("Error          : Could not connect to the website.")

    except requests.exceptions.RequestException as error:
        print(f"URL            : {url}")
        print("Status         : ERROR")
        print(f"Error          : {error}")

    return None


# --------------------------------------------------
# Check multiple URLs
# --------------------------------------------------
def check_multiple_urls():
    urls = input(
        "\nEnter URLs separated by commas:\n"
    ).split(",")

    results = []

    for url in urls:
        url = url.strip()

        if url:
            result = check_url(url)

            if result:
                results.append(result)

    if results:
        print("\n" + "=" * 60)
        print("                    SUMMARY")
        print("=" * 60)

        for result in results:
            print(
                f"{result['url']:<35} "
                f"{result['status_code']} - "
                f"{result['status']}"
            )


# --------------------------------------------------
# Main menu
# --------------------------------------------------
def main():
    while True:
        print("\n" + "=" * 50)
        print("              URL STATUS CHECKER")
        print("=" * 50)

        print("1. Check a URL")
        print("2. Check multiple URLs")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            url = input("\nEnter URL: ").strip()

            if url:
                check_url(url)
            else:
                print("\nURL cannot be empty!")

        elif choice == "2":
            check_multiple_urls()

        elif choice == "3":
            print("\nThank you for using URL Status Checker!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


# --------------------------------------------------
# Program starts here
# --------------------------------------------------
if __name__ == "__main__":
    main()