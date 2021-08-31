import requests


def fetch_page(url):
  try:
    res = requests.get(url)
    print(res.content[:50])
  except BaseException as e:
    print(e)


if __name__ == "__main__":
  url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
  fetch_page(url=url)
