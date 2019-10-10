import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
prPurple("""

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
HASHCAT_BASE_COMMAND = "hashcat -a 0 -m {type} {hash} {wordlist} --force"
options = [
    {
        "name": "MD5 Optimized (<27 chars)",
        "hashType": 0
    },
    {
        "name": "MD5",
        "hashType": 0
    },
    {
        "name": "SHA256",
        "hashType": 1400
    },
    {
        "name": "SHA1",
        "hashType": 1400
    },
    {
        "name": "NTLM Hash",
        "hashType": 1000
    },
    {
        "name": "LM Hash",
        "hashType": 3000
    },
    {
        "name": "WPA/WPA2",
        "hashType": 2500
    },
    {
        "name": "WPA/WPA2 (PMK)",
        "hashType": 2501
    },
    {
        "name": "SHA512",
        "hashType": 1700
    },
    {
        "name": "NetNTLM v2",
        "hashType": 5600
    },
    {
        "name": "phpass/WordPress MD5",
        "hashType": 400
    },
    {
        "name": "Android PIN/Passphrase",
        "hashType": 5800
    },
    {
        "name": "LUKS",
        "hashType": 14600
    }
]

if __name__ == "__main__":
    # Generate menu and prompt user for option
    for count, option in enumerate(options, 1):
        prGreen(f"[{count}] {option['name']}")

    while True:
        selection = input("Enter selection: ")

        if selection.isdigit() and 1 <= int(selection) <= len(options):
            selection = int(selection)
            break
        else:
            print("Bad selection, please try again.")

    selectedItem = options[selection - 1]

    # prompt user for hash and wordlist
    challenge = input("Hash? ")
    prRed("Kali Default: /usr/share/wordlists/rockyou.txt")
    wordlist = input("Wordlist path? ")

    command = HASHCAT_BASE_COMMAND.format(
        type=selectedItem['hashType'],
        hash=challenge,
        wordlist=wordlist,
    )

    os.system(command)
    prYellow(f"\n Executed:\n {command}")
    prCyan(f"\nTo see results Run:\n {command} --show")
    prCyan(f"\nTo save results Run:\n {command} -o <outputname>.txt")

    print("\nExecution complete. Goodbye.")
