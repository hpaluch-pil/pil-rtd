# Pickering Interfaces Ltd. on Read the Docs (rtd)

Introductory Sphinx + Read the Docs pages for Pickering Interfaces Ltd.


Latest version of pages is available on:

* English: https://pil-rtd.readthedocs.io/en/latest/
* Czech: https://pil-rtd.readthedocs.io/cs/latest/

# Setup

TODO: ...


# Building docs locally

Building English version:

```bash
cd docs
make html
```

Buliding Czech version:

```cmd
cd docs
"%SPHINXBUILD%" -b html -D language=cs source build/html/cs
```

