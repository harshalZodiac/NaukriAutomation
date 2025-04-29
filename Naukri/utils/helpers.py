def save_external_link(url, file_path="external_links.txt"):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(url + "\n")