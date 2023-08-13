import argparse

def parse_arguments(args_list=None):
    parser = argparse.ArgumentParser(description="Word Search Tool")
    parser.add_argument("query", nargs="?", default="", help="Word query rules")
    return parser.parse_args(args_list)

args = parse_arguments()

with open("wordlist.txt", "r") as file:
    word_list = [word.strip() for word in file]

def is_isogram(word):
    """Return True if the word is an isogram, False otherwise."""
    return len(set(word)) == len(word)

def is_palindrome(word):
    return word == word[::-1]

def is_semordnilap(word, word_set):
    return not is_palindrome(word) and word[::-1] in word_set

def has_maximum_length(word, max_length):
    return len(word) <= max_length

def has_minimum_length(word, min_length):
    return len(word) >= min_length

def starts_with(word, prefix):
    return word.startswith(prefix)

def ends_with(word, suffix):
    """Return True if the word ends with the specified suffix, False otherwise."""
    return word.endswith(suffix)

def contains_only(word, character_whitelist):
    """Return True if the word contains only characters from the specified whitelist, False otherwise."""
    return all(char in character_whitelist for char in word)


def apply_search_rules(query, word_list):
    # Split the query string into individual rules
    rules = query.split()

    filtered_words = word_list

    for rule in rules:
        if rule.startswith("class="):
            class_value = rule.split("=")[1]
            if class_value == "palindrome":
                filtered_words = [word for word in filtered_words if is_palindrome(word)]
            elif class_value == "isogram":
                filtered_words = [word for word in filtered_words if is_isogram(word)]
            elif class_value == "semordnilap":
                filtered_words = [word for word in filtered_words if is_semordnilap(word, set(filtered_words))]
        elif rule.startswith("maxlength="):
            max_length = int(rule.split("=")[1])
            filtered_words = [word for word in filtered_words if has_maximum_length(word, max_length)]
        elif rule.startswith("minlength="):
            min_length = int(rule.split("=")[1])
            filtered_words = [word for word in filtered_words if has_minimum_length(word, min_length)]
        elif rule.startswith("startswith="):
            prefix = rule.split("=")[1]
            filtered_words = [word for word in filtered_words if starts_with(word, prefix)]
        elif rule.startswith("endswith="):
            suffix = rule.split("=")[1]
            filtered_words = [word for word in filtered_words if ends_with(word, suffix)]
        elif rule.startswith("containsonly="):
            characters = rule.split("=")[1]
            filtered_words = [word for word in filtered_words if contains_only(word, characters)]

    return filtered_words


matching_words = apply_search_rules(args.query, word_list)

