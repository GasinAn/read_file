from read_file import *

GAIADR3_SAM_URL = "https://cdsarc.cds.unistra.fr/ftp/I/355/gaiadr3.sam.gz"

def download_gaiadr3_sam():
    import requests
    r = requests.get(GAIADR3_SAM_URL)
    r.raise_for_status()
    with open("gaiadr3.sam.gz", "wb") as gaiadr3_sam_gz:
        gaiadr3_sam_gz.write(r.content)

def test_read_txt():
    download_gaiadr3_sam()
    dataframe = read_txt(
        "gaiadr3.sam.gz",
        compression="gzip",
        header=None,
        names=["DR3Name", "RAdeg", "DEdeg"],
        colspecs=[(0, 28), (29, 44), (45, 60)],
        dtype={"DR3Name": str, "RAdeg": float, "DEdeg": float},
    )
    print(f"dataframe.dtypes:\n{dataframe.dtypes}\n")
    print(f"dataframe:\n{dataframe}\n")

def test():
    test_read_txt()

if (__name__ == "__main__"):
    test()
