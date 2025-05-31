# 🗣️ Speech-to-Text Offline with Chunkformer

@ Dự án sử dụng [`pvrecorder`](https://github.com/Picovoice/pvrecorder) để ghi âm giọng nói thành file `.wav` trong 5 giây, sau đó chuyển đổi thành văn bản tiếng Việt bằng mô hình [`chunkformer-large-vie`](https://huggingface.co/khanhld/chunkformer-large-vie).

@ > ⚠️ Lưu ý: Trước khi chạy mô hình, cần chỉnh đúng **index micro** trong file `record_and_transcribe.py`.

---

## 📁 Source

@ Khanhld (Chunkformer)  
@ Source code: https://github.com/khanld/chunkformer  
@ Model: https://huggingface.co/khanhld/chunkformer-large-vie  

@ Picovoice (pvrecorder)  
@ Homepage: https://picovoice.ai/  
@ Source code: https://github.com/Picovoice/pvrecorder  

---

## 🚀 Deploy

### ✅ For Ubuntu or apt-based Linux packages:

@ 1. Download the ChunkFormer Repository (forked)
```bash
@ git clone https://github.com/songlingm/chunkformer.git
@ cd chunkformer
@ sudo apt update && sudo apt upgrade -y
@ sudo apt install ffmpeg python3-pip python3.10-venv -y
@ python3 -m venv venv
@ source venv/bin/activate
@ sudo pip install -r requirements.txt
```

@ 2. Download the Model Checkpoint from Hugging Face
```bash
@ huggingface-cli download khanhld/chunkformer-large-vie --local-dir "./chunkformer-large-vie"
```

@ 3. Check index micro and replace duration and index on `record_and_transcribe.py`
```bash
@ python3 list_devices.py # lấy index của micro
```

@ 4. Run the model
```bash
@ python3 record_and_transcribe.py # Nếu lỗi record thì sửa đúng index cho pvrecorder
```

---

@ 📌 Ghi chú:
@ - `pvrecorder` có thể yêu cầu quyền truy cập vào thiết bị ghi âm — hãy đảm bảo thiết bị đã được cấp quyền.
@ - Mô hình hoạt động **offline** hoàn toàn sau khi đã tải về checkpoint từ Hugging Face.


<a name = "citation" ></a>
## Citation
If you use this work in your research, please cite:

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
