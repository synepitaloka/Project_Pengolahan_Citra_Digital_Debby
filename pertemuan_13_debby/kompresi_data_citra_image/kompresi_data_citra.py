import heapq
from collections import defaultdict
from PIL import Image

class HuffmanNode:
    def __init__(self, freq, pixel=None):
        self.freq = freq
        self.pixel = pixel
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(image):
    frequencies = defaultdict(int)
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            frequencies[pixel] += 1

    return frequencies

def build_huffman_tree(frequencies):
    heap = []
    for pixel, freq in frequencies.items():
        node = HuffmanNode(freq, pixel)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = HuffmanNode(left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node.pixel:
        huffman_codes[node.pixel] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

def huffman_compress(image_path):
    image = Image.open(image_path)
    width, height = image.size

    frequencies = calculate_frequencies(image)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    compressed_bits = ""

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            compressed_bits += huffman_codes[pixel]

    return compressed_bits, huffman_codes, width, height

def huffman_decompress(compressed_bits, huffman_codes, width, height):
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    image = Image.new("RGB", (width, height))
    current_bit = ""
    pixel_count = 0
    x = 0
    y = 0

    for bit in compressed_bits:
        current_bit += bit
        if current_bit in reverse_codes:
            pixel = reverse_codes[current_bit]
            image.putpixel((x, y), pixel)
            current_bit = ""
            pixel_count += 1
            x += 1
            if x >= width:
                x = 0
                y += 1
            if pixel_count >= width * height:
                break

    return image

# Contoh penggunaan
image_path = "panda.jpeg"
compressed_bits, huffman_codes, width, height = huffman_compress(image_path)
print("Kode Huffman:", compressed_bits)
print("Tabel Kode Huffman:", huffman_codes)

decompressed_image = huffman_decompress(compressed_bits, huffman_codes, width, height)
decompressed_image.show()
