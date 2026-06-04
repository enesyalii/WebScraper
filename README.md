# 🚀 Auto YouTube Downloader (GUI)

**Auto YouTube Downloader** is a high-performance, user-friendly Graphical User Interface (GUI) for downloading YouTube videos with ease. Built with Python and powered by the industry-standard `yt-dlp` engine, this tool is optimized for speed, simplicity, and cross-platform compatibility.

## ✨ Key Features

-   **High-Speed Downloads**: Utilizes multi-threaded concurrent fragment downloading (up to 10 simultaneous connections) for maximum bandwidth utilization.
-   **Asynchronous GUI**: Designed with Python's `threading` module to ensure the interface remains responsive and never "Freezes" during a download.
-   **Custom Save Locations**: Includes a built-in directory browser to choose exactly where your media is saved.
-   **Auto-Reveal**: Automatically opens your system's file explorer (Windows Explorer, macOS Finder, or Linux XDG) exactly where the file was downloaded once finished.
-   **Smart Buffer Management**: Optimized 16K buffer sizes and disabled filesystem `mtime` modification to ensure the fastest possible disk write speeds.
-   **Cross-Platform Support**: Seamlessly runs on Windows, macOS, and Linux with native icon support.
-   **No Bloat**: No ads, no subscriptions, and zero tracking. Just open-source power.

## 📋 Requirements

While the package handles its own Python dependencies, for high-resolution video merging (e.g., 4K) and optimal performance, it is highly recommended to have **FFmpeg** installed on your system.

-   **Windows**: Install via Chocolatey (`choco install ffmpeg`) or download from the official site.
-   **macOS**: `brew install ffmpeg`
-   **Linux**: `sudo apt install ffmpeg`

## Installation

```bash
pip install autoytdownload
```
## Usage
Run `auto-yt-dl` in your terminal
## Website

You can check out the website here ==> autoytdownload.enesyali.site

## Support this project

You can donate and support to the project via my Ko-Fi page.