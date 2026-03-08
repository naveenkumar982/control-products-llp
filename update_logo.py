import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace logo source
    content = content.replace('src="assets/images/CP_logo_LLP.png"', 'src="assets/images/CP_logo_wide.png"')

    # Replace hardcoded layout width
    content = content.replace('width=\"384\" height=\"78\"', 'width=\"auto\" height=\"78\"')
    content = content.replace('#logo{width:384px;}', '#logo{width:auto; max-width: 100%;}')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {file}')
