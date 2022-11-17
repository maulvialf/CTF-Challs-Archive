use std::io::{self, Read};
use aes::Aes256;
use aes::cipher::generic_array::GenericArray;
use aes::cipher::{BlockEncrypt, KeyInit};
use nuts_and_bolts::StorageMethod;
use rand::Rng;


fn main() {
    let mut flag = [0u8; 64];
    io::stdin().read(&mut flag).expect("Flag not provided");
    
    let orig_key = rand::thread_rng().gen::<[u8; 32]>();
    let key = GenericArray::from(orig_key);
    let cipher = Aes256::new(&key);

    flag.chunks_mut(16).for_each(|block| {
        cipher.encrypt_block(GenericArray::from_mut_slice(block));
    });
    let mut key = StorageMethod::plain(orig_key);
    let mut flag = StorageMethod::plain(flag);
    let mut rng = rand::thread_rng();
    for _ in 0..10 {
        key = if rng.gen::<u8>() % 2 == 0 {
            key.reverse()
        } else {
            key.xor()
        };
        flag = if rng.gen::<u8>() % 2 == 0 {
            flag.reverse()
        } else {
            flag.xor()
        };
    }
    println!("Here's your key: {:?}!", bincode::serialize(&key).unwrap());
    println!("And here's your flag: {:?}!", bincode::serialize(&flag).unwrap());
}

