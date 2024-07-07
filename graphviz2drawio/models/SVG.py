from xml.etree.ElementTree import Element

NS_SVG = "{http://www.w3.org/2000/svg}"


def svg_tag(tag):
    return f"{NS_SVG}{tag}"


def get_first(g: Element, tag: str) -> Element | None:
    return g.find(f"./{NS_SVG}{tag}")


def count_tags(g: Element, tag: str) -> int:
    return len(g.findall(f"./{NS_SVG}{tag}"))


def get_title(g: Element) -> str | None:
    if (title_el := get_first(g, "title")) is not None:
        return title_el.text  # pytype: disable=attribute-error
    return None


def get_text(g: Element) -> str | None:
    if (text_el := get_first(g, "text")) is not None:
        return text_el.text
    return None


def is_tag(g, tag):
    return g.tag == svg_tag(tag)
