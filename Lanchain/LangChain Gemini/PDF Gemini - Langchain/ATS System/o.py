from pdf2image import convert_from_path

from pathlib import Path

pdf_dir = Path(r'C:\Users\Rahul\Desktop\Data Science\krish\LangChain\ATS System\Jitmohan.pdf')
save_dir = Path('Jitmohan.pdf')

for pdf_file in pdf_dir:
    pages = convert_from_path(pdf_file, 300)
    print("pages",pages)
    for num, page in enumerate(pages, start=1):
        page.save(save_dir / f'{pdf_file.stem}-page{num}.jpg', 'JPEG')
        
print("pdf_dirpdf_dir0", pdf_dir)