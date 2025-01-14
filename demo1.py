import qrcode
from PIL import Image


def generate_colored_qr_code(data, version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10,
                             border=4, fill_color=(0, 128, 0), back_color=(255, 255, 255)):
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)
    # 生成黑白二维码图像
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # 将黑白二维码图像转换为 RGB 模式，以便进行颜色修改
    qr_img = qr_img.convert("RGB")
    # 获取图像的像素数据
    pixels = qr_img.load()
    width, height = qr_img.size
    # 将指定颜色应用到二维码的黑色部分
    for i in range(width):
        for j in range(height):
            if pixels[i, j] == (0, 0, 0):  # 黑色部分
                pixels[i, j] = fill_color
    qr_img.save('colored_qrcode.png')


if __name__ == "__main__":
    # 要编码的数据
    data = "https://example.com"
    # 生成彩色二维码，这里设置填充颜色为绿色，背景颜色为白色
    generate_colored_qr_code(data, fill_color=(0, 255, 0), back_color=(255, 255, 255))
