import os
from textractor import Textractor
from textractor.data.constants import TextractFeatures

extractor = Textractor(profile_name="umd", region_name="us-east-1")

folder_path = "pdfs"

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(".pdf"):
            print(file_name)
            document = extractor.start_document_analysis(
                file_source=f"s3://uplink-issues-pdfs/{file_name}",
                features=[TextractFeatures.LAYOUT],
                save_image=False
            )
            text_file = open(f"text/{file_name.replace(".pdf","")}.txt", "w")
            text_file.write(document.get_text())
            text_file.close()
            markdown_file = open("markdown/" + file_name.replace(".pdf","") + ".md", "w")
            markdown_file.write(document.to_markdown())
            markdown_file.close()
