import qrcode

number = int(input("How Many QR Codes you wanted?\n"))

for i in range (1, number + 1):
    data = input(f"Enter URL {i}: ")
    file_path = f"C:\\Users\\anike\\OneDrive\\Desktop\\QRCode\\QRCode{i}.png"

    qr = qrcode.QRCode(
        box_size = 10,
        border = 4,
        version = 1
    )

    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill_color = "black", back_color = "yellow")

    img.save(file_path)

print("All QR Codes Saves successfully.")