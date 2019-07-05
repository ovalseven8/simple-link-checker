import sys
from threading import Thread

import requests
from requests import RequestException


def check_links(links, broken_list, http_method):
    while True:
        try:
            url = links.pop()

            try:
                r = http_method(url)
                if r.status_code == 404:
                    broken_list.append(url)
            except RequestException:
                broken_list.append(url)
        except (KeyError, IndexError):
            break


if __name__ == '__main__':

    number_of_links = 0
    threads = []
    broken_links_head = []
    broken_links = []
    links = set()

    for url in sys.stdin:
        links.add(url.rstrip('\n'))
        number_of_links += 1

    for i in range(0, 40):
        thread = Thread(target=check_links, args=(links, broken_links_head, requests.head))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if len(broken_links_head) >= 1:
        print("HEAD requests have failed for the following URLs:")
        print("\n".join(broken_links_head) + "\n")
        print("Because of misconfigured servers the URLs are checked using GET requests now ...\n")

        for i in range(0, 20):
            thread = Thread(target=check_links, args=(broken_links_head, broken_links, requests.get))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    if len(broken_links) >= 1:
        print(str(len(broken_links)) + "/" + str(number_of_links) + " are broken:")
        print("\n".join(broken_links))
    else:
        print("No broken links! (" + str(len(broken_links)) + "/" + str(number_of_links) + ")")

    if broken_links:
        sys.exit(1)
