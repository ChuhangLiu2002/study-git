import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


def fetch_papers(keyword, limit=5):
    """从 arXiv 获取与关键词相关的最新论文。"""
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:{keyword}",
            "start": 0,
            "max_results": limit,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{params}"

    with urllib.request.urlopen(url, timeout=15) as response:
        root = ET.fromstring(response.read())

    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in root.findall("atom:entry", namespace):
        papers.append(
            {
                "title": " ".join(entry.findtext("atom:title", "", namespace).split()),
                "authors": ", ".join(
                    author.findtext("atom:name", "", namespace)
                    for author in entry.findall("atom:author", namespace)
                ),
                "summary": " ".join(
                    entry.findtext("atom:summary", "", namespace).split()
                ),
                "url": entry.findtext("atom:id", "", namespace),
            }
        )
    return papers


def print_papers(papers):
    """将论文信息输出到控制台。"""
    if not papers:
        print("没有找到相关论文。")
        return

    for index, paper in enumerate(papers, start=1):
        print(f"\n[{index}] {paper['title']}")
        print(f"作者：{paper['authors']}")
        print(f"摘要：{paper['summary']}")
        print(f"链接：{paper['url']}")