from pathlib import Path

import click

from src.contours2nii import save_nifti, create_masks_from_contours
from src.reading import read_dicom_series, parse_xml_contours
from src.transformation import transform_contour_points
from src.utils import determine_dicom_folder_based_on_xml

@click.command()
@click.option('--dicom_folder', type=click.Path(exists=True), default=None)
@click.argument("xml_input", type=click.Path(exists=True))
@click.option("--output_folder", type=click.Path(), default=None)
def main(dicom_folder: str, xml_input: str, output_folder: str):
    """
    Command Line Tool to read DICOM images, process XML contour data, and save as NIFTI files.

    Args:
        dicom_folder (str, optional): Path to the folder with DICOM images.
        xml_input (str): Path to the XML file or folder with XML files.
        output_folder (str, optional): Path to save the NIFTI files.
    """

    # Check if xml_input is a directory or a file
    xml_path = Path(xml_input)
    if xml_path.is_dir():
        xml_files = list(xml_path.glob("*.xml"))
    else:
        xml_files = [xml_path]

    for xml_file in xml_files:
        # Determine the DICOM folder based on xml_input if not provided
        if not dicom_folder:
            dicom_folder = determine_dicom_folder_based_on_xml(xml_file)

        # Use xml file parent directory as output folder if not provided
        if not output_folder:
            output_folder = xml_file.parent

        # Read DICOM series and parse XML contours
        dicom, dicom_shape = read_dicom_series(dicom_folder)
        contours = parse_xml_contours(xml_file)

        # Transform contour points
        transformed_contours = transform_contour_points(contours, dicom)

        # Create mask array from contours
        mask_array = create_masks_from_contours(transformed_contours, dicom_shape)

        # Save the mask array as a NIFTI file
        nifti_output = Path(output_folder) / (xml_file.stem + '_mask.nii.gz')
        save_nifti(mask_array, nifti_output)
