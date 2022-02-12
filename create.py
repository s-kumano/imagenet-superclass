import argparse

from torchvision.datasets import ImageNet


def main(imagenet_root: str, wordnet_is_a_txt_path: str, dst_path: str):
    dataset = ImageNet(imagenet_root, split='val')
    with open(wordnet_is_a_txt_path, 'r') as f:
        lines = f.readlines()
    child_to_parent_wnid = {}
    for line in lines:
        parent_wnid, child_wnid = line.split()
        child_to_parent_wnid[child_wnid] = parent_wnid
    parent_wnid_set = set()
    for child_wnid in dataset.wnids:
        parent_wnid = child_to_parent_wnid[child_wnid]
        parent_wnid_set.add(parent_wnid)
    parent_wnid_list = list(parent_wnid_set)
    print('the number of parent classes', len(parent_wnid_list))
    parent_idx_list = []
    for child_wnid in dataset.wnids:
        parent_wnid = child_to_parent_wnid[child_wnid]
        parent_idx = parent_wnid_list.index(parent_wnid)
        parent_idx_str = str(parent_idx)
        parent_idx_list.append(parent_idx_str)
    assert len(parent_idx_list) == 1000
    parent_idx_list_txt = '\n'.join(parent_idx_list)
    with open(dst_path, 'w') as f:
        f.write(parent_idx_list_txt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('imagenet_root', help='ImageNet root')
    parser.add_argument('wordnet_is_a_txt_path', help='wordnet.is_a.txt path')
    parser.add_argument('--dst_path', '-d', default='superclass.txt', help='destination path')
    args = parser.parse_args()

    imagenet_root: str = args.imagenet_root
    wordnet_is_a_txt_path: str = args.wordnet_is_a_txt_path
    dst_path: str = args.dst_path

    main(imagenet_root, wordnet_is_a_txt_path, dst_path)
