import click
from pathlib import Path

from contours2nii import save_nifti, create_masks_from_contours
from reading import read_dicom_series, parse_xml_contours
from transformation import transform_contour_points

@click.command()
@click.option('--dicom_folder', required=True, type=click.Path(exists=True), help="Path to the folder with DICOM images.")
@click.option('--xml_input', type=click.Path(exists=True), default=None, help="Optional path to the XML file containing contour data. If not provided, the script attempts to find XML files in the DICOM folder.")
@click.option('--output_folder', type=click.Path(), default=None, help="Optional path to save the NIFTI files. Defaults to the DICOM folder if not specified.")
def cli(dicom_folder: str, xml_input: str = None, output_folder: str = None):
    """
    Command Line Tool to read DICOM images, process XML contour data, and save as NIFTI files.

    This script reads DICOM series from a specified folder, processes XML contour data
    to create mask arrays, and saves these arrays as NIFTI files in an output directory.

    Args:
        dicom_folder (str): Path to the folder with DICOM images.
        xml_input (str, optional): Path to the XML file containing contour data. If not provided,
                                   it searches for XML files in the DICOM folder.
        output_folder (str, optional): Path to save the NIFTI files. Defaults to the DICOM folder if not specified.
    """

    # Check if xml_input is a directory or a file
    if xml_input is None:
        xml_files = list(Path(dicom_folder).parent.glob("*.xml"))
    else:
        xml_files = [xml_input]

    if output_folder is None:
        output_folder = dicom_folder
    for xml_file in xml_files:
        # Read DICOM series and parse XML contours
        dicom, dicom_shape = read_dicom_series(dicom_folder)
        contours = parse_xml_contours(xml_file)
        if len(contours) == 0:
            continue
        # Transform contour points
        transformed_contours = transform_contour_points(contours, dicom)

        # Create mask array from contours
        mask_array = create_masks_from_contours(transformed_contours, dicom_shape).transpose((1, 0, 2))

        # Save the mask array as a NIFTI file
        nifti_output = Path(output_folder) / (xml_file.stem + '_mask.nii.gz')
        save_nifti(mask_array, nifti_output)


if __name__ == '__main__':
    cli()
