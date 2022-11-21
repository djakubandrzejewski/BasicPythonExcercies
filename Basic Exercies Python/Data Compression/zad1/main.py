from zipfile import ZipFile
with ZipFile("data.zip", "w") as f:
    f.write("data.dat")