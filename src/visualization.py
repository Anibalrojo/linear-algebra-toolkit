import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

def plot_transformations(
    original_points: NDArray[np.float64], 
    rotated_points: NDArray[np.float64], 
    scaled_points: NDArray[np.float64], 
    composite_points: NDArray[np.float64],
    angle_deg: float,
    scale_factor: float
) -> None:
    """Generates a 2x2 grid of plots to visualize 2D transformations.

    Args:
        original_points: The original set of points, shape (n, 2).
        rotated_points: The points after rotation.
        scaled_points: The points after scaling.
        composite_points: The points after both rotation and scaling.
        angle_deg: The rotation angle in degrees, for plot titles.
        scale_factor: The scaling factor, for plot titles.
    """
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('2D Transformations of a Set of Points', fontsize=16)

    # 1) Rotation
    axs[0, 0].scatter(original_points[:, 0], original_points[:, 1], color='blue', label='Original')
    axs[0, 0].scatter(rotated_points[:, 0], rotated_points[:, 1], color='red', label='Rotated')
    for i in range(len(original_points)):
        axs[0, 0].plot([original_points[i, 0], rotated_points[i, 0]], [original_points[i, 1], rotated_points[i, 1]], 'k--', linewidth=0.8)
    axs[0, 0].set_title(f"Rotation ({angle_deg}°)")
    axs[0, 0].axis('equal')
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # 2) Scaling
    axs[0, 1].scatter(original_points[:, 0], original_points[:, 1], color='blue', label='Original')
    axs[0, 1].scatter(scaled_points[:, 0], scaled_points[:, 1], color='green', label='Scaled')
    for i in range(len(original_points)):
        axs[0, 1].plot([original_points[i, 0], scaled_points[i, 0]], [original_points[i, 1], scaled_points[i, 1]], 'k--', linewidth=0.8)
    axs[0, 1].set_title(f"Scaling ({scale_factor}x)")
    axs[0, 1].axis('equal')
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # 3) Composite Transformation
    axs[1, 0].scatter(original_points[:, 0], original_points[:, 1], color='blue', label='Original')
    axs[1, 0].scatter(rotated_points[:, 0], rotated_points[:, 1], color='red', label='Rotated', alpha=0.6)
    axs[1, 0].scatter(composite_points[:, 0], composite_points[:, 1], color='purple', label='Rotated + Scaled')
    for i in range(len(original_points)):
        axs[1, 0].plot([original_points[i, 0], rotated_points[i, 0]], [original_points[i, 1], rotated_points[i, 1]], 'k--', linewidth=0.6)
        axs[1, 0].plot([rotated_points[i, 0], composite_points[i, 0]], [rotated_points[i, 1], composite_points[i, 1]], 'm--', linewidth=0.6)
    axs[1, 0].set_title("Composite (Rotation + Scaling)")
    axs[1, 0].axis('equal')
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # Leave the bottom-right subplot empty
    axs[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
