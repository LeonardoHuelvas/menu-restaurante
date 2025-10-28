import qrcode

# URL de tu GitHub Pages
url = "https://leonardohuelvas.github.io/menu-restaurante/"

# Generar el QR
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_Menu_Restaurante.png")

print("✅ QR del menú generado correctamente: QR_Menu_Restaurante.png")
