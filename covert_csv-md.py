import csv

def csv_to_markdown(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # primeira linha (cabeçalho)

        # tabela markdown
        markdown = "| ID | Name | Author Name | Author ID | Thumbnail |\n"
        markdown += "|----|------|-------------|-----------|-----------|\n"

        for row in reader:
            world_id = row[0]
            name = row[1]
            author_name = row[2]
            author_id = row[3]
            thumbnail_url = row[4]

            # links
            world_link = f"[{world_id}](https://vrchat.com/home/world/{world_id})"
            author_link = f"[{author_id}](https://vrchat.com/home/user/{author_id})"

            # thumbnail como imagem
            thumbnail_md = f"![]({thumbnail_url})"

            markdown += f"| {world_link} | {name} | {author_name} | {author_link} | {thumbnail_md} |\n"

    # salvar em arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Markdown salvo em {output_file}")


# exemplo de uso
csv_to_markdown("mundos.csv", "mundos.md")
