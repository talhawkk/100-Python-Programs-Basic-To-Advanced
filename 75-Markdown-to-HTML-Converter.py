import re

def markdown_to_html(md_text):
    md_text = re.sub(r'^(#{1}) (.*)', r'<h1>\2</h1>', md_text)  # Header 1
    md_text = re.sub(r'^(#{2}) (.*)', r'<h2>\2</h2>', md_text)  # Header 2
    md_text = re.sub(r'^(#{3}) (.*)', r'<h3>\2</h3>', md_text)  # Header 3

    md_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_text)

    md_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', md_text)

    md_text = re.sub(r'^\* (.*)', r'<ul><li>\1</li></ul>', md_text, flags=re.MULTILINE)

    return md_text

def save_to_html(md_file, output_file):
    with open(md_file, 'r') as file:
        md_text = file.read()

    html_text = markdown_to_html(md_text)

    with open(output_file, 'w') as file:
        file.write(html_text)
    print(f"Converted {md_file} to {output_file}.")

md_file = 'sample.md'  # add your one markdown file
output_file = 'output.html'  # add your Output HTML file
save_to_html(md_file, output_file)
