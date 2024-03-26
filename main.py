import speech_recognition as sr
import VoiceServer
import networktables

nt = networktables.NetworkTablesInstance.getDefault()
nt.startClient("127.0.0.1")
table = nt.getTable("Mic Information")

micDevice = sr.Microphone(device_index=2) # device number of mic
r = sr.Recognizer()

mic = VoiceServer.Microphone(micDevice, r) # class instance of the mic
ntworkTable = VoiceServer.NetworkPublisher(table)

commandCount = 2

if __name__ == "__main__":
    for command in range(commandCount):
        #ntworkTable.publish_to_network(mic.get_words_from_audio())
        while True:
            ntworkTable.publish_to_network(10)