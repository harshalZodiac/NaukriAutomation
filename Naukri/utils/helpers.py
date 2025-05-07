def save_external_link(url, file_path="external_links.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            existing_links = f.read().splitlines()
    except FileNotFoundError:
        existing_links = []

    if url not in existing_links:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(url + "\n")


def save_internal_with_question_job_links(url, file_path="internal_with_question_job_links.txt"):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(url + "\n")