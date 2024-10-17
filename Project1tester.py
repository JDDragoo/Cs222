import json
import ssl
import sys
from urllib.request import urlopen, URLError

def fetch_wikipedia_revisions(article_title):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + article_title.replace(" ", "%20") + "&rvprop=timestamp|user&rvlimit=30&redirects"
    context = ssl._create_unverified_context()
    try:
        response = urlopen(url, context=context)
        data = json.loads(response.read())
        pages = data.get('query', {}).get('pages', {})
        for page_id, page_data in pages.items():
            if page_id == "-1":
                print(f"No Wikipedia page found for the name '{article_title}'.")
                sys.exit(2)
            if 'redirects' in data['query']:
                redirected_to = data['query']['redirects'][0]['to']
                print(f"Redirected to article: {redirected_to}")
            if 'revisions' in page_data:
                revisions = page_data['revisions']
                for revision in revisions:
                    print(f"{revision['timestamp']} {revision['user']}")
                sys.exit(0)
            else:
                print(f"No revisions found for the article '{article_title}'.")
                sys.exit(0)
    except URLError as e:
        print(f"Network error occurred: {e}")
        sys.exit(3)
def main():
    article_title = input("Please enter the Wikipedia article title: ")
    if not article_title.strip():
        print("No article title provided. Exiting.")
        sys.exit(1)
    fetch_wikipedia_revisions(article_title)
if __name__ == "__main__":
    main()
