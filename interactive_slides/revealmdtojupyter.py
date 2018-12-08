import json
from collections import namedtuple
from itertools import groupby
from operator import itemgetter

Slide = namedtuple('Slide', ['source', 'cell_type', 'slide_type'])


def convert_file(file_path):
    with open(file_path) as session_1:
        file_content = session_1.read()

    parsed_file = parse_reveal_md_file(file_content)

    cells = [
        generate_cell(slide.source, slide.cell_type, slide.slide_type)
        for slide in parsed_file
    ]

    jupyter_output = {
        'cells': cells,
        **jupyter_metadata()
    }

    file_name = file_path.split('/')[-1].split('.')[0]

    with open(f'{file_name}.ipynb', 'w') as jupyter_file:
        json.dump(jupyter_output, jupyter_file, indent=2)


def parse_reveal_md_file(file_content):
    raw_slides = file_content.split('\n---\n')

    slides = []

    for slide in raw_slides:
        parsed_slides = parse_reveal_md_slide(slide)
        slides.extend(parsed_slides)

    return slides


def parse_reveal_md_slide(slide):
    raw_sub_slides = slide.split('\n----\n')

    sub_slides = []
    title_slide = Slide(raw_sub_slides[0].strip('\n'), 'markdown', 'slide')
    sub_slides.append(title_slide)

    for raw_sub_slide in raw_sub_slides[1:]:
        if '```' not in raw_sub_slide:
            sub_slide = Slide(raw_sub_slide.strip('\n'), 'markdown', 'subslide')
            sub_slides.append(sub_slide)

        else:
            cells = parse_code(raw_sub_slide)
            sub_slides.extend(cells)

    return sub_slides


def parse_code(sub_slide):
    block_lines = categorise_lines(sub_slide)

    groups = groupby(block_lines, key=itemgetter('block_type'))

    first_key, first_group = next(groups)
    first_block = [
        Slide(combine_group(first_group, first_key), first_key, 'subslide')
    ]

    slide_blocks = [
        Slide(combine_group(group, key), key, None)
        for key, group in groups
    ]

    return first_block + slide_blocks


def categorise_lines(sub_slide):
    lines = sub_slide.split('\n')

    block_lines = []
    block_type = 'markdown'

    for line in lines:
        if '``` python' in line or '```python' in line:
            block_type = 'code'
            continue
        elif '```' in line and block_type == 'code':
            block_type = 'markdown'
            continue
        elif line[:5] == 'Note:':
            continue

        line_data = {'source': f'{line}\n', 'block_type': block_type}

        block_lines.append(line_data)

    return block_lines


def combine_group(group, block_type):
    source_lines = [
        item['source']
        for item in group
    ]

    source = ''.join(source_lines)

    if block_type == 'code':
        source = source.strip('\n')

    return source


def generate_cell(source, cell_type, slide_type):
    if cell_type == 'code':
        code_cell = {
            "execution_count": None,
            "outputs": [],
        }
    else:
        code_cell = {}

    if slide_type is not None:
        metadata = {
            "slideshow": {
                "slide_type": slide_type
            }
        }
    else:
        metadata = {}

    return {
        "cell_type": cell_type,
        "metadata": {**metadata},
        "source": [source],
        **code_cell
    }


def jupyter_metadata():
    return {
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.6.7"
            },
            "livereveal": {
                "scroll": True
            },
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }


convert_file('../session_1.md')
convert_file('../session_2.md')
convert_file('../session_3.md')
convert_file('../session_4.md')
convert_file('../session_5.md')
convert_file('../session_6.md')
