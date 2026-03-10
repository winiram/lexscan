import tiktoken

ENCODING_NAME = "cl100k_base"
MAX_TOKENS_PER_CHUNK = 140_000


def _get_encoding():
    return tiktoken.get_encoding(ENCODING_NAME)


def count_tokens(text: str) -> int:
    enc = _get_encoding()
    return len(enc.encode(text))


def split_into_chunks(text: str) -> list[str]:
    """Split text into chunks that each fit within MAX_TOKENS_PER_CHUNK.

    Most legal documents fit in a single chunk. This is a fallback for very
    long documents.
    """
    enc = _get_encoding()
    tokens = enc.encode(text)

    if len(tokens) <= MAX_TOKENS_PER_CHUNK:
        return [text]

    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + MAX_TOKENS_PER_CHUNK, len(tokens))
        chunk_tokens = tokens[start:end]
        chunks.append(enc.decode(chunk_tokens))
        start = end

    return chunks
