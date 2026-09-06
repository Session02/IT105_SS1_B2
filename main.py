def classify_logistics_feature(feature_name):
    """
    Tự động kiểm tra và phân loại tính năng phần mềm Logistics
    vào đúng 3 nhóm HTTT: TPS, MIS hoặc DSS dựa trên từ khóa ngữ nghĩa.
    """
    text = feature_name.lower()
    
    tps_keywords = ["bấm", "quét", "mã vạch", "in phiếu", "nhập kho", "lấy hàng", "giao hàng", "thu tiền"]
    dss_keywords = ["dự báo", "mô hình", "phân tích điểm nóng", "chiến lược", "đề xuất mở", "mô phỏng"]
    mis_keywords = ["báo cáo", "tổng hợp", "thống kê", "định kỳ", "bảng biểu"]

    if any(keyword in text for keyword in dss_keywords):
        system_type = "DSS (Hỗ trợ quyết định)"
        user_role = "Ban Giám đốc / Giám đốc Chiến lược"
    elif any(keyword in text for keyword in mis_keywords):
        system_type = "MIS (Thông tin quản lý)"
        user_role = "Quản lý bưu cục / Trưởng vùng"
    elif any(keyword in text for keyword in tps_keywords):
        system_type = "TPS (Xử lý giao dịch tác nghiệp)"
        user_role = "Nhân viên kho / Tài xế / Thu ngân bưu cục"
    else:
        system_type = "UNKNOWN (Chưa xác định)"
        user_role = "Cần BA kiểm tra lại mô tả tính năng"

    return system_type, user_role


test_features = [
    "Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục",
    "Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết",
    "Tài xế bấm nút 'Đã lấy hàng' trên App Mobile",
    "Nhân viên kho quét mã vạch nhập kho",
    "In phiếu cước giao hàng cho khách tại bưu cục"
]

print("=== KẾT QUẢ TỰ ĐỘNG PHÂN LOẠI TÍNH NĂNG HTTT ===")
for feature in test_features:
    sys_type, role = classify_logistics_feature(feature)
    print(f"• Tính năng  : {feature}")
    print(f"  -> Phân loại : {sys_type}")
    print(f"  -> Người dùng: {role}\n")