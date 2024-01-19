from pathlib import Path
from typing import List, Tuple, Union

import nibabel as nib
import numpy as np
from scipy.spatial import ConvexHull, Delaunay

def create_masks_from_contours(
    contours: List[List[Tuple[float, float, float]]],
    dicom_array_shape: Tuple[int, int, int],
) -> np.ndarray:
    """
    Creates binary masks from contour data based on the shape of the DICOM array.

    Args:
        contours (List[List[Tuple[float, float, float]]]): A list of contours, where each
            contour is represented as a list of (x, y, z) coordinates.
        dicom_array_shape (Tuple[int, int, int]): The shape of the DICOM array (width, height, depth).

    Returns:
        np.ndarray: A 3D numpy array representing the binary mask.
    """
    # Convert contours to a numpy array
    contours = np.array(contours)
    width, height, depth = dicom_array_shape

    # Create a convex hull from the contour points
    hull = ConvexHull(contours.reshape(-1, 3))

    # Generate a grid of points covering the DICOM array dimensions
    x, y, z = np.meshgrid(np.arange(width), np.arange(height), np.arange(depth))
    grid_points = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T

    # Use Delaunay triangulation to create a mask from the convex hull
    delaunay = Delaunay(contours[hull.vertices])
    mask = delaunay.find_simplex(grid_points) >= 0

    return mask.reshape(width, height, depth).astype(np.int16)

def save_nifti(mask_array: np.ndarray, output_file: Union[str, Path]):
    """
    Saves a binary mask array to a NIFTI file.

    Args:
        mask_array (np.ndarray): A 3D numpy array representing the binary mask.
        output_file (Union[str, Path]): The file path where the NIFTI file will be saved.

    Raises:
        ValueError: If mask_array is not a 3D array.
    """
    # Ensure the mask array is 3D
    if mask_array.ndim != 3:
        raise ValueError("mask_array must be a 3D array.")

    # Convert to Path object if necessary
    output_file = Path(output_file)

    # Create a NIFTI image from the mask array and save it
    nifti_img = nib.Nifti1Image(mask_array, affine=np.eye(4))
    nib.save(nifti_img, str(output_file))
