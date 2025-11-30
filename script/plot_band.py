from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load vasprun.xml
# -------------------------------
vasp = Vasprun("../band/vasprun.xml",
               parse_projected_eigen=True,
               parse_potcar_file=False)

bs = vasp.get_band_structure(line_mode=True)
dos = vasp.complete_dos

# -------------------------------
# 2. Band gap info
# -------------------------------
gap = bs.get_band_gap()
print("\n===== Band Gap Information =====")
print(f"Band gap (eV):  {gap['energy']:.4f}")
print(f"Direct?         {'Yes' if gap['direct'] else 'No'}")
print(f"Transition:     {gap['transition']}")
print("================================\n")

# -------------------------------
# 3. Draw band structure 
# -------------------------------
bs_plotter = BSPlotter(bs)
ax_band = bs_plotter.get_plot()
fig_band = ax_band.get_figure()

# 设置传统样式
ax_band.set_ylim(-6, 6)

fig_band.savefig("band_structure.png", dpi=300, bbox_inches="tight")
fig_band.savefig("band_structure.pdf", dpi=300, bbox_inches="tight")
plt.close(fig_band)
print("Saved: band_structure.png, band_structure.pdf")

# -------------------------------
# 4. Draw Band + DOS 
# -------------------------------
bd_plotter = BSDOSPlotter()

fig_bd = bd_plotter.get_plot(bs, dos)


ax_band = fig_bd[0]
ax_dos = fig_bd[1]


fig = ax_band.get_figure()

ax_band.set_ylim(-6, 6)
ax_dos.set_ylim(-6, 6)

fig.savefig("band_dos.png", dpi=300, bbox_inches="tight")
fig.savefig("band_dos.pdf", dpi=300, bbox_inches="tight")
plt.close(fig)
print("Saved: band_dos.png, band_dos.pdf")
