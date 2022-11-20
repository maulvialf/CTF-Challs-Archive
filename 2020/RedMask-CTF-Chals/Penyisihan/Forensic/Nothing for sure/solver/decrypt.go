package main

import (
	"crypto/aes"
	"crypto/cipher"
	"fmt"
	"io/ioutil"
	"os"
)

func decrypt(ciphertext []byte, key []byte) string {
	block, _ := aes.NewCipher(key)
	iv := ciphertext[:aes.BlockSize]
	ciphertext = ciphertext[aes.BlockSize:]

	stream := cipher.NewCFBDecrypter(block, iv)
	stream.XORKeyStream(ciphertext, ciphertext)

	return string(ciphertext)
}

func decryptFile(pathname string, key []byte) {
	dat, _ := ioutil.ReadFile(pathname)
	decrypted := decrypt([]byte(dat), key)
	fmt.Print(decrypted)
}

func main() {
	key := []byte{114, 101, 100, 109, 97, 115, 107, 95, 95, 95, 115, 101, 99, 114, 101, 116}
	decryptFile(os.Args[1], key)
}
