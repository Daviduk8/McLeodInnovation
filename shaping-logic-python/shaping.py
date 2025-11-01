non_connecting = {'ا', 'د', 'ذ', 'ر', 'ز', 'و'}

def is_joining(prev, curr):
    """Returns True if curr can join with prev."""
    return prev not in non_connecting and curr not in non_connecting

def shape_arabic(text):
    shaped = []
    for i, char in enumerate(text):
        if char == ' ':
            shaped.append(' ')  # preserve spaces
            continue

        prev = text[i - 1] if i > 0 else None
        next_ = text[i + 1] if i < len(text) - 1 else None

        # Determine position
        if not prev or prev in non_connecting:
            if next_ and next_ not in non_connecting:
                form = 'initial'
            else:
                form = 'isolated'
        else:
            if next_ and next_ not in non_connecting:
                form = 'medial'
            else:
                form = 'final'

        shaped.append(f'{char}({form})')  # placeholder for now

    return ' '.join(shaped)

# Example usage
if __name__ == "__main__":
    sample = "سلام"
    print(shape_arabic(sample))
