import sys
import os
import glob

from PyPDF2 import PdfFileMerger

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Input argument 'filepath' is missing")

    filepath = sys.argv[1]

    merger = PdfFileMerger()

    [merger.append(file) for file in glob.glob(filepath + "*")]

    filepath = os.path.abspath(filepath + ".pdf")

    if os.path.exists(filepath):
        raise FileExistsError(filepath)

    merger.write(filepath)
