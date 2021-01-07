import threading
import queue
import urllib.request
from lxml import html


urls = [
    "https://en.wikipedia.org/wiki/Harry_Potter_(character)",
    "https://en.wikipedia.org/wiki/Hermione_Granger",
    "https://en.wikipedia.org/wiki/Ron_Weasley"
]

output = {}


def fetch(url_addr, thread_queue):
    u = urllib.request.urlopen(url_addr)
    thread_queue.put((url_addr, u.read()))


def extract_words(article):
    def get_words(url_content):
        for content_word in url_content.split(" "):
            content_word = content_word.strip("\"")
            content_word = content_word.strip("\n")
            if content_word != "-" and len(content_word) > 0:
                yield content_word.lower()
    doc = html.document_fromstring(article)
    print(doc, end="\n\n")
    for p in doc.cssselect("div.mw-parser-output p"):
        content = p.text_content()
        for word in get_words(content):
            yield word


def process(thread_queue):
    global output
    while True:
        try:
            article_url, article = thread_queue.get(timeout=5)
        except queue.Empty:
            break
        extracted_words = extract_words(article)
        output[article_url] = extracted_words
        thread_queue.task_done()


q = queue.Queue()
producer_threads = []
consumer_threads = []

for url in urls:
    t = threading.Thread(target=fetch, args=[url, q])
    t.start()
    producer_threads.append(t)

for i in range(3):
    t = threading.Thread(target=process, args=[q])
    t.start()
    consumer_threads.append(t)

q.join()

threads = producer_threads + consumer_threads
for t in threads:
    t.join()

print(output)
for url, words in output.items():
    items = list(words)
    print(url)
    print("size: ", len(items), ", some words: ", items[:15])
    print()
