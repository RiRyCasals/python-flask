import os
import markdown

DIR_DATA = os.path.dirname(__file__) + '/data'

md = markdown.Markdown(extensions=['tables'])

def get_filename(page_name):
    return DIR_DATA + '/' + page_name + '.md'

def read_file(page_name, html=False):
    path = get_filename(page_name)
    if os.path.exists(path):
        with open(path, 'rt', encoding='utf-8') as f:
            s = f.read()
            if html:
                s = md.convert(s)
            return s
    return ""

def write_file(page_name, body):
    path = get_filename(page_name)
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(body)
