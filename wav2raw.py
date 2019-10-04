from scipy.io import wavfile
import os 
import h5py

# custom imports
import librispect as lspct

 

# trainroot = ['train-clean-100-wav/', 'train-clean-360-wav/', 'train-other-500-wav/']
# devroot = ['dev-clean/', 'dev-other/']
# testroot = ['test-clean/']

dev_clean = lspct.paths.DEV_CLEAN
dev_other = lspct.paths.DEV_OTHER
train_clean_100 = lspct.paths.TRAIN_CLEAN_100
train_clean_360 = lspct.paths.TRAIN_CLEAN_360
train_other_500 = lspct.paths.TRAIN_OTHER_500
test_clean = lspct.paths.TEST_CLEAN

trainroot = [train_clean_100, train_clean_360, train_other_500]
devroot = [dev_clean, dev_other]
testroot = [test_clean] 

"""convert wav files to raw wave form and store them in the disc 
"""

# store train 
h5f = h5py.File('train-Librispeech.h5', 'w')
for rootdir in trainroot:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.wav'):
                fullpath = os.path.join(subdir, file)
                fs, data = wavfile.read(fullpath)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()

# store dev 
h5f = h5py.File('dev-Librispeech.h5', 'w')
for rootdir in devroot:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.wav'):
                fullpath = os.path.join(subdir, file)
                fs, data = wavfile.read(fullpath)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()

# store test
h5f = h5py.File('test-Librispeech.h5', 'w')
for rootdir in testroot:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.wav'):
                fullpath = os.path.join(subdir, file)
                fs, data = wavfile.read(fullpath)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()

