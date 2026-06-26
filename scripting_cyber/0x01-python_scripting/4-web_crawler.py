#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(start_url, max_depth=2, visited=None, depth=0, base_domain=None):
    if visited is None:
        visited = set()

    if base_domain is None:
        base_domain = urlparse(start_url).netloc

    if depth > max_depth:
        return visited

    try:
        response = requests.get(start_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return visited

    if start_url in visited:
        return visited

    visited.add(start_url)

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")
        if not href:
            continue

        full_url = urljoin(start_url, href)
        parsed = urlparse(full_url)

        if parsed.scheme not in ("http", "https"):
            continue

        if parsed.netloc != base_domain:
            continue

        if full_url not in visited:
            crawl_website(full_url, max_depth, visited, depth + 1, base_domain)

    return visited
