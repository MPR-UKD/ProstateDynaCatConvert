from pathlib import Path
from typing import List
import click
from click.testing import CliRunner
from ProstateDynaCatConvert import cli
from tqdm import tqdm

root = Path("D:/PostDoc")

import warnings

warnings.filterwarnings("ignore")


def find_all_segmentations(root_folder: Path) -> List[Path]:
    """Use a list comprehension with the rglob method of Path to find all .xml files."""
    return [file for file in root_folder.rglob('*.xml')]


segmentations = find_all_segmentations(root)

# Find all patients
patients = set([_.parent for _ in segmentations])

runner = CliRunner()

for patient in tqdm(patients):
    for dicom_folder in patient.glob('*'):
        if dicom_folder.is_dir():
            # Invoke the CLI
            result = runner.invoke(cli, [
                '--dicom_folder', str(dicom_folder),
            ])
