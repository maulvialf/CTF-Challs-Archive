// docker run --rm -v $PWD:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name chal -i ubuntu:18.04
// docker exec -it chal bash
// apt update && apt install -y make gcc socat
// socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./exec.sh,su=nobody
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define UKURAN_KANDANG 20
#define BOBOT_AYAM  32

char *ayams[UKURAN_KANDANG]={0};
char nama[100];

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    _exit(0);
  }
}

void nobaper() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  signal(SIGALRM, kill_on_timeout);
  alarm(60);
}

void menu() {
  puts("###############################");
  printf("Kelola %s", nama);
  puts("1) Beli ayam baru");
  puts("2) Lihat nama ayam");
  puts("3) Ubah nama ayam");
  puts("4) Makan rica-rica ayam");
  puts("###############################");
}

void set_nama() {
  puts("-------------------------------------------------------------------------------");
  puts("Selamat datang di program kandang ayam");
  puts("Di sini Anda bisa membeli, memberi nama, serta menyembelih ayam-ayam Anda");
  puts("-------------------------------------------------------------------------------");
  fputs("Masukkan nama kandang ayam Anda: ", stdout);
  read(0, nama, 100);
  printf(nama);
  puts("Nama yang bagus. Terima kasih telah melakukan registrasi di sistem kami");
}

void beli_ayam() {
  int ind = 0;
  fputs("Ayam ke berapa? ", stdout);
  scanf("%d", &ind);
  if((ind >=0 && ind < UKURAN_KANDANG) && !ayams[ind]) {
    ayams[ind] = malloc(BOBOT_AYAM);
    fputs("Nama ayam: ", stdout);
    read(0, ayams[ind], BOBOT_AYAM);
  } else {
    puts(">:(");
  }
}

void lihat_nama_ayam() {
  int ind = 0;

  fputs("Ayam ke berapa? ", stdout);
  scanf("%d", &ind);

  if(ind < 0 || ind >= UKURAN_KANDANG) {
    puts("ayamnya gak ada");
    return;
  }

  printf("Nama: %s\n", ayams[ind]);
}

void kasih_nama_ayam() {
  int ind = 0;

  fputs("Ayam ke berapa? ", stdout);
  scanf("%d", &ind);

  if(ind < 0 || ind >= UKURAN_KANDANG) {
    puts("ayamnya gak ada");
    return;
  }

  fputs("Nama ayam: ", stdout);
  read(0, ayams[ind], BOBOT_AYAM);
}

void potong_ayam() {
  int ind = 0;

  fputs("Ayam ke berapa? ", stdout);
  scanf("%d", &ind);

  if(ind < 0 || ind >= UKURAN_KANDANG) {
    puts("ayamnya gak ada");
    return;
  }

  free(ayams[ind]);
}

int main() {
  nobaper();

  set_nama();

  int choice = -1;

  while(1) {
    menu();

    fputs("Pilihan Anda: ", stdout);
    scanf("%d", &choice);

    switch(choice) {
    case 1:
      beli_ayam();
      break;
    case 2:
      lihat_nama_ayam();
      break;
    case 3:
      kasih_nama_ayam();
      break;
    case 4:
      potong_ayam();
      break;
    default:
      puts(">:(");
      break;
    }
  }

  return 0;
}