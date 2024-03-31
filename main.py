import speech_recognition as sr
import NetworkServer
import networktables

nt = networktables.NetworkTablesInstance.getDefault()
nt.startClient("127.0.0.1")
table = nt.getTable("Mic Information")

#print(sr.Microphone.list_microphone_names())

micDevice = sr.Microphone(device_index=1) # device number of mic
r = sr.Recognizer()
ntTable = NetworkServer.NetworkPublisher(table)

changeCount = 0

if __name__ == "__main__":
    while True:
        with micDevice as source:
            audio = r.listen(source, phrase_time_limit=2)
        
        directionBasedOnWord = r.recognize_sphinx(audio)

        print(directionBasedOnWord)

        if directionBasedOnWord == "forward":
            directionBasedOnWord = 1.0
            ntTable.publish_to_network("Forward Distance", directionBasedOnWord)
            changeCount += 1

        elif directionBasedOnWord == "backward":
            directionBasedOnWord = -1.0
            ntTable.publish_to_network("Forward Distance", directionBasedOnWord)
            changeCount += 1

        ntTable.publish_to_network("Times Direction Changed", changeCount)
        