#!/usr/bin/env python3
"""Download YouTube video in max quality using yt-dlp."""

import sys
import subprocess


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python down.py <youtube_url>")
        return 2

    url = sys.argv[1]

    # Best video + best audio, merged to mp4 (or best if mp4 not possible)
    cmd = [
        "yt-dlp",
        "-f",
        "bv*+ba/best",
        "--merge-output-format",
        "mp4",
        "-o",
        "%(title)s.%(ext)s",
        url,
    ]

    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print("yt-dlp not found. Install with: pip install -U yt-dlp")
        print("Also ensure ffmpeg is installed and on PATH for merging.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())