import argparse
from typing import Dict, List

from torchvision.datasets import ImageNet


def main(imagenet_root: str, wordnet_is_a_txt_path: str, words_txt_path: str, superclass_path: str, superclass_names_path: str) -> None:
    wnids = ImageNet(imagenet_root, split='val').wnids
    with open(wordnet_is_a_txt_path, 'r') as f:
        wn_lines = f.readlines()
    with open(words_txt_path, 'r') as f:
        w_lines = f.readlines()
    child_to_parent_wnid = {}
    for wn_line in wn_lines:
        parent_wnid, child_wnid = wn_line.split()
        child_to_parent_wnid[child_wnid] = parent_wnid
    wnid_to_name: Dict[str, str] = {}
    for w_line in w_lines:
        wnid, name = w_line.split('\t')
        wnid_to_name[wnid] = name
    parent_wnid_set = set()
    for child_wnid in wnids:
        parent_wnid = child_to_parent_wnid[child_wnid]
        parent_wnid_set.add(parent_wnid)
    parent_wnid_list = list(parent_wnid_set)
    parent_wnid_list.sort()
    print('the number of parent classes', len(parent_wnid_list))
    parent_idx_list: List[str] = []
    parent_name_list: List[str] = []
    for child_wnid in wnids:
        parent_wnid = child_to_parent_wnid[child_wnid]
        parent_name = wnid_to_name[parent_wnid].rstrip('\n')
        parent_idx = parent_wnid_list.index(parent_wnid)
        parent_idx_str = str(parent_idx)
        parent_idx_list.append(parent_idx_str)
        parent_name_list.append(parent_name)
    assert len(parent_idx_list) == 1000 and len(parent_name_list) == 1000
    parent_idx_list_txt = '\n'.join(parent_idx_list)
    parent_name_list_txt = '\n'.join(parent_name_list)
    with open(superclass_path, 'w') as f:
        f.write(parent_idx_list_txt)
    with open(superclass_names_path, 'w') as f:
        f.write(parent_name_list_txt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('imagenet_root', help='ImageNet root')
    parser.add_argument('wordnet_is_a_txt_path', help='wordnet.is_a.txt path')
    parser.add_argument('words_txt_path', help='words.txt path')
    parser.add_argument('--superclass_path', '-s', default='superclass.txt', help='superclass path')
    parser.add_argument('--superclass_names_path', '-sn', default='superclass_names.txt', help='superclass names path')
    args = parser.parse_args()

    imagenet_root: str = args.imagenet_root
    wordnet_is_a_txt_path: str = args.wordnet_is_a_txt_path
    words_txt_path: str = args.words_txt_path
    superclass_path: str = args.superclass_path
    superclass_names_path: str = args.superclass_names_path

    main(imagenet_root, wordnet_is_a_txt_path, words_txt_path, superclass_path, superclass_names_path)
