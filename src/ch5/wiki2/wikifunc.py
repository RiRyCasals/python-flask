import os
import re
import hashlib
import subprocess
import markdown

DIR_DATA = os.path.dirname(__file__) + '/data'
DIR_BACKUP = DIR_DATA + '/backup'
DIFF3 = 'diff3'

md = markdown.Markdown(extensions=['tables'])

def get_filename(page_name):
    return DIR_DATA + '/' + page_name + '.md'

def get_backup(page_name, hash):
    if not os.path.exists(DIR_BACKUP):
        os.makedirs(DIR_BACKUP)
    return DIR_BACKUP + '/' + page_name + '.' + hash

def read_file(page_name, html=False):
    text = read_f(get_filename(page_name))
    hash = get_hash(text)
    print('read:', hash)
    if html:
        text = md.convert(text)
    return text, hash

def write_file(page_name, body):
    body = re.sub(r'\r\n|\r\n', "\n", body)
    write_f(get_filename(page_name), body)
    hash = get_hash(body)
    write_f(get_backup(page_name, hash), body)

def get_diff(page_name, text, hash):
    newfile = DIR_DATA + '/__submit__'
    write_f(newfile, text)
    orgfile = DIR_DATA + '/__pre-editt__'
    backupfile = get_backup(page_name, hash)
    write_f(orgfile, read_f(backupfile))
    curfile = DIR_DATA + '/__update__'
    write_f(curfile, read_f(get_filename(page_name)))
    cp = subprocess.run(
        [DIFF3, '-a', '-m', newfile, orgfile, curfile],
        encoding='utf-8',
        stdout=subprocess.PIPE)
    print(cp)
    res = cp.stdout
    res = res.replace(DIR_DATA + '/', '')
    return res

def read_f(path):
    text = ''
    if os.path.exists(path):
        with open(path, 'rt', encoding='utf-8') as f:
            text = f.read()
    return text

def write_f(path, text):
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(text)

def get_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
