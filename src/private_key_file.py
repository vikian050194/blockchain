ALICE_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-47-44.156921182Z--4261615f91055c19e3d09f2584b47baf1fd58313'
with open(ALICE_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   ALICE_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')

BOB_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-47-52.900024617Z--07358db463ca9449185d75040d8258d9ab564442'
with open(BOB_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   BOB_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')
