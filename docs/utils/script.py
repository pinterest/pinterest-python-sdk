import os
import sys
import yaml
import markdown

MODULES = [
    "ads",
    "bin",
    "client",
    "organic",
    "utils",
]

IGNORED_FILES_INDEXING = {
    "ads.md", #Ignore this file since ads/__init__.py is converted into ads.md
    "organic.md",
    "utils.md",
    "README.md",
    ".pages",
}

IGNORE_MODULES = [
    "bin",
    "config",
    "version",
]

PROJECT_PATH = os.path.abspath(os.getcwd())


def set_up_python_path():
    """
    Set up python path
    """
    sys.path.append(PROJECT_PATH)


def remove_old_doc():
    """
    Remove old doc in docs/pinterest
    """
    print("----------------- " + "Cleaning up old docs")

    files = next(os.walk("docs/pinterest"), (None, None, []))[2]
    for file in files: os.remove(f"docs/pinterest/{file}")


def generate_new_doc():
    """
    Use lazydoc to generate new doc at: docs/pinterest
    """
    print("----------------- " + "Generating md docs")

    from lazydocs import generate_docs
    generate_docs(
        ['pinterest'],
        ignored_modules=IGNORE_MODULES,
        watermark=False,
        remove_package_prefix=True,
        overview_file='README.md',
        output_path='docs/pinterest/',
        src_base_url='https://github.com/pinterest/pinterest-python-sdk/blob/main/')


def sort_index(index: dict) -> dict:
    """Sort index by key and value

    Args:
        index (dict): unsorted index

    Returns:
        dict: sorted index
    """
    return_index = {}
    for k,v in index.items():
        return_index[k] = sorted(v)

    return_index = dict(sorted(return_index.items(), key=lambda item: item[0]))
    return return_index


def remove_module_prefix_from_file(file: str, module: str) -> str:
    """Remove module prefix from file name
    By default, lazydocs add module as prefix
    ex: ads.ad_groups.md -> ad_groups.md

    Args:
        file (str): file to rename
        module (str): module of file

    Returns:
        str: new file name
    """
    new_name = file
    if file != (module + ".md") and file.find(module) == 0:
        new_name = file[len(module)+1:]
    return new_name


def check_index(num_file: int, index: dict):
    """Check if we index corrent number of files

    Args:
        num_file (int): number of file to be indexed
        index (dict): the index

    Raises:
        Exception: Couldn't index all file
    """
    print("Files to index: " + str(num_file))
    num_file_indexed = sum([len(value) for value in index.values()])
    print("Total file indexed: " + str(num_file_indexed))

    if num_file != num_file_indexed:
        raise Exception("Cound't index all file, please double check")


def create_file_index() -> dict:
    """
    Create file index: index[module_name] = list[file_name]

    This function also get rid of the module prefix that lazydocs added in every file

    Note: all the file without module, such as configs.py, version.py is mapped
    to index["extra"]

    Returns:
        dict: file index
    """
    print("----------------- " + "Indexing docs")

    index = {}
    extra_mapping = []
    files = next(os.walk("docs/pinterest"), (None, None, []))[2]

    for file in files:
        if file in IGNORED_FILES_INDEXING: 
            continue

        found_matching_module = False
        for module in MODULES:
            if len(file) < len(module):
                continue

            if file.find(module) == 0:
                if module not in index:
                    index[module] = []
                index[module].append(file)

                found_matching_module = True
                break

        if not found_matching_module:
            extra_mapping.append(file)
    
    return_index = sort_index(index)

    if extra_mapping:
        return_index["extra"] = extra_mapping

    check_index(len(files)-len(IGNORED_FILES_INDEXING), return_index)

    return return_index


def truncate_md_extension(file: str) -> str:
    """Truncate .md file extension

    Args:
        file (str): file name

    Returns:
        str: origin file name
    """
    return file[:-3]


def append_doc_to_spec_file(index: dict):
    """
    Accord to index file, append docs to spec skeleton spec and overwrite it to python-sdk-doc.yaml

    Args:
        index (dict): file index
    """
    print("----------------- " + "Appending doc to spec file")

    # Get skeleton spec
    spec_path = PROJECT_PATH + '/docs/utils/skeleton-spec.yaml'
    spec = yaml.safe_load(open(spec_path, 'r'))

    # Update version
    from pinterest.version import __version__
    spec['info']['version'] = __version__

    # Appending md doc into skeleton spec
    spec['tags'] = []
    spec['x-tagGroups'] = []
    for module, md_files in index.items():
        tag_names = []
        for md_file in md_files:
            name = truncate_md_extension(remove_module_prefix_from_file(md_file, module))
            tag_names.append(name)
            spec['tags'].append(
                {
                    "name": name,
                    "description": markdown.markdown(open(PROJECT_PATH + '/docs/pinterest/' + md_file, 'r').read()),
                    "x-traitTag": False,
                }
            )
        spec['x-tagGroups'].append(
            {
                "name": 'pinterest.' + module,
                "tags": tag_names,
            }
        )
    
    # Overwrite new spec to python-sdk-doc.yaml
    with open(PROJECT_PATH + '/docs/utils/python-sdk-doc.yaml', 'w') as file:
        yaml.dump(spec, file)


def start_doc():
    """
    Use this function to generate documentations
    """
    set_up_python_path()

    remove_old_doc()

    generate_new_doc()

    index = create_file_index()

    append_doc_to_spec_file(index)

start_doc()
