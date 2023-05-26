import argparse
from pathlib import Path
import random
import os
import shutil


def get_indices(num_examples, train_pct):
    indices = list(range(num_examples))
    random.shuffle(indices)

    num_train = int(num_examples * train_pct / 100)
    num_valid = int(num_examples * (100 - train_pct) / 200)

    train_indices = indices[:num_train]
    valid_indices = indices[num_train:num_train + num_valid]
    test_indices = indices[num_train + num_valid:]

    return train_indices, valid_indices, test_indices


def copy_dataset(list_indices, image_files, labels_dir, destination):
    for idx in list_indices:
        image_path = image_files[idx]
        shutil.copy(str(image_path), str(destination / image_path.name))
        label_path = labels_dir / (image_path.stem + ".txt")
        shutil.copy(str(label_path), str(destination / (image_path.stem + ".txt")))

    print("Copied {} images and labels to {}".format(len(list_indices), destination))


def main():
    parser = argparse.ArgumentParser(description="Create datasets to train YOLO on Duckietown images")
    parser.add_argument("datadir", help="Directory containing the subfolders frames and labels", type=str)
    parser.add_argument("outputdir", help="Directory that will contain the datasets", type=str)
    parser.add_argument("train_pct", help="Percentage to use to create the training dataset", type=int)

    args = parser.parse_args()

    datadir = Path(args.datadir)
    outputdir = Path(args.outputdir)
    train_pct = args.train_pct

    frames_dir = datadir / "frames"
    labels_dir = datadir / "labels"

    image_files = list(frames_dir.glob("*.jpg"))
    labels_files = list(labels_dir.glob("*.txt"))

    num_image_files = len(image_files)
    num_labels_files = len(labels_files)

    if num_image_files != num_labels_files:
        print("The number of jpg files and txt files must be equal")
        return

    train_indices, valid_indices, test_indices = get_indices(num_image_files, train_pct)

    trainset_dir = outputdir / "trainset"
    validset_dir = outputdir / "validset"
    testset_dir = outputdir / "testset"

    if trainset_dir.exists() or validset_dir.exists() or testset_dir.exists():
        print("There already exists at least one of trainset, validset, testset directories in {}".format(outputdir))
        return

    os.mkdir(str(trainset_dir))
    os.mkdir(str(validset_dir))
    os.mkdir(str(testset_dir))

    copy_dataset(train_indices, image_files, labels_dir, trainset_dir)
    copy_dataset(valid_indices, image_files, labels_dir, validset_dir)
    copy_dataset(test_indices, image_files, labels_dir, testset_dir)


if __name__ == "__main__":
    main()
