import csv
import re
import os
from datetime import datetime

def escape_markdown(text: str) -> str:
    """Escape characters that can break Markdown tables."""
    if text is None:
        return ""
    special_chars = r"\`*_{}[]()#+-.!|"
    return re.sub(r'([{}])'.format(re.escape(special_chars)), r'\\\1', text)

def csv_to_markdown(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"❌ File not found: {input_file}")
        return

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)  # first line (header)

        # Markdown table header
        markdown = "| Name | Author | Thumbnail |\n"
        markdown += "|------|--------|-----------|\n"

        for row in reader:
            world_id = escape_markdown(row[0])
            name = escape_markdown(row[1])
            author_id = row[2]
            author_name = escape_markdown(row[3])
            thumbnail_url = row[4]

            # Name links to world
            name_link = f"[{name}](https://vrchat.com/home/world/{world_id})"
            # Author links to profile
            author_link = f"[{author_name}](https://vrchat.com/home/user/{author_id})"
            # Thumbnail as image
            thumbnail_md = f"![]({thumbnail_url})"

            markdown += f"| {name_link} | {author_link} | {thumbnail_md} |\n"

        # Add last modified message at the end
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        markdown += f"\n*Last modified: {now_str}*\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Markdown saved to {output_file}")


# ------------------------
# Main program
# ------------------------
input_file = input("Enter the CSV filename to import: ").strip()
if not input_file.lower().endswith(".csv"):
    print("⚠️ The file should be a CSV.")
else:
    output_file = os.path.splitext(input_file)[0] + ".md"
    csv_to_markdown(input_file, output_file)
