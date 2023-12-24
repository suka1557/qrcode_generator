import qrcode

def generate_qr_code_with_data(data_to_be_encoded: dict):
    """
    function that takes in dictinary of data to be encoded into QR Code 
    and generates a QR Code image file
    
    """

    customer_id = str(data_to_be_encoded["customer_id"])
    base_url = str(data_to_be_encoded["url"])
    table_no = str(data_to_be_encoded["table_no"])

    custom_url = base_url + "?customer_id=" + customer_id + "?table_no=" + table_no

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(custom_url)
    qr.make(fit=True)

    qrcode_img = qr.make_image(fill_color="black", back_color="white")
    # qrcode_img.save("qrcode.png")

    return qrcode_img
