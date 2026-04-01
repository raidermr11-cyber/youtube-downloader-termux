# youtube-downloader-termux
YouTube Audio/Video Downloader using yt-dlp for Termux
# 🎥 YouTube Downloader for Termux

একটি সহজ Python প্রোগ্রাম যা **Termux** এ YouTube থেকে অডিও (MP3) এবং ভিডিও (MP4) ডাউনলোড করতে সাহায্য করে।

`yt-dlp` টুল ব্যবহার করে তৈরি।

## ✨ ফিচারসমূহ

- শুধু অডিও ডাউনলোড (MP3 ফরম্যাট)
- ভিডিও ডাউনলোড (সর্বোচ্চ কোয়ালিটি MP4)
- অডিওতে ৪টি কোয়ালিটি অপশন (Best, High, Medium, Low)
- MP3-এ থাম্বনেইল (কভার ইমেজ) যোগ করা
- প্লেলিস্ট সাপোর্ট
- সহজ ইউজার ইন্টারফেস

## 📥 ইনস্টলেশন

Termux ওপেন করে নিচের কমান্ডগুলো চালান:

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install python ffmpeg -y
pip install -U yt-dlp
git clone https://github.com/raidermr11-cyber/youtube-downloader-termux.git
cd youtube-downloader-termux
