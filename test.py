import unittest
from unittest.mock import patch
from mp3_cutaudio import download_audio, cut_intro, cut_middle, cut_end
import os
import shutil
from time import sleep





    @patch('mp3_cutaudio.YouTube')
    def test_download_audio_success(self, mock_youtube):
        mock_stream = mock_youtube.return_value.streams.filter.return_value.first.return_value
        mock_stream.download.return_value = None
        url = 'mocked_url'
        download_audio(url)
        mock_youtube.assert_called_once_with(url)
        mock_stream.download.assert_called_once_with(filename='audio.mp3')
    
    @patch('mp3_cutaudio.YouTube')
    def test_download_audio_failure(self, mock_youtube):
        mock_youtube.side_effect = Exception("Mocked Exception")
        url = 'mocked_url'
        with unittest.mock.patch('builtins.print') as mocked_print:
            download_audio(url)
            mocked_print.assert_called_once()
            call_args = mocked_print.call_args[0]
            self.assertTrue("No such thang..." in call_args[0] and "Mocked Exception" in str(call_args[1]))


class TestAudioCutting(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory to store audio files
        self.temp_dir = "temp_audio"
        os.makedirs(self.temp_dir, exist_ok=True)

        # Copy the original audio file to the temporary directory
        self.original_audio_path = "audio.mp3"
        self.temp_original_audio_path = os.path.join(self.temp_dir, "audio.mp3")
        shutil.copy(self.original_audio_path, self.temp_original_audio_path)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_cut_intro(self):
        # Test cutting the intro
        start_time = "00:30"  # Assuming intro starts at 30 seconds
        cut_intro(self.temp_original_audio_path, start_time)
        self.intro_cut_audio_path = os.path.join(self.temp_dir, "audio_intro_removed.mp3")
        # Add assertions to check if intro was cut correctly

    def test_cut_middle(self):
        # Test cutting the middle
        start_time = "01:00"  # Assuming middle starts at 1 minute
        end_time = "02:00"  # Assuming middle ends at 2 minutes
        cut_middle(self.temp_original_audio_path, start_time, end_time)
        self.middle_cut_audio_path = os.path.join(self.temp_dir, "audio_middle_removed.mp3")
        # Add assertions to check if middle was cut correctly

    def test_cut_end(self):
        # Test cutting the end
        end_time = "03:00"  # Assuming end is at 3 minutes
        cut_end(self.temp_original_audio_path, end_time)
        self.end_cut_audio_path = os.path.join(self.temp_dir, "audio_end_removed.mp3")
        # Add assertions to check if end was cut correctly


if __name__ == "__main__":
    unittest.main()
    