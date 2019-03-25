import yaml
import os
from typing import List, Dict
from scipy.io.wavfile import read
import pandas as pd
from pyAudioAnalysis import audioFeatureExtraction


def load_conf(
    conf_filepath: str='./conf.yaml'
) -> Dict:
    return yaml.load(open(conf_filepath, "r+"))


conf = load_conf()


def load_wav(
    file_path: str
):
    """Load wav data from specified wav file.
    """
    fs, data = read(file_path)
    return data, fs


def get_ESC50_tags(
    esc50_base_dir: str=conf['ESC50_BASE_DIR']
):
    """Returns ESC-50 category list.
    """
    df_metadata = pd.read_csv(os.path.join(esc50_base_dir, 'meta', 'esc50.csv'))

    return df_metadata['category'].value_counts()


def get_ESC50_wavfile(
    esc50_base_dir: str=conf['ESC50_BASE_DIR']
) -> List[str]:
    """Returns ESC-50 wav filepath list.
    """
    df_metadata = pd.read_csv(os.path.join(esc50_base_dir, 'meta', 'esc50.csv'))

    return list(esc50_base_dir + '/audio/' + df_metadata['filename'])


def get_ESC50_wavfile_by_tag(
    tag: str,
    esc50_base_dir: str=conf['ESC50_BASE_DIR'],
) -> List[str]:
    """Returns ESC-50 wav filepath for specified tag.
    """
    df_metadata = pd.read_csv(os.path.join(esc50_base_dir, 'meta', 'esc50.csv'))

    return list(esc50_base_dir + df_metadata[df_metadata['category'] == tag]['filename'])


def get_mfcc_feat_names():
    return conf['MFCC_FEAT_NAMES']
