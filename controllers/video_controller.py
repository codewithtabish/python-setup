from flask import request, jsonify,send_file
import yt_dlp
import os
from config import queue  # Import the queue from config
from time import time
from config import Queue

# Task to download the video in the background


def download_video_task(video_url, format_id):
    try:
        # Parse video URL and format ID from the request JSON
        
        # Directory for storing downloaded videos
        download_dir = r"C:\Users\Mark 1\Downloads"
        os.makedirs(download_dir, exist_ok=True)
        
        # yt-dlp options for downloading
        ydl_opts = {
            'quiet': True,  # Suppress logs
            'noplaylist': True,  # Ensure only the video is processed
            'format': format_id,  # Specify the format to download
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Output template
            'merge_output_format': 'mp4',  # Ensure the video and audio are merged into MP4 format
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            info = ydl.extract_info(video_url)
            video_file = ydl.prepare_filename(info)
        
        # Send the downloaded file as a response
        return send_file(video_file, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400




def get_formats():
    try:
        # Parse the video URL from the request JSON
        data = request.get_json()
        video_url = data.get('url')
        
        # yt-dlp options
        ydl_opts = {
            'quiet': True,  # Suppress logs
            'noplaylist': True,  # Ensure only the video is processed
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info without downloading
            info = ydl.extract_info(video_url, download=False)
            
            # Filter for all MP4 formats with unique resolutions
            unique_formats = []
            seen_resolutions = set()
            
            for fmt in info.get("formats", []):
                if fmt.get("ext") == "mp4":  # Only MP4 formats
                    resolution = f"{fmt.get('height', 'Audio Only')}p"
                    if resolution not in seen_resolutions:  # Avoid duplicates
                        unique_formats.append({
                            "format_id": fmt.get("format_id"),
                            "resolution": resolution,
                            "type": fmt.get("ext"),
                        })
                        seen_resolutions.add(resolution)  # Mark resolution as seen
        
        # Return unique MP4 formats and video title
        return jsonify({"formats": unique_formats, "title": info.get("title")})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to initiate video download and queue it
def download_video():
    try:
        # Parse the incoming request data
        data = request.get_json()
        video_url = data.get('url')
        format_id = data.get('format_id')

        if not video_url or not format_id:
            return jsonify({"error": "Both 'url' and 'format_id' are required"}), 400

        # Enqueue the job to the Redis queue for background processing
        job = queue.enqueue(download_video_task, video_url, format_id)
        
        return jsonify({"message": "Download started", "job_id": job.get_id()}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Endpoint to check the status of the download job
def get_job_status():
    try:
        job_id = request.args.get('job_id')
        job = queue.fetch_job(job_id)
        
        if job is None:
            return jsonify({"error": "Job not found"}), 404
        
        if job.is_finished:
            return jsonify({"status": "finished", "file": job.result}), 200
        elif job.is_failed:
            return jsonify({"status": "failed", "error": job.exc_info}), 500
        else:
            return jsonify({"status": "in progress"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
