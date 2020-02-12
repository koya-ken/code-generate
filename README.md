## require

```
conda create -n code-generate python=3.8
conda install jinja2
# conda install -c anaconda pyyaml
conda install -c conda-forge ruamel.yaml
```

yamlは読み込むだけならpyyamlでもruamel.yamlでも問題ない  
ruamel.yamlはファイル名指定で読み込めるのでそっちを使う

## generate code

```
python generate.py
```
