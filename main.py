import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# ==============================================
# 🎯 CONFIGURACIÓN PRINCIPAL
# ==============================================
URL_MENU = "https://leonardohuelvas.github.io/menu-restaurante/"
COLOR_QR = "#764ba2"  # Color morado igual al de tu plantilla
FONDO_QR = "#ffffff"  # Blanco de fondo
NOMBRE_ARCHIVO = "QR_Menu_MegaBolis.png"

print("=" * 60)
print("🍽️ GENERADOR DE CÓDIGO QR PARA TU MENÚ DIGITAL")
print("=" * 60)
print(f"🔗 Enlace configurado: {URL_MENU}\n")

# ==============================================
# 🧩 FUNCIONES DE GENERACIÓN
# ==============================================

def generar_qr_estilo():
    """Genera un QR redondeado y a color profesional."""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=4,
        )
        qr.add_data(URL_MENU)
        qr.make(fit=True)

        # Generar imagen con estilo y colores
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            fill_color=COLOR_QR,
            back_color=FONDO_QR
        )

        img.save(NOMBRE_ARCHIVO)
        print("✅ QR generado con éxito:", NOMBRE_ARCHIVO)
        print("📱 Escanéalo con tu celular y abrirá directamente el menú.")
        print("🖨️ Ideal para impresión o stickers de mesa.\n")

    except Exception as e:
        print(f"❌ Error al generar el QR: {e}")
        print("💡 Solución: instala dependencias con → pip install qrcode[pil]")


def generar_qr_basico():
    """Genera un QR clásico en blanco y negro (respaldo)."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(URL_MENU)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QR_Menu_Basico.png")
    print("✅ QR básico generado: QR_Menu_Basico.png (modo respaldo)\n")


# ==============================================
# 🚀 EJECUCIÓN PRINCIPAL
# ==============================================
if __name__ == "__main__":
    print("Generando QR con diseño personalizado...\n")
    generar_qr_estilo()
    generar_qr_basico()
    print("=" * 60)
    print("✨ ¡Listo! Tus QR están listos para usar en el negocio 🍹")
    print("=" * 60)
