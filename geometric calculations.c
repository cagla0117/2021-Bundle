#include <stdio.h>

//Çağla Mıdıklı
int main(){
    char k ;
    double alan = 0;
    double r;
    double x;
    double y;
    printf("alanını hesaplamak istediğiniz şekli girin: (daire:a,üçgen:b,dikdörtgen: ");
    scanf("%c", &k);
    if ( k == 'a'){
        printf("yarıçap giriniz: ");
        scanf("%lf",&r);
        alan = 3.14 * r * r ;
        printf("dairenin alanı = %.4lf", alan);


    }
    else if (k == 'b'){
        printf("taban kenarını giriniz: ");
        scanf("%lf",&x);
        printf("taban kenarına ait yüksekliği giriniz: ");
        scanf("%lf",&y);
        alan =  x * y / 2 ;
        printf("üçgenin  alanı = %.4lf", alan);

    }
    else if ( k == 'c'){
        printf("kısa kenarını giriniz: ");
        scanf("%lf",&x);
        printf("uzun kenarını giriniz: ");
        scanf("%lf",&y);
        alan =  x * y  ;
        printf("dikdörtgenin alanı = %.4lf", alan);

    }
   

}