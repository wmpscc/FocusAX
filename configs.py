# =============== 网络代理 ================
# proxy = None
proxy = {"http": "socks5://127.0.0.1:8786", "https": "socks5://127.0.0.1:8786"}
# =============== 保存文件根目录 ================
root_path = "./arxiv"
# =============== DNN模型推理配置信息 ================
threshold = 0.5
enable_mkldnn = True
enforce_cpu = True
thread_num = 4

