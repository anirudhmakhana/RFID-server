# The Open Library Project

A peer to peer library powered by smart contracts and chainlink enabled RFID hardware.

EMBED DEMO VIDEO HERE

Note: this project is still in early development stages.

**Contents:**

- `rfid-interface`: (python) covers the stack from the serial port hardware interface to running an external adapter server through flask. Lots going on here. All good stuff.
- `contracts`: (solidity) ethereum contracts that contain the main business logic for the peer to peer library. `Library.sol` is the main contract here - connects to external adapter through chainlink node and holds the state of all entries (books) in the system. 
- `frontend`: (HTML/JS) frontend web3 app to interface with the smart contracts.

## Build/run instructions

**Start external adapter server**:
```
cd rfid-adapter
./server.sh
```
This will expose the RFID external adapter server at https://link-adapter.loca.lt (if the URL is available). Note that a node operator will need to add this job in order for the contract to work (and the contract oracle address and job id also have to be updated).

**Deploy contracts**:
```
cd truffle-env
truffle compile
truffle migrate --network kovan
```
This will deploy the Library.sol contract to the kovan testnet. Sometimes there are problems with infura, in which case you should copy the contract code into remix to deploy.

**Start front end server**:
```
cd frontend
./server.sh
```
This will start an http server at https://p2p-library.loca.lt (if URL is available). 

#### Things that can go wrong:

Adapter --> Contract:
- Chainlink node details don't match the external adapter.
- Localtunnel URL is incorrect.

Contract --> Frontend:
- ABI from deployed contract doesn't match ABI in `frontend/index.js`.
- Deployed contract address doesn't match the frontend.
- Localtunnel URL is incorrect.

## Architecture

TODO
