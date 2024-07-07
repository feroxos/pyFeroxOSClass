import OpenSSL.crypto

def get_certificate_info(file_path, password=None):
    with open(file_path, 'rb') as file:
        data = file.read()

    if file_path.endswith('.p12') or file_path.endswith('.jks'):
        p12 = OpenSSL.crypto.load_pkcs12(data, password)
        cert = p12.get_certificate()
    else:
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, data)

    issuer = cert.get_issuer()
    subject = cert.get_subject()
    not_after = cert.get_notAfter()
    not_before = cert.get_notBefore()

    return {
        'issuer': issuer,
        'subject': subject,
        'notAfter': not_after.decode(),
        'notBefore': not_before.decode(),
    }
##Rivedere le funzioni confermando che alcuni adpoint vadano a buon fine