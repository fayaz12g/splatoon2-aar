import os

def download_extract_copy(input_folder, mod_name):
    import requests
    import zipfile
    import shutil
    import getpass

    # URL of the ZIP file
    zip_url = "https://github.com/fayaz12g/aar-files/raw/main/splatoon2/Splat.zip"

    username = getpass.getuser()
    directory_path = f"C:/Users/{username}/AppData/Roaming/AnyAspectRatio/perm/splatoon2"
    # Check if the directory exists
    if not os.path.exists(directory_path):
        # Create the directory if it doesn't exist
        os.makedirs(directory_path)
        print(f"Directory {directory_path} created successfully.")
    else:
        print(f"Directory {directory_path} already exists.")
    perm_folder = f"C:/Users/{username}/AppData/Roaming/AnyAspectRatio/perm/splatoon2"
    zip_file_source = os.path.join(perm_folder, "Splat.zip")

    if not os.path.isfile(zip_file_source):
        # Download the ZIP file
        print("Downloading zip file. This may take up to 10 seconds.")
        response = requests.get(zip_url)
        print("Zip file downloaded.")
        with open(zip_file_source, "wb") as file:
            print("Writing contents to temp folder.")
            file.write(response.content)

    # Extract the ZIP file
    extract_folder = os.path.join(input_folder, mod_name, "temp")
    print(f"Extracting zip to {extract_folder}. This can also take a few seconds.")
    with zipfile.ZipFile(zip_file_source, "r") as zip_ref:
        zip_ref.extractall(extract_folder)


    # Copy the extracted file
    print("Copying extracted files")
    romfs_folder = os.path.join(input_folder, mod_name, "romfs")
    extracted_folder = os.path.join(extract_folder)
    src_folder_path = os.path.join(extracted_folder)
    dst_folder_path = os.path.join(romfs_folder, "Layout")

    # Remove the existing destination folder if it exists
    if os.path.exists(dst_folder_path):
        shutil.rmtree(dst_folder_path)

    # Recreate the destination folder and copy the content
    os.makedirs(os.path.dirname(dst_folder_path), exist_ok=True)
    shutil.copytree(src_folder_path, dst_folder_path)

    # Clean up
    print("Cleaning up old files")
    shutil.rmtree(extract_folder)