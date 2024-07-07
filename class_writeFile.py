import zipfile
import tarfile
import gzip
##files = ['file1.txt', 'file2.txt', 'file3.txt']
##create_zip(files, 'archive.zip')
def create_zip(files, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zf:
        for file in files:
            zf.write(file)

def create_tar(files, tar_file):
    with tarfile.open(tar_file, 'w') as tf:
        for file in files:
            tf.add(file)

def create_gz(files, gz_file):
    with gzip.open(gz_file, 'wb') as zf:
        for file in files:
            with open(file, 'rb') as f:
                zf.write(f.read())
def writeFile(fileName,typeWrite,testo):
    try:
        f = open(fileName, typeWrite)
        f.write(testo)
        f.close()
        return True
    except:
        return False