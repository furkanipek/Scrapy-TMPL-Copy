# Scrapy TMPL Copy

> First create your virtual environment, install scrapy.

> Then install my Scrapy TMPL Copy tool.

# What is it?

> It is a small tool for copying template files for "scrapy genspider".

> After you put your own template files in the tmpl folder, you can send the files to scrapy with "tmplsetup.py".

## Example Usage

```bash

# Create Folder
mkdir TestProject

# Enter Folder
cd TestProject

# Create virtual env
python3 -m venv menv

# Install Scrapy
pip install scrapy

# ADD My TMPL Copy
git clone https://github.com/furkanipek/Scrapy-TMPL-Copy.git

# Create your own template in the tmpl folder.

tmplsetup.py

# After the copying process is finished, you can create your spider.

scrapy genspider -t YourTempName <name> <domain>

```
