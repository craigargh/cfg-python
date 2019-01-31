import argparse
import os

from markdown2 import markdown
import pdfkit

OUTPUT_DIR = 'out'


def parse_md(file_name):
    with open(file_name) as md_file:
        content = md_file.read()

    return markdown(content, extras=['code-friendly', 'fenced-code-blocks', 'tables'])


def save_html(html):
    stylesheets = (
        '<head>\n'
        '<link rel="stylesheet" href="code.css">\n'
        '<link rel="stylesheet" href="style.css">\n'
        '</head>\n'
    )

    output = '\n'.join([stylesheets, '<body>',  html, '</body>'])

    with open(f'{OUTPUT_DIR}/session_1.html', 'w+') as html_file:
        html_file.write(output)


def save_pdf(html):
    output = '\n'.join(['<body>',  html, '</body>'])

    margin = '1.4in'
    options = {
        'page-size': 'A4',
        'margin-top': margin,
        'margin-right': margin,
        'margin-bottom': margin,
        'margin-left': margin,
        'encoding': "UTF-8",
    }


    css = [f'{OUTPUT_DIR}/code.css', f'{OUTPUT_DIR}/style.css']
    pdfkit.from_string(html, f'{OUTPUT_DIR}/session_1.pdf', css=css, options=options)


def run(format):
    all_files = sorted(
        f 
        for f in os.listdir('.') 
        if os.path.isfile(f)
        if 'session' in f
    )

    all_files.insert(0, 'introduction.md')

    parsed = '\n'.join(
        parse_md(file_name)
        for file_name in all_files
    )

    if format == 'pdf':
        save_pdf(parsed)
    elif format =='html':
        save_html(parsed)
    elif format == 'all':
        save_pdf(parsed)
        save_html(parsed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=['pdf', 'html', 'all'], default='html')

    args = parser.parse_args()
    run(args.format)
