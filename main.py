import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# Tu enlace de Google Drive
data = "https://drive.google.com/uc?export=view&id=1ylxivbR5CIIKBYbcmEIHUR3eDHjwAHAi"

# Opción 1: QR básico (tu código original mejorado)
def generar_qr_basico():
    qr = qrcode.QRCode(
        version=1,  # Controla el tamaño (1 es el más pequeño)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección de errores
        box_size=10,  # Tamaño de cada cuadrito
        border=4,  # Borde blanco alrededor
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QR_Menu_Basico.png")
    print("✅ QR básico generado: QR_Menu_Basico.png")

# Opción 2: QR con bordes redondeados (más moderno)
def generar_qr_redondeado():
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer()
    )
    img.save("QR_Menu_Redondeado.png")
    print("✅ QR redondeado generado: QR_Menu_Redondeado.png")

# Opción 3: QR con colores personalizados
def generar_qr_colores():
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Cambia los colores aquí (fill_color es el QR, back_color es el fondo)
    img = qr.make_image(fill_color="#1a472a", back_color="#ffffff")
    img.save("QR_Menu_Colores.png")
    print("✅ QR con colores generado: QR_Menu_Colores.png")

# Ejecutar las funciones
if __name__ == "__main__":
    print("🔗 Enlace usado:", data)
    print("\nGenerando códigos QR...\n")
    
    generar_qr_basico()
    generar_qr_redondeado()
    generar_qr_colores()
    
    print("\n✨ Todos los QR han sido generados exitosamente!")
    print("📱 Prueba escanearlos con tu celular para verificar que funcionen")