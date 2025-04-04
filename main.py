from audio_processor import download_audio
from text_processor import transcribe_audio, summarize_text
import time
import os
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

def validate_url(url):
    if not any(domain in url for domain in ['youtube.com', 'youtu.be']):
        raise ValueError("Invalid YouTube URL")
    if 'list=' in url:
        raise ValueError("Playlist URLs not supported")
    return True

def save_full_transcript(transcript, url, timestamp):
    """Save complete unmodified transcript"""
    os.makedirs("outputs/transcripts", exist_ok=True)
    filename = f"full_transcript_{timestamp}.txt"
    filepath = os.path.join("outputs", "transcripts", filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Full Transcript ({timestamp})\n")
        f.write(f"Source: {url}\n")
        f.write(f"Total Words: {len(transcript.split())}\n\n")
        f.write(transcript)
    
    print(f"✓ Full transcript saved to: {os.path.abspath(filepath)}")
    return filepath

def main():
    try:
        url = input("Enter YouTube URL: ").strip()
        validate_url(url)
        
        print("\nStep 1/3: Downloading audio...")
        start_time = time.time()
        audio_path = download_audio(url)
        print(f"✓ Completed in {time.time() - start_time:.1f}s")
        
        print("\nStep 2/3: Transcribing audio...")
        start_time = time.time()
        transcript = transcribe_audio(audio_path)
        transcribe_time = time.time() - start_time
        print(f"✓ Completed in {transcribe_time:.1f}s")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        total_words = len(transcript.split())
        print(f"Total words transcribed: {total_words}")
        
        # Save complete transcript
        transcript_path = save_full_transcript(transcript, url, timestamp)
        
        print("\nStep 3/3: Generating summary...")
        start_time = time.time()
        summary = summarize_text(transcript)
        print(f"✓ Completed in {time.time() - start_time:.1f}s")
        
        # Save summary
        os.makedirs("outputs/summaries", exist_ok=True)
        summary_path = f"outputs/summaries/summary_{timestamp}.txt"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"Video Summary ({timestamp})\n")
            f.write(f"Source: {url}\n")
            f.write(f"Original Words: {total_words}\n")
            f.write(f"Summary Length: {len(summary.split())} words\n\n")
            f.write(summary)
            
        print(f"\n✅ Final summary saved to: {os.path.abspath(summary_path)}")
        print(f"\n📄 Full transcript available at: {os.path.abspath(transcript_path)}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Troubleshooting:")
        print("- Try a different video URL")
        print("- Check video has audible dialogue")
        print("- Ensure stable internet connection")

if __name__ == "__main__":
    main()
