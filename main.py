import speech_recognition as sr
import NetworkServer
import networktables

nt = networktables.NetworkTablesInstance.getDefault()
nt.startClient("127.0.0.1")
table = nt.getTable("Mic Information")

#print(sr.Microphone.list_microphone_names())

micDevice = sr.Microphone(device_index=1) # device number of mic
r = sr.Recognizer()
ntworkTable = NetworkServer.NetworkPublisher(table)

commandCount = 2

if __name__ == "__main__":
    for command in range(commandCount):
        while True:
            with micDevice as source:
                audio = r.listen(source, phrase_time_limit=2)
            
            print(r.recognize_sphinx(audio))

            ntworkTable.publish_to_network(r.recognize_sphinx(audio))