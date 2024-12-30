# Video-Enhancement-with-CodeFormer

This project provides a Python script to enhance the quality of input videos using CodeFormer, a robust face restoration algorithm. The script processes an input video by extracting frames, enhancing them, and reassembling the frames into an output video with improved visual quality.
Features

    Frame Extraction: Decomposes the input video into individual frames.
    Frame Enhancement: Enhances each frame using CodeFormer with Real-ESRGAN for background upsampling.
    Video Reconstruction: Reassembles the enhanced frames into a video.
    Audio Preservation: Extracts and reattaches the original audio to the enhanced video.

Prerequisites

Ensure you have the following installed:

    Python 3.7 or higher
    FFmpeg
    Required Python packages (listed in requirements.txt)

Installation

    Clone the Repository:

git clone https://github.com/sczhou/CodeFormer.git
cd CodeFormer

Install Dependencies:

pip install -r requirements.txt
python basicsr/setup.py develop

Download Pre-trained Models:

    python scripts/download_pretrained_models.py facelib
    python scripts/download_pretrained_models.py CodeFormer

Usage

    Prepare Your Input Video:

    Place your input video (e.g., input.mp4) in the movie directory.

    Run the Enhancement Script:

    Execute the following command:

python enhance_video.py --input input.mp4 --output output.mp4 --w 0.9

             --input: Path to the input video file.
             --output: Desired path for the output video file.
             --w: Balance between quality and fidelity (range: 0.1 to 0.9).

Script Details

The enhance_video.py script performs the following steps:

    1.Setup: Imports necessary libraries and sets up directories.
    2.Frame Extraction: Uses FFmpeg to extract frames from the input video.
    3.Frame Enhancement: Enhances each frame using CodeFormer with Real-ESRGAN for background upsampling.
    4.Video Reconstruction: Reassembles the enhanced frames into a video using FFmpeg.
    5.Audio Preservation: Extracts the original audio from the input video and merges it with the enhanced video.

Example

Here's how to enhance a video named input.mp4:

    Place input.mp4 in the movie directory.

    Run the script:

python enhance_video.py --input movie/input.mp4 --output movie/output.mp4 --w 0.9

Find the enhanced video at movie/output.mp4.
