import subprocess

def ten_wifi_dang_dung():
    try:
        connected_wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('latin-1').split('\n')
        for line in connected_wifi_info:
            if "SSID" in line:
                connected_wifi_name = line.split(":")[1].strip()
                return connected_wifi_name
        return "Khong tim thay wifi nao ca! "
    except Exception as e:
        return str(e)

def lay_mat_khau_wifi(ten_wifi):
    try:
        command = f"netsh wlan show profile name=\"{ten_wifi}\" key=clear"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL).decode('utf-8')
        password_line = [line.strip() for line in output.split('\n') if "Key Content" in line][0]
        password = password_line.split(":")[1].strip()
        return password
    except Exception as e:
        return str(e)

# Lấy tên wifi đang kết nối
connecting_wifi = ten_wifi_dang_dung()

# Hiển thị tên wifi đang kết nối
print("Ten Wifi Dang Ket Noi:", connecting_wifi)

# Lấy mật khẩu của wifi đó
mat_khau = lay_mat_khau_wifi(connecting_wifi)
print("Mat Khau:", mat_khau)