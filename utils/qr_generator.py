import qrcode
import io

def generate_qr_code(text):
    """
    Generate a QR code for the given text.

    Args:
        text (str): The content to encode in the QR code.

    Returns:
        BytesIO: The QR code image in PNG format as a BytesIO stream.
    """
    # Create a QR code instance with desired settings
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=8,  # Size of the QR code boxes
        border=4,  # Border size
    )
    
    # Add data to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a BytesIO stream
    img_stream = io.BytesIO()
    img.save(img_stream, format="PNG")
    img_stream.seek(0)

    return img_stream
