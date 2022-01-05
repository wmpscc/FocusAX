import requests
from tqdm import tqdm
from configs import proxy


def download(url: str, file_name: str):
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    head = requests.head(url, headers=headers)
    file_size = head.headers.get('Content-Length')  # 文件大小，以 B 为单位
    if file_size is not None:
        file_size = int(file_size)
    response = requests.get(url, headers=headers, stream=True, proxies=proxy, verify=False)
    chunk_size = 1024 * 1024
    bar = tqdm(total=file_size)
    with open(file_name, mode='wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
    bar.close()


if "__main__" == __name__:
    url = 'https://arxiv.org/pdf/2107.01063.pdf'
    file_name = '2107.01063.pdf'
    download(url, file_name)
