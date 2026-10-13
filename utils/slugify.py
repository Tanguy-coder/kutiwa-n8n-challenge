import re
import unicodedata

def slugify(text: str) -> str:
    """
    Convert a string to a URL‑friendly slug.

    - Lowercases the string.
    - Normalizes unicode characters to ASCII.
    - Replaces any non‑alphanumeric characters with a hyphen.
    - Collapses multiple hyphens.
    - Strips leading/trailing hyphens.
    """
    # Normalize unicode characters to their closest ASCII representation
    normalized = unicodedata.normalize('NFKD', text)
    ascii_str = normalized.encode('ascii', 'ignore').decode('ascii')
    # Replace non‑alphanumeric characters with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', ascii_str.lower())
    # Remove leading/trailing hyphens
    return slug.strip('-')
