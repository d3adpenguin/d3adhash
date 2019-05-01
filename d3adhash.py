import os 
print("""

             .                 ::                                 :,            
           .                 .                .                      .          
                 .         .       .       ..                                   
 .                       ..                                  .          .     . 
                      .?$D.              .          .NDN                      . 
    ::               .NDDDDDD,                   .DDDDDDD::,               ,    
      .            ...DDDDDDDDDD          .    DDDDDDDDDD                 .     
.                  . 8DDDDDDDDDDDD           DDDDDDDDDNDDN            .  .      
.                    DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD            ,         
                     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD       .              
             ,       DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        ::            
            .  .     NDDDDDDDDNDDDDDDDDDDDDDDDDDDDDDDDDDDN                      
                     ~DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDI            .         
                     .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD     .                 
  .   .               DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD   .                   
    ,:               8DNDDDDDDDDDDDDDDDNNNDDDDDDDDDDDDDDDI                 .,   
   .                 DDDDDN     DDDDDDDDDDDDDDD     MDD??D                      
 .                   DDDDDD      DDDDDDDDDDDDN      DI??DD   .                 .
                 .   DDDDDD       DDDDDDDDDDD.      Z$DDDN     .                
                      DDDDDD .   .DDDDDDDDDDD  .   DDDDDD                       
             .        IDDDDDDDD$DDDDDDDDDDDDDDDDDDDDDDDDD         ::            
            .          ODDDDDDDDNDDDDDDDDDDDDDDDDDDDDDDD          . .           
        .,              .DDDDDDDDDDDDDDDDDDDDDDDDDDDDD.               .         
                          NDDDDDDDDDDDDDDDDDDDDDDDDDD .       .                 
                   DDDDD    ,DDDDDDDDDDDDDDDDDDDDD~    DDDDD.                 . 
    ..           .DDDDDON       DDDDDDDN8DDDDND.      DDDNNDD.             . .  
   ...           NDDDDDDD:             . .           .DDDNNDDD             .    
.      .         NDDDDDDD,                 .          DDDDDDDD        ,.,.      
.        .      DDDDDDDDDD                          .DDDDDDDDDD       ...       
           .  .DDDDDDDDDDDDDD                     DDDDDDDDDDDDDD?               
            :,NDDDDDDDDDDDDDDDDN.              DD:DDDDDDDDDDDDDDD .             
            .:NDDDDDDDDDDDDDDDDDDDD.        DDD?DDDDDDDDDDDDDDDDD .             
              .DDDDDD.  ?DDDDDDDDDDDDD. .NDDDDDDDDDDDDO  .DDDDDZ                
                  .       . DDDDDDDDDDDDDDDDDDDDDDD,        .  ,                
                       .,     .DDDDDDDDDDDDDDDDD.          .             .      
    ,                 .         DDDDDDDDDDDDDDD           ,.               ::   
     .             .  .      DDDDDDDDDDDDDDDDDDDDD     ...                 ::   
       .       $DD?NN    :DDDDDDDDDDDDD DDDDDDDDDDDDD=,   DDDDDN                
 .            DDIDDDDDDNDDDDDDDDDDDD       DDDDDDDDD??NDDDDDDDDDD               
              DDDDDDDDDDDDDDDDDDD.           .DDDDDDDDDDDDDDDDDDN               
             :NDDDDDDDDDDDDDDD.::                DDDDDDDDDDDDDDDD .             
             ::MDDDDDDDDDDD.   ::                .  DDDDDDDDDDDD   ,            
                 DDDDDDDD.                           .DDDDDDDD       .          
                 NDDDDDDD=, .                        .DDDDDDDD         .        
       .         7DDDDDDD.,                .          DDDDDDD8                 .
    ,:            MDDD8D.               ::             DDNNDN              .    
    ::             .  ..               ,,:               :,                ..   
  .               ..    .                 .                 .                 . 
.               ..        .                          .                          
                 .                .                , .          .               
                              .                  ,.                 .           
Dear Die-ary, there's nothing terribly wrong with feeling lost,
so long as that feeling precedes some plan on your part to actually do something about it.
Too often a person grows complacent with their disillusionment,
perpetually wearing their 'discomfort' like a favorite shirt.
I can't say I'm very pleased with where my life is just now...
but I can't help but look forward to where it's going. 
-Nny
""")
print("-----------------------------")
print("-----------------------------")
print("---------No-Salts------------")
print("-----Hash Cat Utility--------")
print("---All results in krakd.txt---")
print("-----------------------------")
print("[1] MD5 optimized (under 27 character passwords)")
print("[2] MD5 ")
print("[3] SHA256 ")
print("[4] SHA1 ")
print("[5] NTLM ")
print("[6] LM ")
print("[7] WPA/WPA2 ")
print("[8] WPA/WPA2 PMK ")
print("[9] SHA512")
print("[10] NetNLTMv2")
print("[11] WordPress(md5)")
print("[12] Android Pin/Pass. ")
print("[13] LUKS")

option = int(input("Enter number : \n"))


if option == 1:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 0 $Hash $Word --force --show > krakd.txt
""")

if option == 2:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 0 $Hash $Word --force --show > krakd.txt
""")

if option == 3:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 1400 $Hash $Word --force --show > krakd.txt
""")

if option == 4:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 100 $Hash $Word --force --show > krakd.txt
""")

if option == 5:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 1000 $Hash $Word --force --show > krakd.txt  
""")

if option == 6:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 3000 $Hash $Word  --force --show > krakd.txt
""")

if option == 7:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 2500 $Hash $Word  --force --show > krakd.txt
""")

if option == 8:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 2501 $Hash $Word  --force --show > krakd.txt
""")

if option == 9:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 1700 $Hash $Word  --force --show > krakd.txt
""")

if option == 10:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 5600 $Hash $Word  --force --show > krakd.txt
""")

if option == 11:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 400 $Hash $Word  --force --show > krakd.txt
""")

if option == 12:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 5800 $Hash $Word  --force --show > krakd.txt
""")

if option == 13:
    os.system("""
echo -n "Hash to Krak : "
read Hash
echo -n " Wordlist to use :"
read Word
sudo hashcat -a 0 -m 14600 $Hash $Word  --force --show > krakd.txt
""")
