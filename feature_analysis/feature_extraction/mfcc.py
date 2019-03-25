import numpy as np
from pyAudioAnalysis import audioFeatureExtraction


def extract_mfcc(
    signal: np.ndarray,
    sample_rate: int=44100,
    window: float=0.5,
    stride: float=0.25
):
    feats, f_names = audioFeatureExtraction.stFeatureExtraction(
            signal,
            sample_rate,
            sample_rate * window,
            stride * sample_rate
    )

    return feats.T, f_names
