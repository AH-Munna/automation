def remove_repetitions(input_string: str):
    # Split the string using ','
    items = input_string.split(',')
    
    # Trim spaces, convert to lowercase, and filter out empty items
    processed_items = [item.strip().lower() for item in items]
    non_empty_items = [item for item in processed_items if item]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_items = []
    for item in non_empty_items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    
    # Print the unique items
    print("\033[32mUnique items:\033[0m")
    for item in unique_items:
        print(item + ',')