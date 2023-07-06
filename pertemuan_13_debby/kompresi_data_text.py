def rle_compress(text):
    compressed = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += str(count) + text[i - 1]
            count = 1
    compressed += str(count) + text[-1]
    return compressed

# Contoh penggunaan
original_text = "DEBBY SAUDRAAAAN DENGANNNN VALEEEENN"
compressed_text = rle_compress(original_text)
print("Teks asli:", original_text)
print("Teks terkompresi:", compressed_text)