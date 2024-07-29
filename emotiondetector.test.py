"""
Unit test module for the `emotiondetector` package
"""
import unittest
from emotiondetector.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Unit test class for emotion detector
    """
    def test_emotion_detector(self):
        """
        Test cases for emotion detector
        """
        joy_unit_test = emotion_detector("I am glad this happened")
        self.assertEqual(joy_unit_test["dominant_emotion"], "joy")

        anger_unit_test = emotion_detector("I am really mad about this")
        self.assertEqual(anger_unit_test["dominant_emotion"], "anger")

        disgust_unit_test = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_unit_test["dominant_emotion"], "disgust")

        sad_unit_test = emotion_detector("I am so sad about this")
        self.assertEqual(sad_unit_test["dominant_emotion"], "sadness")

        fear_unit_test = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_unit_test["dominant_emotion"], "fear")

unittest.main()
