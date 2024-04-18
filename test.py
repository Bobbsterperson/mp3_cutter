import unittest
from unittest.mock import patch
from mp3_cutaudio import download_audio, cut_intro, cut_middle, cut_end
import os



# ass = input("time: ")
# end_m = int(ass.split(':')[0]) * 60 * 1000
# end_s = int(ass.split(':')[1]) * 1000
# end_time_ms = end_m + end_s
# print(f"{end_time_ms}")

# time: 20:20
# 1220000

# time: 05:05
# 305000

# time: 5:5
# 305000

# time: 4:65
# 305000


class TestDownloadAudio(unittest.TestCase):

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


class testCutIntro(unittest.TestCase):
    
    def testcutintro(self):
        #arrange
        test_audio_file = "audio.mp3"
        start_time = "00:05"
        #act 
        cut_intro(test_audio_file, start_time)
        #assert
        output_file = f"{os.path.splitext(test_audio_file)[0]}_intro_removed.mp3"
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)


class testCutmiddle(unittest.TestCase):
    
    def testcutmiddle(self):
        #arrange
        test_audio_file = "audio.mp3"
        start_time = "00:05"
        end_time = "01:00"
        #act 
        cut_middle(test_audio_file, start_time, end_time)
        #assert
        output_file = f"{os.path.splitext(test_audio_file)[0]}_middle_removed.mp3"
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

class testCutend(unittest.TestCase):
    
    def testcutend(self):
        #arrange
        test_audio_file = "audio.mp3"
        end_time = "01:05"
        #act 
        cut_end(test_audio_file, end_time)
        #assert
        output_file = f"{os.path.splitext(test_audio_file)[0]}_end_removed.mp3"
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
    