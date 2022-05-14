import os
from turtle import mode
import numpy as np
import mne
import flask 

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/view', methods=['GET'])
def getEEG():
    sample_data_folder = mne.datasets.sample.data_path()
    sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                    'sample_audvis_filt-0-40_raw.fif')
    raw = mne.io.read_raw_fif(sample_data_raw_file)

    print(raw)
    print(raw.info)

    # raw.plot_psd(fmax=50)
    # raw.plot(duration=5, n_channels=30)
    sampling_freq = raw.info['sfreq']
    start_stop_seconds = np.array([11, 13])
    start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
    channel_index = 0
    raw_selection = raw[channel_index, start_sample:stop_sample]
    print(raw_selection)
    arr1 = raw_selection[1].tolist()
    arr2 = raw_selection[0].tolist()
    return jsonify({"arr1": arr1},{"arr2": arr2})

if __name__ == "__main__":
    app.run(host='192.168.100.171', port='3000',debug=True)
    


