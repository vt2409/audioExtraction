import ffmpeg

class AudioExtract:
    @staticmethod
    def audio_extraction(input_path, output_path):
        try:
            # Convert video to audio using FFmpeg and overwrite if the file exists
            ffmpeg.input(input_path).output(output_path).overwrite_output().run(capture_stdout=True, capture_stderr=True)

            # Convert video to audio using FFmpeg but doesn't overwrite if the file exists and got failed
            # ffmpeg.input(input_path).output(output_path).run(capture_stdout=True, capture_stderr=True)
            
            print(f"✅ Audio extracted successfully: {output_path}")
            return True
        except Exception as error:
            print(f"❌ Exception Occurred: {error}")
            return False

# Creating an object of the class
obj = AudioExtract()

# File paths
input_video_path = "../documents/sample_video.mp4"
output_audio_path = "../documents/sample_video.mp3"

print(f"🎯 Output File Path: {output_audio_path}")

# Extract audio
success = obj.audio_extraction(input_video_path, output_audio_path)

print(f"✅ Extraction Successful: {success}")




