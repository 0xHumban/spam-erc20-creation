# Spam-erc20-creation

> The goal: share your social media links on Telegram groups that detect newly verified tokens, and attract new buyers.

## Requirements
- python >= 3
- [brownie](https://github.com/eth-brownie/brownie)

## Configuration

### Contract configuration
Modify the contract ``Token.sol`` with your info in the ``./contracts`` directory


> You can build the contract, to check any errors: ``$ brownie build --all``


### Script configuration
> Configure the script in the ``brownie-config.yaml``

### Token and Key configuration

#### Token configuration:
```
$ export ETHERSCAN_TOKEN=YOUR_ETHERSCAN_KEY
$ export BASESCAN_TOKEN=YOUR_ETHERSCAN_KEY
```
#### Keys configuration:

```
$ export PUBLIC_KEY=YOUR_PUBLIC_KEY
 export PRIVATE_KEY=YOUR_PRIVATE_KEY
```

> You can write this lines in your ``.bashrc`` file, to not rewrite the configuration before each launch.


### Networks configuration
Check networks config:
``$ brownie networks list true``

> You can add your own network in ``netword-config.yaml`` (example wrote in)

Import the file to the brownie configuration:  
``$ brownie networks import ./network-config.yaml``

Check the network configuration:
``$ brownie networks list true``

Tutorial: [brownie networks tutorial](https://www.codeforests.com/2022/01/27/python-brownie-network-setup/)

## Run
``$ brownie run scripts/spam_erc20.py --network base-sepolia``
> Replace ``base-sepolia`` by the network to deploy contracts

### Logs
After each contract deployment, the contract address is wrote in a file in the ``./addresses`` folder

## Contributing

Thanks for your help improving the project! 

Feel free to open issue / create pull requests!

## Credits

This script would not have been possible without the great work done in:
- [token-mix](https://github.com/brownie-mix/token-mix)


## License
This script is licensed under the MIT License, similar to the content used within it.