#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(start_url, max_depth=2):
    visited = set()
    base_domain = urlparse(start_url).netloc

    def crawl(url, depth):
        if depth > max_depth:
            return

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return

        if url in visited:
            return

        visited.add(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if not href:
                continue

            full_url = urljoin(url, href)
            parsed = urlparse(full_url)

            if parsed.scheme not in ("http", "https"):
                continue

            if parsed.netloc != base_domain:
                continue

            if full_url not in visited:
                crawl(full_url, depth + 1)

    crawl(start_url, 0)
    return visited
