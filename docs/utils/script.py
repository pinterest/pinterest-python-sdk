import os

modules = [
    "ads",
    "bin",
    "client",
    "organic",
    "utils",
]

def clean_up_old_doc():
    print("----------------- " + "Cleaning up old docs")

    files = next(os.walk("docs/pinterest"), (None, None, []))[2]
    for file in files: os.remove(f"docs/pinterest/{file}")

def generate_new_doc():
    print("----------------- " + "Generating md docs")

    from lazydocs import generate_docs
    generate_docs(["pinterest"], output_path=f"docs/pinterest/")

def create_file_index():
    print("----------------- " + "Indexing docs")

    file_mapping = {
        "extra": list()
    }
    files = next(os.walk("docs/pinterest"), (None, None, []))[2]
    for file in files:
        found_matching_module = False
        for module in modules:
            if len(file) < len(module):
                continue

            if file.find(module) == 0:
                if module not in file_mapping:
                    file_mapping[module] = []
                file_mapping[module].append(file)
                found_matching_module = True
                break
        if not found_matching_module:
            file_mapping["extra"].append(file)
    
    total_mapping = 0
    for k,v in file_mapping.items():
        print(k,v)
        total_mapping += len(v)

    if len(files) != total_mapping:
        raise Exception("Cound't map all files, please run script again!")

    print("Total file maps: " + str(total_mapping))
    return file_mapping

clean_up_old_doc()
generate_new_doc()
create_file_index()