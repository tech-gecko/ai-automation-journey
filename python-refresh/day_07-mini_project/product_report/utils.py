def log(message: str):
    with open("product_report.log", "a") as log_file:
        log_file.write(message + "\n")
