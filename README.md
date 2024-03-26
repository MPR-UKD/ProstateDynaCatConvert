# ProstateDynaCatConvert

ProstateDynaCatConvert is a Python-based tool designed to read DICOM images and contour data from Philips DynaCAD Prostate and convert them into NIFTI formats. This tool serves as an invaluable resource for medical imaging professionals and researchers, streamlining the processing and analysis of radiological data.

## Key Features

- Processes and converts DICOM and XML data from Philips DynaCAD Prostate into NIFTI files.
- Offers a simple and efficient command-line interface for straightforward data conversion.
- Supports automated builds for macOS, Windows, and Linux via GitHub Actions, ensuring accessibility and ease of use across different platforms.

## System Requirements

- **Python Version:** 3.10 or higher to ensure compatibility with the latest features and security updates.
- **Dependency Management:** Utilizes Poetry for an efficient and reliable dependency management process.

## Installation

To get started with ProstateDynaCatConvert, follow these steps:

1. **Pre-compiled Releases:** Available for macOS, Windows, and Linux on the GitHub project page, these releases simplify the installation process.
2. **Manual Installation:**
   - Ensure Python 3.10 or newer is installed on your system.
   - Install Poetry to handle dependencies efficiently.
   - Clone the repository and navigate into the project directory.
   - Run `poetry install` to set up the environment and install all necessary dependencies.

## Usage

`ProstateDynaConvert.py` is a command-line utility designed for the conversion of DICOM images and XML-based contour data into NIFTI format. It specifically caters to the needs of processing prostate imaging data. 

### Getting Started

Before using `ProstateDynaConvert.py`, ensure you have the following prerequisites:
- DICOM images in a directory.
- An optional XML file with contour data, if contour analysis is part of your workflow.

### How to Execute

Use the following command with the appropriate arguments to execute the tool:

```bash
python ProstateDynaConvert.py --dicom_folder=<path_to_dicom> [--xml_input=<path_to_xml>] [--output_folder=<path_to_output>]
```

This command line interface offers flexibility in specifying the location of your DICOM images, the optional XML file for contour data, and the desired output directory for the NIFTI files.

For a more detailed explanation of each argument and step-by-step guidance through the conversion process, refer to the **[Usage Section](#usage)**.

## Releases

Find pre-built versions of the tool for various operating systems under the Releases section on the GitHub project page. These releases simplify the setup process, allowing you to get started with your data conversion tasks more quickly.

## License

This project is made available under the GNU General Public License v3.0. For full license details, please consult the `LICENSE` file in the project repository.
