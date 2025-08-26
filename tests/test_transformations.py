import unittest
import numpy as np
import sys
import os

# Add the project root to the Python path to allow importing from src
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.transformations import apply_transformations

class TestTransformations(unittest.TestCase):

    def test_apply_transformations_shape(self):
        """Test that the output arrays have the correct shape."""
        points = np.array([[1, 2], [3, 4]])
        rotated, scaled, composite = apply_transformations(points)
        self.assertEqual(rotated.shape, points.shape)
        self.assertEqual(scaled.shape, points.shape)
        self.assertEqual(composite.shape, points.shape)

    def test_90_degree_rotation(self):
        """Test the rotation logic with a simple 90-degree rotation."""
        point = np.array([[2.0, 3.0]])
        
        # We test with a 90-degree angle for a predictable result.
        # cos(90) = 0, sin(90) = 1.
        # Rotation matrix R = [[0, -1], [1, 0]]
        # Expected result: [x, y] @ R.T = [2, 3] @ [[0, 1], [-1, 0]] = [-3, 2]
        expected_rotated_point = np.array([[-3.0, 2.0]])

        rotated, _, _ = apply_transformations(point, angle_deg=90.0, scale_factor=1.0)
        
        # Use np.allclose for safe floating-point comparisons
        self.assertTrue(np.allclose(rotated, expected_rotated_point))

if __name__ == '__main__':
    unittest.main()
