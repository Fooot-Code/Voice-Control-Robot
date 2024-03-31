# import required libraries
import speech_recognition as sr

class NetworkPublisher:
    def __init__(self, table):
        self.table = table

    def publish_to_network(self, keyName, direction):
        self.table.putNumber(keyName, direction)
        