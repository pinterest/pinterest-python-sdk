# Documentation guide

The documentation for this library has been generated using [lazydocs](https://github.com/ml-tooling/lazydocs). If you make change to this library, please use `script.py` to regenerate the documentation.

## Steps to generate documentation

Run `script.py`:
1. Module name as prefix: we can leverage this for indexing but then we have to truncate them out. Look into `create_file_index()` in `scripts.py`
2. Lazydocs built-in ignore-module doesn't work properly with its generator, in this case `ads/__init__.py` generates into `ads.md` which is "accidentally" duplicates with our `ads/ads.py` model. So that we have to use our own `IGNORED_MODULES` to filter out this file.
3. At the end of the process, to display on https://developers.pinterest.com we append all doc to `skeleton-spec.yaml` results in `python-sdk-doc.yaml`.
