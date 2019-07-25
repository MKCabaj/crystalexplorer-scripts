import sbf
import numpy as np
import matplotlib.pyplot as plt
import re
import glob


def histogram(surface_file):
    de, di = read_de_di(surface_file)
    return np.histogram2d(di, de, bins=200, range=((0, 2.5), (0, 2.5)))

def read_de_di(surface_file):
    f = sbf.read_file(surface_file)
    return f['d_e'].data, f['d_i'].data

def main():
#    import argparse
#    parser = argparse.ArgumentParser()    
#    parser.add_argument('surface_file1',
#                        help='CrystalExplorer surface file in .sbf format')
#    parser.add_argument('surface_file2',
#                        help='CrystalExplorer surface file in .sbf format')
#    args = parser.parse_args()
#    print(args.surface_file1)
    fig, axes = plt.subplots(1, 3)
    fig.set_size_inches(12, 4)
    H1, xedges, yedges = histogram(surface_files[i])
    H2, _, _ = histogram(surface_files[i+1])
    X, Y = np.meshgrid(xedges, yedges)
    H1[H1 == 0] = np.nan
    H2[H2 == 0] = np.nan
    surface_file1_title = re.sub(r'\.\w*','', str(surface_files[i]))
    surface_file2_title = re.sub(r'\.\w*','', str(surface_files[i+1]))
    c = axes[0].pcolormesh(X, Y, H1, cmap='coolwarm')
    axes[0].set_title(surface_file1_title)
    c = axes[1].pcolormesh(X, Y, H2, cmap='coolwarm')
    axes[1].set_title(surface_file2_title)
    c = axes[2].pcolormesh(X, Y, H1-H2, cmap='coolwarm')
    axes[2].set_title(surface_file1_title + " - " + surface_file2_title)
    for ax in axes:
        ax.set_xlabel(r'$d_i$')
        ax.set_ylabel(r'$d_e$')
        ax.grid()     
    plt.savefig(surface_file1_title + "_" + surface_file2_title + ".png", dpi=300, bbox_inches='tight')
    
surface_files = glob.glob('*.cxs')
    
i=0
while i < len(surface_files)-1:    
    if __name__ == '__main__':
        main()
        i+=1
