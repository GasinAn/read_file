import requests
import gzip

GAIADR3_SAM_URL = "https://cdsarc.cds.unistra.fr/ftp/I/355/gaiadr3.sam.gz"

def download_gaiadr3_sam():
    r = requests.get(GAIADR3_SAM_URL)
    r.raise_for_status()
    with open("gaiadr3.sam.gz", "wb") as gaiadr3_sam_gz:
        gaiadr3_sam_gz.write(r.content)
    with gzip.open("gaiadr3.sam.gz", "rb") as gaiadr3_sam_gz:
        content = gaiadr3_sam_gz.read().decode("ASCII")
    with open("gaiadr3.sam", "w") as gaiadr3_sam:
        gaiadr3_sam.write(content)

def test_read_txt():
    download_gaiadr3_sam()

def test():
    test_read_txt()

if (__name__ == "__main__"):
    test()
