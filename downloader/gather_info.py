import os
import time
import numpy as np
# from downloader.Composing import parse_pdf
from downloader.markdown_model import typing
from configs import root_path


def load_detail(path_dir):
    d = np.load(os.path.join(path_dir, 'details.npy'), allow_pickle=True).item()
    title = d['title']
    abs = d['abs']
    url = d['url']
    return title, abs, url


def parse_pdf(spd, path_pdf, path_extract):
    pil_images = spd.convert_pdf2img(path_pdf)
    for page_num, img in enumerate(pil_images):
        if page_num > 20:  # 只要前20页
            break
        spd.parse_page(img, page_num, save_dir=path_extract)


def create_markdown(spd, path_pdf, all_md='', root_dir=None):
    path_pdf = path_pdf.replace('\\', '/')
    d = path_pdf.split('/')[-2]

    if root_dir is None:
        root_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))  # today

    if not os.path.isdir(os.path.join(root_dir, d)):
        return
    title, abs, url = load_detail(os.path.join(root_dir, d))
    title_cn = ''
    abs_cn = ''
    if os.path.exists(os.path.join(root_dir, d, "abs.md")):
        md = typing(title, abs, url, title_cn, abs_cn, os.path.join(root_dir, d, 'img'), is_all_typing=True)
        all_md = all_md + md
        return all_md

    parse_pdf(spd, path_pdf, path_extract=os.path.join(root_dir, d, 'img'))
    md = typing(title, abs, url, title_cn, abs_cn, os.path.join(root_dir, d, 'img'))
    np.savetxt(os.path.join(root_dir, d, "abs.md"), [md], "%s", encoding='utf-8')
    md = typing(title, abs, url, title_cn, abs_cn, os.path.join(root_dir, d, 'img'), is_all_typing=True)
    all_md = all_md + md
    return all_md


if __name__ == '__main__':
    from paperparse import std_parse_doc as spd
    create_markdown(spd, r'D:\MyWork\ParsePaperServer\pdf\2103.03230.pdf', root_dir='../outputs')
