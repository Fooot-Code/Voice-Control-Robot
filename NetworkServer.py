# import required libraries
import speech_recognition as sr

class NetworkPublisher:
    def __init__(self, table):
        self.table = table

    def publish_to_network(self, distance):
        if distance == "ten":
            distance = 10.0
        self.table.putNumber("Forward Distance", distance)