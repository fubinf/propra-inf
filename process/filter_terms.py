"""
This script extracts terms from a glossary file and searches for their occurrences in Markdown files.
It supports filtering terms by a string or starting letter and can replace found terms with a reference format.

Example usage:
    python filter_terms.py --path ../docs/ --filter "API"
    python filter_terms.py --path ../docs/ --letter A
    python filter_terms.py --path ../docs/ --filter "API" --dry-run

Note:
    There may still be matches that are not desired because they appear in areas that are not filtered,
    such as custom Markdown sections or other unhandled patterns.
"""

import os
import re
import argparse

def extract_terms(glossary_path, filter_string=None, start_letter=None):
    """
    Extracts terms from the glossary file.

    Args:
        glossary_path (str): Path to the glossary file.
        filter_string (str, optional): String to filter terms. Defaults to None.
        start_letter (str, optional): Letter to filter terms starting with it. Defaults to None.

    Returns:
        list: A list of extracted terms.
    """
    terms = []
    with open(glossary_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Match terms within [TERM::...] blocks
        matches = re.findall(r'\[TERM::(.*?)\]', content)
        for match in matches:
            # Split terms by '|' if multiple terms are listed
            terms.extend(match.split('|'))
    # Apply filter string if provided
    if filter_string:
        terms = [term for term in terms if filter_string.lower() in term.lower()]
    # Apply starting letter filter if provided
    if start_letter:
        terms = [term for term in terms if term.lower().startswith(start_letter.lower())]
    return terms

def is_term_already_referenced(term, content):
    """
    Checks if the term is already enclosed within square brackets.

    Args:
        term (str): The term to check.
        content (str): The content to search in.

    Returns:
        bool: True if the term is already referenced, False otherwise.
    """
    return re.search(rf'\[.*{re.escape(term)}.*\]', content) is not None

def is_term_in_md_header_or_codeblock(term, content):
    """
    Checks if the term is in a Markdown header, code block, or specific metadata lines.

    Args:
        term (str): The term to check.
        content (list): The content as a list of lines.

    Returns:
        bool: True if the term is in an excluded context, False otherwise.
    """
    in_codeblock = False
    for line in content:
        if line.strip().startswith("```"):  # Toggle code block state
            in_codeblock = not in_codeblock
        if in_codeblock:  # Skip lines inside code blocks
            continue
        if line.startswith("#"):  # Skip Markdown headers
            if term in line:
                return True
        # Skip specific metadata lines
        if any(line.strip().startswith(prefix) for prefix in ["title:", "assumes:", "requires:", "explains:", "mentions:"]):
            if term in line:
                return True
        # Skip terms within `*<term>*` patterns
        if re.search(rf'`*{re.escape(term)}*`', line):
            return True
    return False

def search_terms_in_files(terms, directory, exclude_file):
    """
    Searches for terms in Markdown files within a directory.

    Args:
        terms (list): List of terms to search for.
        directory (str): Path to the directory containing Markdown files.
        exclude_file (str): Path to the file to exclude from the search.

    Returns:
        dict: A dictionary mapping terms to their occurrences (file path, line number, line content).
    """
    term_occurrences = {term: [] for term in terms}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file.endswith(os.path.basename(exclude_file)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                    for line_number, line in enumerate(content, start=1):
                        for term in terms:
                            # Check if the term is in the line and not already referenced
                            if term in line and not is_term_already_referenced(term, line):
                                # Check if the term is not in excluded contexts
                                if not is_term_in_md_header_or_codeblock(term, content):
                                    term_occurrences[term].append((file_path, line_number, line.strip()))
    return term_occurrences

def replace_terms_in_files(term_occurrences):
    """
    Replaces terms in files with their reference format.

    Args:
        term_occurrences (dict): A dictionary mapping terms to their occurrences.
    """
    for term, files in term_occurrences.items():
        for file_path, _, _ in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Replace the term with its TERMREF equivalent
            updated_content = content.replace(term, f"[TERMREF::{term}]")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

def main():
    """
    Main function to parse arguments, extract terms, search for occurrences, and optionally replace terms.
    """
    parser = argparse.ArgumentParser(
        description="Filter and search terms in glossary and files.",
        epilog="Examples:\n"
               "  python filter_terms.py --path ./docs/ --filter 'API'\n"
               "  python filter_terms.py --letter A\n",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-p', '--path', type=str, default='../ch/',
        help="Path to search files in (default: ../ch/)."
    )
    parser.add_argument(
        '-f', '--filter', type=str,
        help="Filter string to restrict terms."
    )
    parser.add_argument(
        '-l', '--letter', type=str,
        help="Use only terms starting with this letter."
    )
    parser.add_argument(
        '-d', '--dry-run', action='store_true',
        help="Only display found terms and matches without making changes."
    )
    args = parser.parse_args()

    glossary_path = '../ch/glossary.md'
    terms = extract_terms(glossary_path, args.filter, args.letter)
    print(f"Found terms ({len(terms)}): {', '.join(terms)}")

    term_occurrences = search_terms_in_files(terms, args.path, glossary_path)
    for term, occurrences in term_occurrences.items():
        print(f"\nTerm: {term}")
        if occurrences:
            for file_path, line_number, line in occurrences:
                print(f"  {file_path}:{line_number}: {line}")
        else:
            print("  No matches found.")

    if not args.dry_run:
        replace_terms_in_files(term_occurrences)

if __name__ == "__main__":
    main()
