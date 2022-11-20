#include<stdio.h>
#include<string>
#include<iostream>
#include <vector>
using namespace std;


vector<string> split(string x){
	x = x.append((x.length()/3 + (x.length() % 3 != 0))*3 - x.length(),'F');
	// cout <<x <<endl;
	vector<string> blocks;
	for(int i=0; i<x.length()/3;i+=1){
		blocks.push_back(x.substr(i*3,3));
		// cout << blocks[i]<<endl;
	}

	return blocks;

}

string enc(string x){
	string res="    ";
	res[0] =(int)x[0]>>2;
	res[1] = (((int)x[0]&0x3)<<4)+((int)x[1]>>4);
	res[2] = (((int)x[1]&15)<<2)+(((int)x[2])>>6);
	res[3] = (int)x[2]&63;
	// string res=;
	// res.insert(res.end(),one+two+three+four);
	// res.append(char((((int)x[0]&0x3)<<4)+((int)x[1]>>4)));
	// res.append(char((((int)x[1]&15)<<2)+(((int)x[2])>>6)));
	// res.append(char((int)x[2]&63));
	return res;
}

int main(){
	string x;
	string res;
	// string test="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	string test="o5Rkw4VEt1rxYiT/vB2lg6XfjQHndANGb3+JmFc8MUSPOKZ0qC7DpaLzsue9WyIh";
	//"\x0d\x28\xc9\x21\x60\xe6\x87\x80\x5f\xca\x42\x4c\x4a\x3a\x0a\xf5\x23\x67\x8f\xed\xc7\x51\x13\xbc\x9b\x68\x54\x97\x1e\x41\xe0\xea\x90\x08\x50\x25\x6f\x44\xfc\x6c\x69\xaa\x6b\xb8\xe7\x02\x48\x2b\xe9\x3d\xc8\x70\xc3\x61\x2c\xf9\x72\x3b\x98\x7a\x81\xfb\xff\x03";
	cin >> x ;
	vector<string> blocks = split(x);
	for(int i=0;i<blocks.size();i++){
		// cout<<blocks[i]<<endl;
		blocks[i]=enc(blocks[i]);
		// cout<<blocks[i]<<endl;
	}
	for(int k=0;k<=100;k++){//update
		for(int i=0;i<blocks.size();i++){
			for(int j=0;j<4;j++){
				if(k!=100){//update
					if(i!=blocks.size()-1){
						blocks[i][j]= (int)blocks[i][j] ^ (int)blocks[i+1][j];	
					} else{
						blocks[i][j]= (int)blocks[i][j] ^ (int)blocks[0][j]; //update
					}
				}else{
					printf("%c",test[blocks[i][j]]);//update
				}
			}
		}
	}
	printf("\n");

	// scanf("%s",&x);

	// for (int i = 0; i < strlen(x); i+=3)
	// {
	// 	// printf("%d\n",i);
	// 	printf("%02x",test[x[i]>>2]);
	// 	printf("%02x",test[((x[i]&0x3)<<4)+(x[i+1]>>4)]);
	// 	if(x[i+1]=='\x00'){printf("%02x%02x",0x3f,0x3f);break;}
	// 	printf("%02x",test[((x[i+1]&15)<<2)+((x[i+2])>>6)]);
	// 	if(x[i+2]=='\x00'){printf("%02x",0x3f);break;}
	// 	else printf("%02x",test[x[i+2]&63]);
	// 	/* code */
	// }
	// cout << ((int)x[0]>>2) << endl;
	// printf("\n");
}
