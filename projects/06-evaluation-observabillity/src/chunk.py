from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: int
    text: str
    source: str
    section: str