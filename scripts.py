import os
from collections import Counter
import socket

def count_words(file_path):
    with open(file_path, 'r') as f:
        words = f.read().split()
    return words

def top_three_frequent_words(words):
    counter = Counter(words)
    return counter.most_common(3)

def handle_contractions(text):
    contractions = {"I'm": "I am", "can't": "cannot", "don't": "do not", "isn't": "is not", "won't": "will not"}
    for contraction, replacement in contractions.items():
        text = text.replace(contraction, replacement)
    return text.split()

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Paths to the files inside the container
if_path = '/home/data/IF.txt'
always_path = '/home/data/AlwaysRememberUsThisWay.txt'
output_path = '/home/data/output/result.txt'

# Read and process files
if_words = count_words(if_path)
always_text = open(always_path, 'r').read()
always_words = handle_contractions(always_text)

# Count total words
total_if_words = len(if_words)
total_always_words = len(always_words)
grand_total_words = total_if_words + total_always_words

# Get top 3 words
top_if = top_three_frequent_words(if_words)
top_always = top_three_frequent_words(always_words)

# Get container's IP address
container_ip = get_ip()

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write results to result.txt
with open(output_path, 'w') as f:
    f.write(f"Total words in IF.txt: {total_if_words}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_always_words}\n")
    f.write(f"Grand total of words: {grand_total_words}\n")
    f.write(f"Top 3 words in IF.txt: {top_if}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_always}\n")
    f.write(f"Container's IP address: {container_ip}\n")

# Print the contents of result.txt to the console
with open(output_path, 'r') as f:
    print(f.read())
