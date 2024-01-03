from pydub import AudioSegment,silence
import csv


#Este es el header del CSV
header = ['Pareja', 'Guitarrista', 'Condicion', 'Silencio', 'Trial', 'DUR1', 'DUR2', 'DUR3', 'promedio']
data = []
#Se carga el array data de esta manera
#data = ['Pareja', 'Guitarrista', 'Condicion', 'Silencio', 'Trial', 'ONSET']

condicion = "S"
silencio = "SC"
#Abrimos el archivo y corremos los procesos, a medida que vamos cargando la data
with open('silencios_'+condicion+'_'+silencio+'.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    #Escribimos el header
    writer.writerow(header)

    total = 0
    for p in range(1,21):
        for t in range(1,4):   
            myaudio = AudioSegment.from_wav('audios2410/P'+str(p)+'_'+condicion+'_'+silencio+'_GTR1_00'+str(t)+'.wav')
    
            dBFS=myaudio.dBFS
    
            silenc = silence.detect_silence(myaudio, min_silence_len=500, silence_thresh=dBFS-16)

            silenc = [((start/1000),(stop/1000)) for start,stop in silenc] #in sec


            print(str(p)+"_"+ str(t))
            print(silenc[1][1] - silenc[1][0])
            print(silenc[2][1] - silenc[2][0])
            print(silenc[3][1] - silenc[3][0])
            print("promedio", ((silenc[1][1] - silenc[1][0]) +  (silenc[2][1] - silenc[2][0]) + (silenc[3][1] - silenc[3][0]))/3)

            
            data = [p, "GTR1", condicion, silencio, t, (silenc[1][1] - silenc[1][0]), (silenc[2][1] - silenc[2][0]), (silenc[3][1] - silenc[3][0]), ((silenc[1][1] - silenc[1][0]) +  (silenc[2][1] - silenc[2][0]) + (silenc[3][1] - silenc[3][0]))/3]
            writer.writerow(data)

            myaudio = AudioSegment.from_wav('audios2410/P'+str(p)+'_'+condicion+'_'+silencio+'_GTR2_00'+str(t)+'.wav')
    
            dBFS=myaudio.dBFS
    
            silenc = silence.detect_silence(myaudio, min_silence_len=500, silence_thresh=dBFS-16)

            silenc = [((start/1000),(stop/1000)) for start,stop in silenc] #in sec

            #print(silenc)
            print(str(p)+"_"+ str(t))
            print(silenc[1][1] - silenc[1][0])
            print(silenc[2][1] - silenc[2][0])
            print(silenc[3][1] - silenc[3][0])
            print("promedio", ((silenc[1][1] - silenc[1][0]) + (silenc[2][1] - silenc[2][0]) + (silenc[3][1] - silenc[3][0])) / 3)
            data = [p, "GTR2", condicion, silencio, t, (silenc[1][1] - silenc[1][0]), (silenc[2][1] - silenc[2][0]), (silenc[3][1] - silenc[3][0]), ((silenc[1][1] - silenc[1][0]) + (silenc[2][1] - silenc[2][0]) + (silenc[3][1] - silenc[3][0])) / 3]
            writer.writerow(data)
            

#print(silence[1][1] - silence[1][0])
#print(silence[2][1] - silence[2][0])
#print(silence[3][1] - silence[3][0]) 