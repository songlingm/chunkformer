 # 🗣️ Live Speech-to-Text Offline using Chunkformer and Pvrecorder

 Đây là bản fork sử dụng [`pvrecorder`](https://github.com/Picovoice/pvrecorder) để ghi âm giọng nói thành file `.wav` sau đó chuyển đổi thành văn bản tiếng Việt bằng mô hình [`chunkformer-large-vie`](https://huggingface.co/khanhld/chunkformer-large-vie).


 ---

 ## 📁 Nguồn tham khảo

 * **Mô hình Chunkformer**
   * Tác giả: [Khanhld](https://github.com/khanld/chunkformer)
   * Mã nguồn: [chunkformer](https://github.com/khanld/chunkformer)
   * Mô hình: [chunkformer-large-vie](https://huggingface.co/khanhld/chunkformer-large-vie)

 * **Thư viện ghi âm pvrecorder**
   * Trang chủ: [Picovoice.ai](https://picovoice.ai/)
   * Mã nguồn: [pvrecorder](https://github.com/Picovoice/pvrecorder)

 ---

 ## 🚀 Cài đặt & Triển khai

 ### ✅ Yêu cầu hệ thống

 * Hệ điều hành: Ubuntu hoặc các bản phân phối Linux **có sử dụng hệ quản lý gói `apt`** (ví dụ: Debian, Linux Mint, Pop!_OS, v.v.
 * Phiên bản Python: **Python 3.10 hoặc cao hơn**

 ---

 ### 🔧 Các bước triển khai

 1. **Clone repository (đã fork):**
    ```bash
    git clone https://github.com/songlingm/chunkformer.git
    cd chunkformer
    ```

 2. **Cập nhật hệ thống & cài đặt dependencies:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install ffmpeg python3-pip python3.10-venv -y
    ```

 3. **(Optional) Tạo và kích hoạt môi trường ảo:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

 4. **Cài đặt các thư viện cần thiết:**
    ```bash
    sudo pip install -r requirements.txt
    ```

 5. **Tải checkpoint mô hình từ Hugging Face:**
    ```bash
    huggingface-cli download khanhld/chunkformer-large-vie --local-dir "./chunkformer-large-vie"
    ```

 6. **Xác định và chỉnh `index` micro:**
    ```bash
    python3 list_devices.py  # Kiểm tra index của micro
    ```

    ➡️ Sau đó sửa `index` và `duration` trong `streaming_transcribe.py` theo nhu cầu. Mặc định duration = 5 (file .wav sẽ có thời lượng là 5s)

 7. **Chạy chương trình chuyển đổi giọng nói sang văn bản:**
    ```bash
    python3 streaming_transcribe.py
    ```

    > ⚠️ Nếu gặp lỗi khi ghi âm hoặc không thấy text, hãy kiểm tra lại `index` của micro cho đúng với thiết bị ghi âm của bạn.

 ---

 ## 📌 Ghi chú

 * `pvrecorder` đôi khi yêu cầu quyền truy cập thiết bị ghi âm — hãy đảm bảo thiết bị của bạn đã được cấp quyền.
 * Mô hình hoạt động **offline** hoàn toàn sau khi đã tải về checkpoint.
 * Trong khi chương trình chạy, có thể nói liên tục mà không cần quan tâm đến độ dài của từng đoạn audio wav chia nhỏ.

 ---





<a name = "citation" ></a>
## Citation

```bibtex
@INPROCEEDINGS{10888640,
  author={Le, Khanh and Ho, Tuan Vu and Tran, Dung and Chau, Duc Thanh},
  booktitle={ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={ChunkFormer: Masked Chunking Conformer For Long-Form Speech Transcription}, 
  year={2025},
  volume={},
  number={},
  pages={1-5},
  keywords={Scalability;Memory management;Graphics processing units;Signal processing;Performance gain;Hardware;Resource management;Speech processing;Standards;Context modeling;chunkformer;masked batch;long-form transcription},
  doi={10.1109/ICASSP49660.2025.10888640}}

```
---
## 📬 Contact
- 📧 Email: lampt.b19vt216@stu.ptit.edu.vn
