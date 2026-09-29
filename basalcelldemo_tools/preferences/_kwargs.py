"""
Project-wide constants and default configurations.

Importing this module automatically optimizes matplotlib font settings,
ensuring that exported PDFs contain editable text (e.g., for Adobe Illustrator)
rather than vectorized paths.

**Note**: non-class or non-function variables are not documented by Sphinx
"""

from pathlib import Path

import matplotlib as mpl

mpl.rcParams.update(
    {
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)

kwarg_savefig = {
    "facecolor": "white",
    "dpi": 600,
    "bbox_inches": "tight",
    "pad_inches": 0.05,
    "transparent": True,
}
"""
dict: Default keyword arguments for saving matplotlib figures (`savefig`).
Configured to output high-resolution (600 dpi), transparent images with
minimized margins, optimized for academic publications and presentations.
"""

OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "docs/jupyternb/output"
"""
pathlib.Path: Absolute path to the base directory for exporting analysis results and
figures from Jupyter Notebooks.
"""

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
"""
pathlib.Path: Absolute path to the directory storing raw and intermediate processed data
for the project.
"""

CellTypist_Models = Path(__file__).resolve().parent.parent / "celltypist_models"
"""
pathlib.Path: Absolute path to the directory containing CellTypist model files used for
cell type annotation.
"""
