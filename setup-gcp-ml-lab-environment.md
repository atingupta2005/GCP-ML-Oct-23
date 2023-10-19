# Setup GCP ML

## Install packages
```
sudo apt-get update -y
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
sudo snap install google-cloud-cli
```

```
gcloud init
```

```
pip uninstall -y google.cloud.storage
```

```
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
