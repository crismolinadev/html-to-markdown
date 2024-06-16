from bs4 import BeautifulSoup
import sys

def html_to_markdown(html_file):
    # Read HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all chapters
    chapters = soup.find_all('div', class_='chapter')

    # Initialize Markdown content
    markdown_content = ""

    # Iterate over each chapter
    for chapter_idx, chapter in enumerate(chapters, start=1):
        # Extract Chapter title
        chapter_title = chapter.find('div', class_='n').text.strip()
        markdown_content += f"# {chapter_idx}. {chapter_title}\n\n"

        # Extract materials within the same chapter
        materials = chapter.find_next_sibling('div', class_='materials').find_all('a', class_='material')

        # Convert each material title to Markdown format
        for material_idx, material in enumerate(materials, start=1):
            material_title = material.find('div', class_='n').text.strip()
            markdown_content += f"## {chapter_idx}.{material_idx} {material_title}\n\n"

        # Add horizontal rule after the last material in the chapter
        markdown_content += "---\n"

    return markdown_content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python html_to_markdown_converter.py <input_html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    markdown_output = html_to_markdown(html_file)
    
    # Write the Markdown output to a file named result.md
    with open('result.md', 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print("Markdown content has been written to result.md")
