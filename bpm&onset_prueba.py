from essentia.standard import *
import essentia.standard as es
from tempfile import TemporaryDirectory
import IPython




# Load audio file.
audio = MonoLoader(filename='GUITARRABASE1.wav')()

# 1. Compute the onset detection function (ODF).

# The OnsetDetection algorithm provides various ODFs.
od_hfc = OnsetDetection(method='hfc')
od_complex = OnsetDetection(method='complex')

# We need the auxilary algorithms to compute magnitude and phase.
w = Windowing(type='hann')
fft = FFT() # Outputs a complex FFT vector.
c2p = CartesianToPolar() # Converts it into a pair of magnitude and phase vectors.

# Compute both ODF frame by frame. Store results to a Pool.
pool = essentia.Pool()
for frame in FrameGenerator(audio, frameSize=1024, hopSize=512):
    magnitude, phase = c2p(fft(w(frame)))
    pool.add('odf.hfc', od_hfc(magnitude, phase))
    pool.add('odf.complex', od_complex(magnitude, phase))


# 2. Detect onset locations.
onsets = Onsets()
onsets_hfc = onsets(# This algorithm expects a matrix, not a vector.
                    essentia.array([pool['odf.hfc']]),
                    # You need to specify weights, but if we use only one ODF
                    # it doesn't actually matter which weight to give it
                    [1])

onsets_complex = onsets(essentia.array([pool['odf.complex']]), [1])
'''
def computeOnsets(filename, pool):
    loader = EasyLoader(filename=filename,
                        sampleRate=pool['samplerate'],
                        startTime=STARTTIME, endTime=ENDTIME,
                        downmix=pool['downmix'])
    onset = OnsetRate()
    loader.audio >> onset.signal
    onset.onsetTimes >> (pool, 'ticks')
    onset.onsetRate >> None
    essentia.run(loader)
    pool.set('size', loader.audio.totalProduced())
    pool.set('length', pool['size']/pool['samplerate'])



'''
for on in onsets_complex:

    from scipy.io.wavfile import write
    import numpy as np

    samplerate = 44100

    t = np.linspace(0., 1., samplerate)

    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2. * np.pi * on * t)
    write("mi_wav.wav", samplerate, data.astype(np.int16))



    audio = es.MonoLoader(filename='mi_wav.wav')()
    rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
    bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)

    print("BPM:", bpm, "onset:",  on)
    #print(audio)

IPython.display.Audio('mi_wav.wav')

