import pyshark


# Đường dẫn đến file .pcapng đã thu được bằng Wireshark
file_path = r'C:\study\bai_kiem_tra\Bài Kiểm Tra\Phạm Thị Thu Trang & Hoàng Sỹ Việt .pcapng'

# Tạo đối tượng đọc file gói tin
cap = pyshark.FileCapture(file_path, use_json=True, keep_packets=False)

# Duyệt qua từng gói tin trong file
for i, pkt in enumerate(cap):
    try:
        print(f"\n=== Gói {i+1} ===")

        # Tầng 2: Data Link Layer (Ethernet)
        if 'eth' in pkt:
            print("Tầng 2 - MAC nguồn (Source MAC):", pkt.eth.src)
            print("Tầng 2 - MAC đích (Destination MAC):", pkt.eth.dst)

        # Tầng 3: Network Layer (IP)
        if 'ip' in pkt:
            print("Tầng 3 - IP nguồn (Source IP):", pkt.ip.src)
            print("Tầng 3 - IP đích (Destination IP):", pkt.ip.dst)
            print("Tầng 3 - Giao thức:", pkt.ip.proto)

    except Exception as e:
        print(f"Lỗi tại gói #{i+1}: {e}")

    # Giới hạn số gói để xem (tùy chọn)
    if i >= 10:
        break
