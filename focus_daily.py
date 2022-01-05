from downloader.download_arxiv_daily import start_parse

if __name__ == '__main__':
    key_words = ['GAN']
    subject_words = ['ML', 'CV', 'AI']
    start_parse(key_words, subject_words, needPDF=True, needZip=False)
