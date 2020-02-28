# -*- coding: utf-8 -*-
"""
Created on Thu Fev 27 22:47:18 2020
@author: engoliveira

"""

import datetime
import hashlib
import time

class Block():
    blockNo = 0
    data = None
    next = None
    hash = None
    Nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        Hash = hashlib.sha256()
        Hash.update(
        str(self.Nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return Hash.hexdigest()

    def __str__(self):
        Info = "Block Hash: " + str(self.hash()) + "\nBlock Number: " + \
        str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + \
        str(self.Nonce)+"\n-----------------------------------------------------------------------------"
        return Info

class BlockChain():

    diff = 10
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        for i in range(self.maxNonce):
            if (int(block.hash(), 16) <= self.target):
                self.add(block)
                print(block)
                break
            else:
                block.Nonce += 1

if(__name__ == '__main__'):

    blockchain = BlockChain()

    for j in range(10):
        time.sleep(3) 
        while blockchain.head is not None:
            print(blockchain.head)
            blockchain.head = blockchain.head.next
            time.sleep(3)    
        
        blockchain.mine(Block("Block " + str(j+1)))