import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont
import imageio
import tempfile
from io import StringIO

class TerminalRecorder:
    def __init__(self, width=38, height=22, font_size=24, bg_color="navy", text_color="white"):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.frames = []
        self.temp_dir = tempfile.mkdtemp()
        print(f"Temporary directory: {self.temp_dir}", file=sys.stdout)

        # Try to load a monospace font
        try:
            self.font = ImageFont.truetype("Andale Mono.ttf", font_size)
        except:
            # Fallback to default font
            print("unable to load TTF, using default font", file=sys.stderr)
            self.font = ImageFont.load_default()
        
        # Calculate image dimensions based on font size
        sample_text = "W"
        sample_size = self.font.getbbox(sample_text)
        _, _, self.char_width, self.char_height = sample_size

        self.image_width = self.char_width * width
        self.image_height = self.char_height * height
        # captability with mp4 output
        self.image_height += (16 - (self.image_height % 16)) % 16
        self.image_width += (16 - (self.image_width % 16)) % 16

    def create_frame(self, text):
        """Create an image from text content"""
        # Create new image with background
        image = Image.new('RGB', (self.image_width, self.image_height), self.bg_color)
        draw = ImageDraw.Draw(image)
        
        # Split text into lines
        lines = text.split('\n')
        
        # Draw each line
        y = 0
        for line in lines[:self.height]:  # Limit to terminal height
            draw.text((0, y), line[:self.width], font=self.font, fill=self.text_color)
            y += self.char_height
            
        return image

    def capture_frame(self, text):
        """Capture a frame and store it"""
        frame = self.create_frame(text)
        frame_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        frame.save(frame_path)
        self.frames.append(frame_path)
        if len(self.frames) % 1000 == 0:
            print(f"Captured {len(self.frames)} frames", file=sys.stdout)

    def save_gif(self, output_path, duration=1):
        """Combine all frames into a GIF"""
        print(f"Saving GIF ({len(self.frames)} frames) to {output_path}", file=sys.stdout)
        images = []
        for frame_path in self.frames:
            images.append(imageio.v2.imread(frame_path))
        
        imageio.mimsave(output_path, images, duration=duration)
        # Cleanup temporary files
        print(f"Cleaning up temporary directory: {self.temp_dir}", file=sys.stdout)
        for frame_path in self.frames:
            os.remove(frame_path)
        os.rmdir(self.temp_dir)

        print(f"Done", file=sys.stdout)

    def save_mp4(self, output_path, duration=1):
        """Combine all frames into a GIF"""
        print(f"Saving Mp4 ({len(self.frames)} frames) to {output_path}", file=sys.stdout)

        writer = imageio.get_writer(output_path, fps=20)
        for frame_path in self.frames:
            writer.append_data(imageio.v2.imread(frame_path))
        writer.close()

        # Cleanup temporary files
        print(f"Cleaning up temporary directory: {self.temp_dir}", file=sys.stdout)
        for frame_path in self.frames:
            os.remove(frame_path)
        os.rmdir(self.temp_dir)

        print(f"Done", file=sys.stdout)

# Example usage
def demo():
    # Create recorder instance
    recorder = TerminalRecorder()
    
    # Generate some example frames
    for i in range(5):
        # Create some example terminal output
        output = f"Frame {i + 1}\n"
        output += "=" * 20 + "\n"
        output += f"Counter: {i}\n"
        output += f"Time: {time.strftime('%H:%M:%S')}\n"
        
        # Capture the frame
        recorder.capture_frame(output)
        
    # Save the final GIF
    recorder.save_gif("terminal_output.gif", duration=100.0)

if __name__ == "__main__":
    demo()