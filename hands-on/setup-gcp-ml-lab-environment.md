# Setup GCP ML

## VM Configuration
```
16 GB RAM
8 Core CPU
SSD Disk
```


## Install Python
```
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.10-venv python3-pip
sudo mkdir -p /pyenv
sudo chmod -R 777 /pyenv
python3 -m venv /pyenv
source /pyenv/bin/activate
sudo mkdir -p /workdir
sudo chmod -R 777 /workdir
cd /workdir
pip install jupyter
nohup jupyter notebook --ip 0.0.0.0 --port 8888 &
```


## Install packages on Ubuntu
```
sudo apt install -y tree zip vim nano ranger net-tools iputils-ping p7zip-full
sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo -y
```

```
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```

```
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

```
sudo apt-get update
```

```
sudo snap install google-cloud-cli --classic
```

### Authenticate to GCP

```
gcloud init
gcloud auth application-default login
gcloud auth login
gcloud config set project PROJECT_ID
```

### Install packages in Python
```
source /pyenv/bin/activate
pip install google.cloud.storage
```

```
pip install google.cloud.aiplatform -U
```

```
pip install --upgrade gcsfs -U
```

```
pip install --upgrade google-cloud-bigquery -U
```

```
pip install --upgrade google-cloud-bigquery-storage -U
```

```
pip install pandas
```

```
pip install scikit-learn
```

```
pip install kfp -U
```

```
pip install  google-cloud-pipeline-components -U
```

```
pip install  googleapis-common-protos -U
```

```
pip install google-cloud-aiplatform -U
```

```
pip install matplotlib
```

```
pip install db-dtypes
```

### Close Git Repo
```
git clone https://github.com/atingupta2005/GCP-ML-Oct-23
```

### Setup Jupyter Notebook
```
cd /workdir
pip install jupyter
tail nohup.out
```



## How to start
- Open Powershell and run below commandsL

```
ssh gcpuser@<public-ip-address>
source /pyenv/bin/activate
cd /workdir/
pkill -f jupyter
nohup jupyter notebook --ip 0.0.0.0 --port 8888 &
tail nohup.out
```

- Now open browser in your laptop and hit below URL:
  -  https://<public-ip-address>:8888
