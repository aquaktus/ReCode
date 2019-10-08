# ReCode
## Retrieval-Based Neural Code Generation

http://aclweb.org/anthology/D18-1111

## How to Run
Run the command `bash run_trained_model.sh`

## How to train CPU (≈5 hours), Updated by Aquaktus (Carlos Gemmell)
```
git clone https://github.com/aquaktus/ReCode.git
virtualenv -p python2.7 ReCode
cd ReCode
pip install -r requirements.txt 
mkdir data
cd data
wget https://storage.googleapis.com/miscellaneous_carlos_gemmell/ReCode/django.cleaned.dataset.freq3.par_info.refact.space_only.order_by_ulink_len.bin
cd ..
bash train.sh 
```

## List of modifications to the original code
- train.sh to include retrieval and alignment
- decoder.py l8-9 fixing too many parameters giving error
- code_gen.py l8 commenting out vprof since can't install
- dataset.py changing absolute paths to own spec


## BibTex
```
# coding=utf-8

@InProceedings{D18-1111,
  author = 	"Hayati, Shirley Anugrah
		and Olivier, Raphael
		and Avvaru, Pravalika
		and Yin, Pengcheng
		and Tomasic, Anthony
		and Neubig, Graham",
  title = 	"Retrieval-Based Neural Code Generation",
  booktitle = 	"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"925--930",
  location = 	"Brussels, Belgium",
  url = 	"http://aclweb.org/anthology/D18-1111"
}
```
