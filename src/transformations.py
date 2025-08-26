import numpy as np
from numpy.typing import NDArray

def apply_transformations(
    points: NDArray[np.float64], 
    angle_deg: float = 45.0, 
    scale_factor: float = 1.5
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """Applies rotation, scaling, and composite transformations to 2D points.

    Args:
        points: An array of 2D points, shape (n, 2).
        angle_deg: The rotation angle in degrees. Defaults to 45.0.
        scale_factor: The scaling factor. Defaults to 1.5.

    Returns:
        A tuple containing:
            - rotated_points: Points after rotation.
            - scaled_points: Points after scaling.
            - composite_points: Points after rotation followed by scaling.
    """
    angle_rad = np.radians(angle_deg)

    # Rotation matrix
    R = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])

    # Scaling matrix
    S = np.array([
        [scale_factor, 0],
        [0, scale_factor]
    ])

    # Apply transformations
    rotated_points = points @ R.T
    scaled_points = points @ S.T
    composite_points = rotated_points @ S.T
    
    return rotated_points, scaled_points, composite_points
