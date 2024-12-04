# ImageNet superclass
The example of superclass list and source code. The number of superclasses is 558.

## requirements

### ImageNet dataset
See [here](https://pytorch.org/vision/stable/datasets.html#imagenet) for details.

### `wordnet.is_a.txt`
~Please download from [here](https://github.com/innerlee/ImagenetSampling/blob/master/Imagenet/data/wordnet.is_a.txt).~

Please download from [here](https://www.image-net.org/data/wordnet.is_a.txt) [official].

### `words.txt`
~Please download from [here](https://github.com/innerlee/ImagenetSampling/blob/master/Imagenet/data/words.txt).~

Please download from [here](https://www.image-net.org/data/words.txt) [official].

### `torch` and `torchvision`
```bash
pip install -r requirements.txt
```

## run
```bash
python create.py <imagenet_root> <wordnet_is_a_txt_path> <words_txt_path> -s <superclass_path> -sn <superclass_names_path>
```
