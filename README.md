# Tokens Sender #

Script takes one by one line from data.csv and sends specified amount of tokens to destination address.
Source address if specified in settings.py

### Get parity or geth run ###
```
parity --warp --rpcapi "eth,net,web3,personal,parity"
ssh root@parity.mysqterium.local -L 18545:localhost:8545
```

### Setup account ###

## Setup Python3
```
brew install python3
brew install pip3
```

## Install the requirements using pip
```
pip3 install -r requirements.txt
```

### Running script###
```
python3 app.py
```