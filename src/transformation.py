from typing import List, Tuple

import SimpleITK as sitk
import numpy as np

def transform_contour_points(
    contours: List[List[Tuple[float, float, float]]],
    dicom_image: sitk.Image
) -> List[Tuple[float, float, float]]:
    """
    Transforms contour points from the XML coordinate basis to the DICOM coordinate basis.

    Args:
        contours (List[List[Tuple[float, float, float]]]): List of contours, where each
            contour is represented as a list of (x, y, z) coordinates.
        dicom_image (sitk.Image): The DICOM image from which to extract transformation information.

    Returns:
        List[Tuple[float, float, float]]: List of transformed contour points.
    """
    # Extract necessary transformation information from the DICOM header
    # and compute the transformation
    transformed_points = []
    for contour in contours:
        for point in contour:
            # Convert points from the XML coordinate basis to the DICOM coordinate basis
            try:
                transformed_point = dicom_image.TransformPhysicalPointToContinuousIndex(point)
            except:
                continue
            transformed_points.append(transformed_point)

    return transformed_points
