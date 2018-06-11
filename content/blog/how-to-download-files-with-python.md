---
{
  "date": "2018-06-11",
  "slug": "how-to-download-files-with-python",
  "subtitle": "Generic subtitle",
  "title": "How to download files with Python",
  "toc": "true"
}
---
<!--more-->

TL;DR: Python program able to download, resume downloads and validate
downloaded files with hashes. You can find it at the end of the article.

In one of my recent projects on natural language processing and patents,
I tried to program a little script which downloads files needed for the
analysis.

The program should be able to do the following things:

1. Download a given file
2. Resume the download if the file is incomplete
3. Validate the file at the end of the download using hashes
4. Wrap everything with beautiful progress bars

Note that, to run the script you have to have at least a python 3.6 environment as I am using [``f-strings``](https://www.python.org/dev/peps/pep-0498/).

# Downloading files

At first, we need to know how to download a file. We will use
[``requests``](http://docs.python-requests.org/en/latest/) to handle
connections to web content.


```python
import requests
```

In the next step, we will download a file and store it on the disk. The file size is 19kb, so you are save to download it. If you have doubts about the file, insert any other link which can be a picture or something else.


```python
url = 'http://www.patentsview.org/data/20171226/cpc_group.tsv.zip'

r = requests.get(url)

with open('cpc_group.tsv.zip', 'wb') as f:
    f.write(r.content)
```

Note that ``requests.get`` will download the file immediately and store it in memory. For larger files, this does not work as they might not fit in memory. Therefore, we use the ``stream`` keyword to receive the file in chunks and store them on disk. The next file is about 3MB big. Use a different URL if you feel more comfortable with that.


```python
url = 'http://www.patentsview.org/data/20171226/government_interest.tsv.zip'

r = requests.get(url, stream=True)

with open('government_interest.tsv.zip', 'wb') as f:
    for chunk in r.iter_content(32 * 1024):
        f.write(chunk)
```

# Resuming downloads

If you download large files, chances are that your download is interrupted. For that, we need a way to resume the download at the last byte position. We can do that by sending an Range-request to the server and specifying the range of bytes, we want to receive.


```python
resume_header = ({'Range': f'bytes=0-2000000'})

r = requests.get(url, stream=True, headers=resume_header)

with open('government_interest_part.tsv.zip', 'wb') as f:
    for chunk in r.iter_content(32 * 1024):
        f.write(chunk)
```

We look at the file size whether we have been able to download the file partially.


```python
from pathlib import Path

path = Path('government_interest_part.tsv.zip')

print(f'Size of file: {path.stat().st_size} Bytes')
```

    Size of file: 2000001 Bytes
    

Now, we resume the download at the position of the last byte. We also have to change the mode from ``open()`` to ``'ab'`` as we are appending new content and do not want to overwrite existing content.


```python
resume_header = ({'Range': f'bytes={path.stat().st_size}-'})

r = requests.get(url, stream=True, headers=resume_header)

with open('government_interest_part.tsv.zip', 'ab') as f:
    for chunk in r.iter_content(32 * 1024):
        f.write(chunk)
```

The crucial aspect of this code is that we correctly define the following range of bytes for the following downloads. It is important to know that the boundaries of the Range header are inclusive so that bytes in positions 0 and 2000000 are downloaded. Therefore, the file size is 2000001 and we can plug in the value to correctly resume the download.

# Validating downloads

At last, we want to make sure that the download of the file worked as expected. To assert whether two files are identical, one of the easiest solutions is to compare hashes. A hash function projects any kind of data onto data with fixed-length. The resulting object is called hash and should be different for two different objects but identical for the same. In this example, we use SHA256 to validate the two files.


```python
import hashlib

with open('government_interest.tsv.zip', 'rb') as f:
    content = f.read()
    
sha = hashlib.sha256()

sha.update(content)

print(sha.hexdigest())
```

    42e53da0f2adc03e035eb2f967998da5cb8e2b1235cd2630efc59e31df866372
    


```python
with open('government_interest_part.tsv.zip', 'rb') as f:
    content = f.read()
    
sha = hashlib.sha256()

sha.update(content)

print(sha.hexdigest())
```

    42e53da0f2adc03e035eb2f967998da5cb8e2b1235cd2630efc59e31df866372
    

Both hashes match and we have correctly resumed the download :).

# Visualizing download progress

There are multiple options to print pretty progress bars in python to the command line interface ([``progressbar2``](https://github.com/WoLpH/python-progressbar) e.g.), but I used ``tqdm`` for unknown reason.

To display the progress of the download, we have to know the total file size which we can easily request without downloading the whole file. Use ``requests.head()`` instead of ``requests.get()``.


```python
url = 'http://www.patentsview.org/data/20171226/government_interest.tsv.zip'

r = requests.head(url)

file_size = int(r.headers.get('content-length', 0))

print(f'Size of file: {file_size}')
```

    3895459
    

Note that content length returns a string and not a number.


```python
from tqdm import tqdm


r = requests.get(url, stream=True)

initial_pos = 0

with open('government_interest.tsv.zip', 'wb') as f:
    with tqdm(total=file_size, unit='B',
              unit_scale=True, unit_divisor=1024,
              desc='government_interest.tsv.zip', initial=initial_pos,
              ascii=True, miniters=1) as pbar:
        for chunk in r.iter_content(32 * 1024):
            f.write(chunk)
            pbar.update(len(chunk))
```

    government_interest.tsv.zip: 100%|#################################################| 3.71M/3.71M [00:26<00:00, 254kB/s]
    

# Complete script

At last, here is the complete script.

<script src="https://gist.github.com/tobiasraabe/58adee67de619ce621464c1a6511d7d9.js"></script>
