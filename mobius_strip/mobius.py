import numpy as np
from scipy.integrate import simps
from scipy.spatial.distance import euclidean

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u_vals = np.linspace(0, 2 * np.pi, n)
        self.v_vals = np.linspace(-w / 2, w / 2, n)
        self.x, self.y, self.z = self.compute_mesh()

    def parametric_equations(self, u, v):
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_mesh(self):
        u, v = np.meshgrid(self.u_vals, self.v_vals)
        x, y, z = self.parametric_equations(u, v)
        return x, y, z

    def compute_surface_area(self):
        du = self.u_vals[1] - self.u_vals[0]
        dv = self.v_vals[1] - self.v_vals[0]
        dx_du = np.gradient(self.x, du, axis=1)
        dx_dv = np.gradient(self.x, dv, axis=0)
        dy_du = np.gradient(self.y, du, axis=1)
        dy_dv = np.gradient(self.y, dv, axis=0)
        dz_du = np.gradient(self.z, du, axis=1)
        dz_dv = np.gradient(self.z, dv, axis=0)
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv
        area_element = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        area = simps(simps(area_element, self.v_vals), self.u_vals)
        return area

    def compute_edge_length(self):
        edge_coords = [self.parametric_equations(u, self.w / 2) for u in self.u_vals]
        edge_coords += [self.parametric_equations(u, -self.w / 2) for u in reversed(self.u_vals)]
        edge_points = np.array(edge_coords)
        length = sum(
            euclidean(edge_points[i], edge_points[i + 1])
            for i in range(len(edge_points) - 1)
        )
        return length
