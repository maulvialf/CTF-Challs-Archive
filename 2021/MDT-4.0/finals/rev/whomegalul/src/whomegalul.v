module main

import os
import hash.crc32
import crypto.sha1

struct Credential {
	hostname string
mut:
	message string
}

fn (mut c Credential) validate() {
	match c.hostname.len {
		16 {
			p := crc32.sum(c.hostname[..4].bytes())
			q := crc32.sum(c.hostname[4..8].bytes())
			r := crc32.sum(c.hostname[8..12].bytes())
			s := crc32.sum(c.hostname[12..].bytes())
			data := [p, q, r, s]
			mut count := 0
			compare := [4628670836, 3103493584, 3130303600, 4628670836, 1577575616, 1604385632, 3103493584, 1577575616, 79208380, 3130303600, 1604385632, 79208380]
			for i in data {
				for j in data {
					if i != j{
					match i + j {
							u32(compare[count]) {
								count++
							}
							else { return }
						}
					}
				}
			}
			hash := sha1.hexhash(c.hostname)
			c.message = "MDT4.0{$hash}"

		}
		else { return }
	}
}

fn main() {
	mut creds := Credential{os.hostname(),  "program ini hanya dapat di jalankan oleh agent khusus"}
	creds.validate()
	println(creds.message)
}
