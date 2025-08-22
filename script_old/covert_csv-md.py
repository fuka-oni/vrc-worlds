import csv
import re

def escape_markdown(text: str) -> str:
    """Escape characters that can break Markdown tables."""
    if text is None:
        return ""
    # List of characters to escape in Markdown
    special_chars = r"\`*_{}[]()#+-.!|"
    # Escape each character by prefixing with \
    return re.sub(r'([{}])'.format(re.escape(special_chars)), r'\\\1', text)

def csv_to_markdown(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # first line (header)

        # Markdown table header
        markdown = "| ID | Name | Author | Thumbnail |\n"
        markdown += "|----|------|--------|-----------|\n"

        for row in reader:
            world_id = escape_markdown(row[0])
            name = escape_markdown(row[1])
            author_id = row[2]       # usr_xxxxx
            author_name = escape_markdown(row[3])
            thumbnail_url = row[4]

            # links
            world_link = f"[{world_id}](https://vrchat.com/home/world/{world_id})"
            author_link = f"[{author_name}](https://vrchat.com/home/user/{author_id})"

            # thumbnail as image
            thumbnail_md = f"![]({thumbnail_url})"

            markdown += f"| {world_link} | {name} | {author_link} | {thumbnail_md} |\n"

    # save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Markdown saved to {output_file}")


# Example usage
csv_to_markdown("mundos.csv", "mundos.md")
