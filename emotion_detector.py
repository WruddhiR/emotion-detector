import unittest
from emotion_detection.emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_anger(self):
        text = "I am so angry!"
        result = emotion_predictor(text)
        self.assertGreater(result['anger'], 0)

    def test_joy(self):
        text = "I am so happy!"
        result = emotion_predictor(text)
        self.assertGreater(result['joy'], 0)

if __name__ == '__main__':
    unittest.main()

