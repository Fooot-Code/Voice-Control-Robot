# import required libraries
import speech_recognition as sr


class Microphone:
    def __init__(self, recognizer, mic) -> None:
        self.recognizer = recognizer
        self.mic = mic

    def get_audio_from_mic(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)
            return audio
        
    def get_words_from_audio(self):
        self.recognizer.recognize_sphinx(self.get_audio_from_mic())

class NetworkPublisher:
    def __init__(self, table):
        self.table = table

    def publish_to_network(self, distance):
        self.table.putValue("Forward Distance", distance)