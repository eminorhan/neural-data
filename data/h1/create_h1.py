import os
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


_folder_mapping = {
    'sub-HumanPitt-held-in-calib': 'in-calib',
    'sub-HumanPitt-held-in-minival': 'in-minival',
    'sub-HumanPitt-held-out-calib': 'out-calib'
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',type=str, help='Data directory')
    return parser

if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = [f for f in sorted(os.listdir(args.data_dir)) if f.endswith('.nwb')]
    print(f"Files: {nwb_files}")

    # list to store results for each session
    kin_list, vel_list, timestamps_list, blacklist_list, epochs_list, trials_list, labels_list, spike_counts_list, identifier_list = [], [], [], [], [], [], [], [], []

    for file_name in nwb_files:
        file_path = os.path.join(args.data_dir, file_name)
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()
            units = nwbfile.units.to_dataframe()
            kin = nwbfile.acquisition['OpenLoopKinematics'].data[:].T
            vel = nwbfile.acquisition['OpenLoopKinematicsVelocity'].data[:].T
            timestamps = nwbfile.acquisition['OpenLoopKinematics'].offset + np.arange(kin.shape[0]) * nwbfile.acquisition['OpenLoopKinematics'].rate
            blacklist = ~nwbfile.acquisition['eval_mask'].data[:].astype(bool)
            trials = nwbfile.acquisition['TrialNum'].data[:]
            labels = [l.strip() for l in nwbfile.acquisition['OpenLoopKinematics'].description.split(',')]
            spike_counts = np.vstack([np.histogram(row, bins=np.append(timestamps, timestamps[-1] + nwbfile.acquisition['OpenLoopKinematics'].rate))[0] for row in units['spike_times']])  # spike count matrix (nxt: n is #channels, t is time bins)
            identifier = nwbfile.identifier

            # append trials
            kin_list.append(kin)
            vel_list.append(vel)
            timestamps_list.append(timestamps)
            blacklist_list.append(blacklist)
            trials_list.append(trials)
            labels_list.append(labels)
            spike_counts_list.append(spike_counts)
            identifier_list.append(identifier)

    def gen_data():
        for a, b, c, d, e, f, g, h in zip(kin_list, vel_list, timestamps_list, blacklist_list, trials_list, labels_list, spike_counts_list, identifier_list):
            yield {
                "kin": a,
                "vel": b,
                "timestamps": c,
                "blacklist": d,
                "trials": e,
                "labels": f,
                "spike_counts": g,
                "identifier": h
                }

    ds = Dataset.from_generator(gen_data)
        
    # push all data to hub under "all"
    ds.push_to_hub("eminorhan/h1", _folder_mapping[os.path.basename(args.data_dir)], token=True)