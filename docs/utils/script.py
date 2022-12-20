import os
import sys
import yaml
import markdown

modules = [
    "ads",
    "bin",
    "client",
    "organic",
    "utils",
]
PROJECT_PATH = os.path.abspath(os.getcwd())

def set_up_python_path():
    sys.path.append(PROJECT_PATH)


def remove_old_doc():
    print("----------------- " + "Cleaning up old docs")

    files = next(os.walk("docs/pinterest"), (None, None, []))[2]
    for file in files: os.remove(f"docs/pinterest/{file}")


def generate_new_doc():
    print("----------------- " + "Generating md docs")

    from lazydocs import generate_docs
    generate_docs(["pinterest"], output_path=f"docs/pinterest/", src_base_url='https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/')


def create_file_index():
    print("----------------- " + "Indexing docs")

    file_mapping = {}
    extra_mapping = []
    files = next(os.walk("docs/pinterest"), (None, None, []))[2]
    for file in files:
        found_matching_module = False
        for module in modules:
            if len(file) < len(module):
                continue

            if file.find(module) == 0:
                # Rename file to get rid of index, ex: ads.ad_groups.md -> ad_groups.md
                new_name = file
                if file != (module + ".md"):
                    new_name = file[len(module)+1:]
                    os.rename(f"docs/pinterest/{file}", f"docs/pinterest/{new_name}")
                # Start indexing new file
                if module not in file_mapping:
                    file_mapping[module] = []
                file_mapping[module].append(new_name)
                found_matching_module = True
                break
        if not found_matching_module:
            extra_mapping.append(file)
    
    total_mapping = len(extra_mapping)
    return_mapping = {}
    for k,v in file_mapping.items():
        # Sort mapping by value
        return_mapping[k] = sorted(v)
        total_mapping += len(v)

    if len(files) != total_mapping:
        raise Exception("Cound't map all files, please double check!")
    
    print("Total file maps: " + str(total_mapping))

    # Sort mapping by index
    return_mapping = dict(sorted(return_mapping.items(), key=lambda item: item[0]))

    # Add `extra`` mapping at the end to make sure the `extra` section
    # appear at the end of the page
    return_mapping["extra"] = extra_mapping

    return  return_mapping


def append_doc_to_spec_file(file_index: dict):
    spec_path = PROJECT_PATH + '/docs/utils/skeleton-spec.yaml'
    spec = yaml.load(open(spec_path, 'r'), Loader=yaml.FullLoader)

    spec['tags'] = []
    spec['x-tagGroups'] = []
    for tag_name, md_files in file_index.items():
        tag_names = []
        for md_file in md_files:
            tag_names.append(md_file)
            spec['tags'].append(
                {
                    "name": md_file,
                    "description": markdown.markdown(open(PROJECT_PATH + '/docs/pinterest/' + md_file, 'r').read()),
                    "x-traitTag": False,
                }
            )
        spec['x-tagGroups'].append(
            {
                "name": 'pinterest.' + tag_name,
                "tags": tag_names,
            }
        )
    with open(PROJECT_PATH + '/docs/utils/python-sdk-doc.yaml', 'w') as file:
        yaml.dump(spec, file)
    return spec

def start_doc():
    set_up_python_path()

    remove_old_doc()

    generate_new_doc()

    index = create_file_index()

    append_doc_to_spec_file(index)

start_doc()