# Install PyFlink in Mac
## Install Conda
```bash
brew install --cask miniconda
conda create -n myenv python=3.10.14
conda init zsh
conda activate myenv

## Check if conda works
conda list
conda env list
```

## Install PyFlink
```bash
pip install --upgrade pip setuptools wheel
pip install apache-flink==1.19.0
```
Note, it may take some time(in my Mac, it takes 20min after `export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1` and `export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1`) to build grpc-io due to the python and grpc-io version. Check this [issue](https://github.com/grpc/grpc/issues/24026) for more details.


## Verify a simple example
```bash
python /usr/local/Caskroom/miniconda/base/envs/myenv/lib/python3.10/site-packages/pyflink/examples/datastream/word_count.py
```
The output is like this:
```txt
Using Any for unsupported type: typing.Sequence[~T]
No module named google.cloud.bigquery_storage_v1. As a result, the ReadFromBigQuery transform *CANNOT* be used with `method=DIRECT_READ`.
Executing word_count example with default input data set.
Use --input to specify file input.
Printing result to stdout. Use --output to specify output path.
(a,5)
(Be,1)
(Is,1)
(No,2)
(Or,1)
(To,4)
(be,1)
(by,2)
(he,1)
(in,3)
(is,2)
(my,1)
(of,14)
...
```
