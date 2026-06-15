from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Hàm xử lý gọi API để rút gọn link
def shorten_url(long_url):
    # Sử dụng API miễn phí, không cần đăng ký tài khoản của TinyURL
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            return response.text  # Trả về đường link đã rút gọn
        else:
            return "Lỗi: Không thể kết nối tới server rút gọn."
    except Exception as e:
        return f"Lỗi kết nối: {str(e)}"

# Trang chủ của ứng dụng web
@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    original_url = None
    error_message = None

    # Khi người dùng nhấn nút "Rút gọn" (gửi dữ liệu POST lên)
    if request.method == "POST":
        original_url = request.form.get("url_input").strip()

        if original_url:
            # Gọi hàm rút gọn link ở trên
            result = shorten_url(original_url)
            if "Lỗi" in result:
                error_message = result
            else:
                short_url = result
        else:
            error_message = "Vui lòng không để trống đường link!"

    # Trả về giao diện kèm theo các kết quả (nếu có)
    return render_template("index.html", short_url=short_url, original_url=original_url, error=error_message)

if __name__ == "__main__":
    # Chạy ứng dụng web ở chế độ Debug để dễ sửa lỗi
    app.run(debug=True)
