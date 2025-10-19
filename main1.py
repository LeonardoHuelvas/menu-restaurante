import qrcode

# CAMBIA ESTO por tu URL de GitHub Pages cuando la tengas
# Ejemplo: "https://tuusuario.github.io/menu-restaurante"
data = "https://tuusuario.github.io/menu-restaurante"

print("=" * 60)
print("🎯 GENERADOR DE QR PARA MENÚ PROFESIONAL")
print("=" * 60)

def generar_qr_menu():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QR_Menu_Final.png")
    print("\n✅ QR generado exitosamente: QR_Menu_Final.png")
    print(f"🔗 URL: {data}")
    print("\n📱 Escanea el QR con tu celular para probar")
    print("🖨️  Listo para imprimir en alta calidad")

if __name__ == "__main__":
    try:
        generar_qr_menu()
        print("\n" + "=" * 60)
        print("✨ ¡Todo listo! Ahora sigue los pasos de configuración")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Ejecuta: pip install qrcode[pil]")