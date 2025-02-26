import cv2
import textwrap
import numpy as np
import moviepy.editor as mp

# Load video
cap = cv2.VideoCapture("minecraft-parkour-gameplay-no-copyright-1080-000-6083_RcxOCXlV.mp4")

# Video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Load story text
with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

# Wrap text to fit within video width
wrapped_text = textwrap.wrap(story, width=20)  # Adjust width for larger font
total_lines = len(wrapped_text)

# Calculate total frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

frame_count = 0
max_lines_visible = 5  # Limit to 5 lines

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Determine how many lines to display based on video progress
    max_lines_to_display = min((frame_count * total_lines) // total_frames, total_lines)

    # Keep only the last 5 lines
    start_line = max(0, max_lines_to_display - max_lines_visible)
    current_lines = wrapped_text[start_line:max_lines_to_display]

    # Define fixed white background box properties
    box_width = int(width * 0.8)  # 80% of video width
    box_height = int(height * 0.4)  # 40% of video height (for larger text space)
    box_x = (width - box_width) // 2  # Center horizontally
    box_y = (height - box_height) // 2  # Center vertically

    # Add a white background rectangle for text
    overlay = frame.copy()
    cv2.rectangle(overlay, (box_x, box_y), (box_x + box_width, box_y + box_height), (255, 255, 255), -1)
    alpha = 0.7  # Transparency level
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5  # Increased font size
    color = (0, 0, 0)  # Black text for contrast
    thickness = 4  # Thicker font

    # Calculate the **centered Y position** for text
    text_line_height = 60  # Increased height of each text line
    total_text_height = len(current_lines) * text_line_height
    start_y = box_y + (box_height - total_text_height) // 2  # Center text vertically in box

    # Display text **centered horizontally and vertically**
    for i, line in enumerate(current_lines):
        text_size = cv2.getTextSize(line, font, font_scale, thickness)[0]
        text_x = box_x + (box_width - text_size[0]) // 2  # Center text horizontally
        text_y = start_y + i * text_line_height + text_size[1]  # Adjust baseline for each line
        cv2.putText(frame, line, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)

    out.write(frame)
    frame_count += 1

cap.release()
out.release()
cv2.destroyAllWindows()
