from ddgs import DDGS


def web_search(query: str) -> str:

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        if not results:
            return "No search results found."

        output = []

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")
            url = result.get("href", "")

            output.append(
                f"Title: {title}\n"
                f"Description: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search failed: {str(e)}"