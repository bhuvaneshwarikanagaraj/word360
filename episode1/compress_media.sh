#!/bin/bash

# Create backup directories
mkdir -p episode1/images/original
mkdir -p episode1/video/original

# Backup original images
echo "Backing up original images..."
cp episode1/images/*.jpg episode1/images/original/
cp episode1/*.jpg episode1/images/original/

# Backup original videos
echo "Backing up original videos..."
cp episode1/video/*.mp4 episode1/video/original/
cp episode1/*.mp4 episode1/video/original/

# Compress JPG images
echo "Compressing JPG images..."
find episode1 -name "*.jpg" -not -path "*/original/*" -exec convert {} -strip -quality 85 -resize '1024x1024>' {} \;

# Compress MP4 videos
echo "Compressing MP4 videos..."
find episode1 -name "*.mp4" -not -path "*/original/*" -exec ffmpeg -i {} -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k {}.compressed.mp4 \; -exec mv {}.compressed.mp4 {} \;

# Compress MP3 audio
echo "Compressing MP3 files..."
find episode1 -name "*.mp3" -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 4 {}.compressed.mp3 \; -exec mv {}.compressed.mp3 {} \;

echo "Compression completed!"
echo "Original files are backed up in the 'original' directories." 