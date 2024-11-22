import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_joy(self):
        statement = "I am glad this happened"
        expected_emotion = "joy"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_emotion)

    def test_emotion_detector_anger(self):
        statement = "I am really mad about this"
        expected_emotion = "anger"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_emotion)
    
    def test_emotion_detector_disgust(self):
        statement = "I feel disgusted just hearing about this"
        expected_emotion = "disgust"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_emotion)

    def test_emotion_detector_sadness(self):
        statement = "I am so sad about this"
        expected_emotion = "sadness"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_emotion)

    def test_emotion_detector_fear(self):
        statement = "I am really afraid that this will happen"
        expected_emotion = "fear"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()