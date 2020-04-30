"""
Created on Tue Apr 21 18:15:21 2020

@author: zding
edited from hdf5_getters by Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu
"""
import numpy as np

def get_num_songs(data,songidx=0):
    """
    Return the number of songs contained in this h5 file, i.e. the number of rows
    for all basic informations like name, artist, ...
    """
    return data['metadata']['songs']['artist_name'][songidx]

def get_artist_familiarity(data,songidx=0):
    """
    Get artist familiarity from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_familiarity'][songidx]

def get_artist_hotttnesss(data,songidx=0):
    """
    Get artist hotttnesss from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_hotttnesss'][songidx]

def get_artist_id(data,songidx=0):
    """
    Get artist id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_id'][songidx]

def get_artist_mbid(data,songidx=0):
    """
    Get artist musibrainz id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_mbid'][songidx]

def get_artist_playmeid(data,songidx=0):
    """
    Get artist playme id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_playmeid'][songidx]

def get_artist_7digitalid(data,songidx=0):
    """
    Get artist 7digital id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_7digitalid'][songidx]

def get_artist_latitude(data,songidx=0):
    """
    Get artist latitude from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_latitude'][songidx]

def get_artist_longitude(data,songidx=0):
    """
    Get artist longitude from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_longitude'][songidx]

def get_artist_location(data,songidx=0):
    """
    Get artist location from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_location'][songidx]

def get_release(data,songidx=0):
    """
    Get release from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['release'][songidx]

def get_release_7digitalid(data,songidx=0):
    """
    Get release 7digital id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['release_7digitalid'][songidx]

def get_song_id(data,songidx=0):
    """
    Get song id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['song_id'][songidx]

def get_song_hotttnesss(data,songidx=0):
    """
    Get song hotttnesss from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['song_hotttnesss'][songidx]

def get_title(data,songidx=0):
    """
    Get title from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['title'][songidx]

def get_track_7digitalid(data,songidx=0):
    """
    Get track 7digital id from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['track_7digitalid'][songidx]

def get_similar_artists(data,songidx=0):
    """
    Get similar artists array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['metadata']['songs'].shape[0] == songidx + 1:
        return data['metadata']['similar_artists'][data['metadata']['songs']['idx_similar_artists'][songidx]:].shape
    return data['metadata']['similar_artists'][data['metadata']['songs']['idx_similar_artists'][songidx]:
                                            data['metadata']['songs']['idx_similar_artists'][songidx+1]].shape

def get_artist_terms(data,songidx=0):
    """
    Get artist terms array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['metadata']['songs'].shape[0] == songidx + 1:
        return data['metadata']['artist_terms'][data['metadata']['songs']['idx_artist_terms'][songidx]:]
    return data['metadata']['artist_terms'][data['metadata']['songs']['idx_artist_terms'][songidx]:
                                            data['metadata']['songs']['idx_artist_terms'][songidx+1]]

def get_artist_terms_freq(data,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['metadata']['songs'].shape[0] == songidx + 1:
        return np.mean(data['metadata']['artist_terms_freq'][data['metadata']['songs']['idx_artist_terms'][songidx]:])
    return np.mean(data['metadata']['artist_terms_freq'][data['metadata']['songs']['idx_artist_terms'][songidx]:
                                              data['metadata']['songs']['idx_artist_terms'][songidx+1]])

def get_artist_terms_weight(data,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['metadata']['songs'].shape[0] == songidx + 1:
        return data['metadata']['artist_terms_weight'][data['metadata']['songs']['idx_artist_terms'][songidx]:].shape
    return data['metadata']['artist_terms_weight'][data['metadata']['songs']['idx_artist_terms'][songidx]:
                                                data['metadata']['songs']['idx_artist_terms'][songidx+1]].shape

def get_analysis_sample_rate(data,songidx=0):
    """
    Get analysis sample rate from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['analysis_sample_rate'][songidx]

def get_audio_md5(data,songidx=0):
    """
    Get audio MD5 from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['audio_md5'][songidx]

def get_danceability(data,songidx=0):
    """
    Get danceability from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['danceability'][songidx]

def get_duration(data,songidx=0):
    """
    Get duration from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['duration'][songidx]

def get_end_of_fade_in(data,songidx=0):
    """
    Get end of fade in from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['end_of_fade_in'][songidx]

def get_energy(data,songidx=0):
    """
    Get energy from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['energy'][songidx]

def get_key(data,songidx=0):
    """
    Get key from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['key'][songidx]

def get_key_confidence(data,songidx=0):
    """
    Get key confidence from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['key_confidence'][songidx]

def get_loudness(data,songidx=0):
    """
    Get loudness from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['loudness'][songidx]

def get_mode(data,songidx=0):
    """
    Get mode from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['mode'][songidx]

def get_mode_confidence(data,songidx=0):
    """
    Get mode confidence from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['mode_confidence'][songidx]

def get_start_of_fade_out(data,songidx=0):
    """
    Get start of fade out from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['start_of_fade_out'][songidx]

def get_tempo(data,songidx=0):
    """
    Get tempo from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['tempo'][songidx]

def get_time_signature(data,songidx=0):
    """
    Get signature from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['time_signature'][songidx]

def get_time_signature_confidence(data,songidx=0):
    """
    Get signature confidence from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['time_signature_confidence'][songidx]

def get_track_id(data,songidx=0):
    """
    Get track id from a HDF5 song file, by default the first song in it
    """
    return data['analysis']['songs']['track_id'][songidx]

def get_segments_start(data,songidx=0):
    """
    Get segments start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['segments_start'][data['analysis']['songs']['idx_segments_start'][songidx]:])
    return np.mean(data['analysis']['segments_start'][data['analysis']['songs']['idx_segments_start'][songidx]:
                                           data['analysis']['songs']['idx_segments_start'][songidx+1]])
    
def get_segments_confidence(data,songidx=0):
    """
    Get segments confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['segments_confidence'][data['analysis']['songs']['idx_segments_confidence'][songidx]:])
    return np.mean(data['analysis']['segments_confidence'][data['analysis']['songs']['idx_segments_confidence'][songidx]:
                                                data['analysis']['songs']['idx_segments_confidence'][songidx+1]])

def get_segments_pitches(data,songidx=0):
    """
    Get segments pitches array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return data['analysis']['segments_pitches'][data['analysis']['songs']['idx_segments_pitches'][songidx]:,:].shape
    return data['analysis']['segments_pitches'][data['analysis']['songs']['idx_segments_pitches'][songidx]:
                                             data['analysis']['songs']['idx_segments_pitches'][songidx+1],:].shape

def get_segments_timbre(data,songidx=0):
    """
    Get segments timbre array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return data['analysis']['segments_timbre'][data['analysis']['songs']['idx_segments_timbre'][songidx]:,:].shape
    return data['analysis']['segments_timbre'][data['analysis']['songs']['idx_segments_timbre'][songidx]:
                                             data['analysis']['songs']['idx_segments_timbre'][songidx+1],:].shape

def get_segments_loudness_max(data,songidx=0):
    """
    Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['segments_loudness_max'][data['analysis']['songs']['idx_segments_loudness_max'][songidx]:])
    return np.mean(data['analysis']['segments_loudness_max'][data['analysis']['songs']['idx_segments_loudness_max'][songidx]:
                                             data['analysis']['songs']['idx_segments_loudness_max'][songidx+1]])

def get_segments_loudness_max_time(data,songidx=0):
    """
    Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return data['analysis']['segments_loudness_max_time'][data['analysis']['songs']['idx_segments_loudness_max_time'][songidx]:].shape
    return data['analysis']['segments_loudness_max_time'][data['analysis']['songs']['idx_segments_loudness_max_time'][songidx]:
                                             data['analysis']['songs']['idx_segments_loudness_max_time'][songidx+1]].shape
    
def get_segments_loudness_start(data,songidx=0):
    """
    Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['segments_loudness_start'][data['analysis']['songs']['idx_segments_loudness_start'][songidx]:])
    return np.mean(data['analysis']['segments_loudness_start'][data['analysis']['songs']['idx_segments_loudness_start'][songidx]:
                                             data['analysis']['songs']['idx_segments_loudness_start'][songidx+1]])

def get_sections_start(data,songidx=0):
    """
    Get sections start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['sections_start'][data['analysis']['songs']['idx_sections_start'][songidx]:])
    return np.mean(data['analysis']['sections_start'][data['analysis']['songs']['idx_sections_start'][songidx]:
                                             data['analysis']['songs']['idx_sections_start'][songidx+1]])

def get_sections_confidence(data,songidx=0):
    """
    Get sections confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['sections_confidence'][data['analysis']['songs']['idx_sections_confidence'][songidx]:])
    return np.mean(data['analysis']['sections_confidence'][data['analysis']['songs']['idx_sections_confidence'][songidx]:
                                             data['analysis']['songs']['idx_sections_confidence'][songidx+1]])

def get_beats_start(data,songidx=0):
    """
    Get beats start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['beats_start'][data['analysis']['songs']['idx_beats_start'][songidx]:])
    return np.mean(data['analysis']['beats_start'][data['analysis']['songs']['idx_beats_start'][songidx]:
                                             data['analysis']['songs']['idx_beats_start'][songidx+1]])

def get_beats_confidence(data,songidx=0):
    """
    Get beats confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['beats_confidence'][data['analysis']['songs']['idx_beats_confidence'][songidx]:])
    return np.mean(data['analysis']['beats_confidence'][data['analysis']['songs']['idx_beats_confidence'][songidx]:
                                             data['analysis']['songs']['idx_beats_confidence'][songidx+1]])

def get_bars_start(data,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['bars_start'][data['analysis']['songs']['idx_bars_start'][songidx]:])
    return np.mean(data['analysis']['bars_start'][data['analysis']['songs']['idx_bars_start'][songidx]:
                                             data['analysis']['songs']['idx_bars_start'][songidx+1]])
    

def get_bars_confidence(data,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['bars_confidence'][data['analysis']['songs']['idx_bars_confidence'][songidx]:])
    return np.mean(data['analysis']['bars_confidence'][data['analysis']['songs']['idx_bars_confidence'][songidx]:
                                             data['analysis']['songs']['idx_bars_confidence'][songidx+1]])

def get_tatums_start(data,songidx=0):
    """
    Get tatums start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['tatums_start'][data['analysis']['songs']['idx_tatums_start'][songidx]:])
    return np.mean(data['analysis']['tatums_start'][data['analysis']['songs']['idx_tatums_start'][songidx]:
                                             data['analysis']['songs']['idx_tatums_start'][songidx+1]])
    

def get_tatums_confidence(data,songidx=0):
    """
    Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['analysis']['songs'].shape[0] == songidx + 1:
        return np.mean(data['analysis']['tatums_confidence'][data['analysis']['songs']['idx_tatums_confidence'][songidx]:])
    return np.mean(data['analysis']['tatums_confidence'][data['analysis']['songs']['idx_tatums_confidence'][songidx]:
                                             data['analysis']['songs']['idx_tatums_confidence'][songidx+1]])
    

def get_artist_mbtags(data,songidx=0):
    """
    Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['musicbrainz']['songs'].shape[0] == songidx + 1:
        return data['musicbrainz']['artist_mbtags'][data['musicbrainz']['songs']['idx_artist_mbtags'][songidx]:].shape
    return data['musicbrainz']['artist_mbtags'][data['metadata']['songs']['idx_artist_mbtags'][songidx]:
                                             data['metadata']['songs']['idx_artist_mbtags'][songidx+1]].shape
    

def get_artist_mbtags_count(data,songidx=0):
    """
    Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if data['musicbrainz']['songs'].shape[0] == songidx + 1:
        return data['musicbrainz']['artist_mbtags_count'][data['musicbrainz']['songs']['idx_artist_mbtags'][songidx]:].shape
    return data['musicbrainz']['artist_mbtags_count'][data['metadata']['songs']['idx_artist_mbtags'][songidx]:
                                             data['metadata']['songs']['idx_artist_mbtags'][songidx+1]].shape
        
def get_year(data,songidx=0):
    """
    Get release year from a HDF5 song file, by default the first song in it
    """
    return data['musicbrainz']['songs']['year'][songidx]

def get_artist_name(data,songidx=0):
    """
    Get artist name from a HDF5 song file, by default the first song in it
    """
    return data['metadata']['songs']['artist_name'][songidx]