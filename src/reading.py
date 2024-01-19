from pathlib import Path
from typing import Union, Tuple, Dict, Any, List
from xml.etree import ElementTree as ET

import SimpleITK as sitk

def read_dicom_series(dicom_folder: Union[str, Path]) -> Tuple[sitk.Image, List[int]]:
    """
    Reads a DICOM series and returns the image and its dimensions.

    Args:
        dicom_folder (Union[str, Path]): The folder path containing the DICOM series.

    Returns:
        Tuple[sitk.Image, List[int]]: A tuple containing the 3D image and its shape
        as [width, height, depth].
    """
    # Read the DICOM series as a 3D image
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(str(dicom_folder))
    reader.SetFileNames(dicom_names)
    image: sitk.Image = reader.Execute()
    dicom_shape = [image.GetWidth(), image.GetHeight(), image.GetDepth()]
    return image, dicom_shape

def parse_xml_contours(
    xml_file: Union[str, Path]
) -> List[List[Tuple[float, float, float]]]:
    """
    Parses the XML file and extracts the contour information.

    Args:
        xml_file (Union[str, Path]): Path to the XML file containing contour data.

    Returns:
        List[List[Tuple[float, float, float]]]: A list of contours, where each contour is
        represented as a list of (x, y, z) coordinates.

    Raises:
        FileNotFoundError: If the XML file does not exist.
        ET.ParseError: If there is an error parsing the XML file.
    """
    # Convert to Path object if necessary
    xml_file = Path(xml_file)

    # Check if the XML file exists
    if not xml_file.exists():
        raise FileNotFoundError(f"XML file {xml_file} does not exist.")

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize a list to hold all contours
    all_contours = []

    # Iterate through each Contour element in the XML
    for contour in root.findall(".//Contour"):
        # Initialize a list to hold points for the current contour
        contour_points = []

        # Iterate through each point in the contour
        for point in contour.findall(".//Pt"):
            # Split the point text to get x, y, z coordinates
            x, y, z = map(float, point.text.split(","))

            # Add the point to the contour points list
            contour_points.append((x, y, z))

        # Add the current contour to the all contours list
        all_contours.append(contour_points)

    return all_contours