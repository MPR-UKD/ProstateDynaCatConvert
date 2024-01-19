from pathlib import Path
from typing import Optional

def determine_dicom_folder_based_on_xml(xml_path: Path) -> Optional[str]:
    """
    Determines the DICOM folder path based on the provided XML file path.

    This function attempts to locate the DICOM folder by progressively truncating
    the XML file name and searching for a matching folder in the same directory.

    Args:
        xml_path (Path): The path of the XML file.

    Returns:
        Optional[str]: The path of the determined DICOM folder, if found.

    Raises:
        ValueError: If it is not possible to determine the DICOM folder.
    """
    # Remove a specific prefix from the XML file name to generate a potential folder name
    folder_name = xml_path.stem.replace("pseg.", "")
    parent_dir = xml_path.parent

    # Iteratively check for a matching folder by truncating the file name
    for count in range(1, len(folder_name) + 1):
        possible_folders = list(parent_dir.glob(folder_name[:count] + "*"))

        # Return the path if exactly one possible folder is found
        if len(possible_folders) == 1:
            return str(possible_folders[0])

        # If no folders are found, raise an error
        if not possible_folders:
            raise ValueError("Cannot determine DICOM folder; please provide the folder manually.")

    # In case the loop completes without finding a folder, also raise an error
    raise ValueError("Cannot determine DICOM folder; please provide the folder manually.")
