import random
from bitarray import bitarray
from lorem_text import lorem


def random_ascii_words(count: int) -> bytes:
    return bytes(lorem.words(count), 'ascii')


def random_ascii_sentences(count: int) -> bytes:
    return bytes(lorem.sentence(count), 'ascii')


# Paragraph consist of 2 to 4 sentences
def random_ascii_paragraph(count: int) -> bytes:
    return bytes(lorem.paragraph(count), 'ascii')


def random_bytes(count: int) -> bytes:
    return random.randbytes(count)


def random_bits(count: int) -> bitarray:
    bits: bitarray = bitarray()

    for i in range(0, count):
        bits.append(random.randint(0, 1))

    return bits
