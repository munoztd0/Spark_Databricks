messsage = "the quick brown fox"
N=10

def split_text_into_chunks(text, max_length):
    # Handle the case where a single word is longer than max_length
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        # If the word is longer than max_length, it becomes its own chunk
        if len(word) > max_length:
            # If there's a current chunk in progress, add it before this long word
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = 0
            
            # Add the long word as a separate chunk
            chunks.append(word)
            continue

        # Check if adding this word would exceed max_length
        word_length = len(word)
        space_length = 1 if current_chunk else 0  # Account for space between words
        
        if current_length + space_length + word_length > max_length:
            # Current chunk is full, save it and start a new one
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = word_length
        else:
            # Add word to current chunk
            current_chunk.append(word)
            current_length += space_length + word_length

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
