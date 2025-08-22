# Create an example EMX mixing matrix heatmap and save it for the user.
import numpy as np
import matplotlib.pyplot as plt
import os

labels = ["joy","sadness","acceptance","disgust","fear","anger","surprise","anticipation"]

# Example directed influence matrix M[row -> column]
M = np.array([
    # to:   joy   sad   acc   dis   fear  anger surpr anticip
    [ 0.60, -0.40, 0.30, -0.20, -0.20, -0.30, 0.10,  0.20],  # joy
    [-0.40,  0.60,-0.20,  0.00,  0.20,  0.00, 0.05, -0.20],  # sadness
    [ 0.20,  0.00, 0.60, -0.30,  0.00, -0.10, 0.00,  0.10],  # acceptance
    [-0.20,  0.00,-0.50,  0.60,  0.05,  0.20, 0.00,  0.00],  # disgust
    [-0.20,  0.10, 0.00,  0.00,  0.60,  0.20, 0.20,  0.00],  # fear
    [-0.30,  0.00,-0.20,  0.20,  0.10,  0.60, 0.00,  0.00],  # anger
    [ 0.05,  0.05, 0.00,  0.00,  0.10,  0.00, 0.60,  0.30],  # surprise
    [ 0.10, -0.10, 0.10,  0.00,  0.00,  0.00, 0.10,  0.60],  # anticipation
])

fig, ax = plt.subplots(figsize=(6.5, 5.5))
im = ax.imshow(M, aspect='equal')  # default colormap
ax.set_xticks(range(len(labels)))
ax.set_yticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_yticklabels(labels)
ax.set_xlabel("to emotion")
ax.set_ylabel("from emotion")
cbar = plt.colorbar(im, ax=ax)
cbar.set_label("influence (-1 inhibit, +1 amplify)")
plt.title("EMX Mixing Matrix (example)")
plt.tight_layout()


out_dir = r"C:\Users\adsmi\Documents\matrixemotion\docs\diagrams"
os.makedirs(out_dir, exist_ok=True)

out_path = os.path.join(out_dir, "emx_matrix_heatmap.png")
plt.savefig(out_path, dpi=200)
print("Saved diagram to:", out_path)
