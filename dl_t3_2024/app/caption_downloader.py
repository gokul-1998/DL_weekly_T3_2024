from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys
import re

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    # Regex pattern to extract video ID
    pattern = r"(?<=v=)[\w-]+|(?<=youtu.be/)[\w-]+"
    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        return None

# Function to get YouTube video title
def get_video_title(video_id):
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    return yt.title

# Function to fetch the transcript
def fetch_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

# Function to create a PDF with paragraphs for each minute on new pages
def create_pdf(transcript, title):
    filename = f"{title}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    text_start_y = height - 40  # Start Y position for text
    line_height = 14  # Height of each line including spacing

    current_minute = None  # To keep track of current minute

    for entry in transcript:
        start = entry['start']
        text = entry['text']

        # Calculate the minute (rounded up)
        minute = int(start // 60) + 1

        # Check if we are starting a new minute
        if minute != current_minute:
            current_minute = minute
            if current_minute != 1:
                c.showPage()  # Start a new page for each new minute
            c.setFont("Helvetica-Bold", 14)
            c.drawString(40, text_start_y, f"Minute {current_minute}")
            current_y = text_start_y - (line_height * 2)  # Space after header

        # Set font back to normal for content
        c.setFont("Times-Roman", 12)

        # Split text into paragraphs
        paragraphs = text.split('\n\n')
        for paragraph in paragraphs:
            lines = paragraph.split('\n')
            for line in lines:
                if current_y < 40:  # Check if there's enough space for another line
                    c.showPage()  # If not, create a new page
                    current_y = text_start_y  # Reset Y position for new page
                c.drawString(40, current_y, line)  # Draw the line of text
                current_y -= line_height  # Move Y position down for next line

    c.save()
    print(f"PDF saved as {filename}")

# Main function to get the transcript and generate PDF
def main(video_url):
    video_id = extract_video_id(video_url)
    if video_id:
        title = get_video_title(video_id)
        transcript = fetch_transcript(video_id)
        create_pdf(transcript, title)
    else:
        print("Invalid YouTube URL provided.")

if __name__ == "__main__":
        video_url = input("Enter the YouTube video URL: ")
        main(video_url)