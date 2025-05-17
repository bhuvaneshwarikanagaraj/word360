import subprocess
import os

def encode_video_for_mobile(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    # FFmpeg encoding command
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf", "scale=480:360",  # Lower resolution for low-end devices
        "-c:v", "libx264",
        "-profile:v", "baseline",  # Ensures compatibility with old Android phones
        "-level", "3.0",           # Conservative level for base-level devices
        "-preset", "slow",         # Better compression
        "-b:v", "500k",            # Moderate bitrate for mobile
        "-maxrate", "600k",
        "-bufsize", "1000k",
        "-c:a", "aac",
        "-b:a", "64k",             # Low-bitrate mono audio
        "-ac", "1",                # Mono audio
        "-ar", "44100",            # Standard sample rate
        "-movflags", "+faststart", # Fast start for streaming
        output_path
    ]

    try:
        print("🎬 Encoding started...")
        subprocess.run(command, check=True)
        print(f"✅ Encoding complete: {output_path}")
    except subprocess.CalledProcessError as e:
        print("❌ Encoding failed:", e)

if __name__ == "__main__":
    input_file = "video4.mp4" # Replace with your video
    output_file = "video44.mp4"  # Output file
    encode_video_for_mobile(input_file, output_file)