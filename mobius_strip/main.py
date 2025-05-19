import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mobius import MobiusStrip

def main():
    mobius = MobiusStrip(R=1.0, w=0.3, n=300)

    # Surface Area and Edge Length
    surface_area = mobius.compute_surface_area()
    edge_length = mobius.compute_edge_length()
    print(f"Surface Area ≈ {surface_area:.4f}")
    print(f"Edge Length ≈ {edge_length:.4f}")

    # Visualization
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(mobius.x, mobius.y, mobius.z, color='cyan', edgecolor='k', alpha=0.8)
    ax.set_title("Möbius Strip")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
