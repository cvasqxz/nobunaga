package main

import (
	"bytes"
	"log"

	"github.com/btcsuite/btcd/rpcclient"
	"github.com/btcsuite/btcd/txscript"
)

func main() {
	connCfg := &rpcclient.ConnConfig{
		Host:         "localhost:18332",
		CookiePath:   "/home/cvasqxz/.bitcoin/testnet3/.cookie",
		HTTPPostMode: true,
		DisableTLS:   true,
	}

	client, err := rpcclient.New(connCfg, nil)
	errorHandler(err)
	defer client.Shutdown()

	blockCount, err := client.GetBlockCount()
	errorHandler(err)

	for blockHeight := blockCount - 1000; blockHeight < blockCount; blockHeight++ {

		blockHash, err := client.GetBlockHash(blockHeight)
		errorHandler(err)

		block, err := client.GetBlock(blockHash)
		errorHandler(err)

		for _, transaction := range block.Transactions {
			for _, vin := range transaction.TxIn {
				if len(vin.Witness) == 0 {
					continue
				}

				for _, witness := range vin.Witness {
					ordStart := bytes.Index(witness, []byte{111, 114, 100})

					if len(witness) == 0 || ordStart == -1 {
						continue
					}

					decodedWitness, err := txscript.DisasmString(witness)
					errorHandler(err)

					log.Println(decodedWitness)

				}
			}
		}
	}

}

func errorHandler(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
