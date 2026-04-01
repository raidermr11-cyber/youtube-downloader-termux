import os
import subprocess

def main():
    print("🎵 YouTube Downloader (yt-dlp) 🎥")
    print("=====================================")
    
    # লিংক নেওয়া
    url = input("\nYouTube ভিডিও/প্লেলিস্টের লিংক দাও: ").strip()
    if not url:
        print("❌ লিংক দিতে হবে!")
        return
    
    # অডিও নাকি ভিডিও
    print("\nকী ডাউনলোড করতে চাও?")
    print("1. শুধু অডিও (MP3)")
    print("2. ভিডিও (সর্বোচ্চ কোয়ালিটি)")
    choice = input("অপশন সিলেক্ট করো (1 বা 2): ").strip()
    
    if choice == "1":
        # অডিও কোয়ালিটি অপশন
        print("\nঅডিও কোয়ালিটি সিলেক্ট করো:")
        print("1. Best (সর্বোচ্চ কোয়ালিটি - সুপারিশকৃত)")
        print("2. High")
        print("3. Medium")
        print("4. Low (ছোট ফাইল)")
        
        q_choice = input("অপশন (1-4): ").strip()
        
        if q_choice == "1":
            quality = "0"   # best
        elif q_choice == "2":
            quality = "2"
        elif q_choice == "3":
            quality = "5"
        elif q_choice == "4":
            quality = "8"
        else:
            quality = "0"
            print("ডিফল্ট Best কোয়ালিটি নেওয়া হচ্ছে...")
        
        # অডিও ডাউনলোড কমান্ড
        cmd = [
            "yt-dlp", "-x", "--audio-format", "mp3",
            "--audio-quality", quality,
            "--embed-thumbnail",  # কভার ইমেজ সহ
            "--output", "%(title)s.%(ext)s",
            url
        ]
        print("\n⏳ অডিও ডাউনলোড শুরু হচ্ছে... (Best MP3)")
        
    elif choice == "2":
        # ভিডিও ডাউনলোড (সর্বোচ্চ কোয়ালিটি)
        cmd = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",
            "--merge-output-format", "mp4",
            "--output", "%(title)s.%(ext)s",
            url
        ]
        print("\n⏳ ভিডিও ডাউনলোড শুরু হচ্ছে... (সর্বোচ্চ কোয়ালিটি)")
    
    else:
        print("❌ ভুল অপশন! প্রোগ্রাম বন্ধ করা হচ্ছে।")
        return
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✅ ডাউনলোড সম্পূর্ণ! ফাইলটি Downloads ফোল্ডারে পাবে।")
    except Exception as e:
        print(f"\n❌ কিছু সমস্যা হয়েছে: {e}")
        print("yt-dlp আপডেট করো: pip install -U yt-dlp")

if __name__ == "__main__":
    main()
