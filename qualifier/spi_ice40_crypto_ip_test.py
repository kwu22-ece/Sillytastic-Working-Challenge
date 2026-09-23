# WUBBLE LUBBLE GUPLE BUBBLE INC: THE POKE-IT-POLITELY CHECKLIST.
# Director Plonko Fizzlebottom, Oompa Loompa employer, requests a gup inspection.
# Get the job: 1,000,000 D-Bucks (Doug Bucks) per floogle of Silly Land time.
# Comments have joined Goof Time; the executable reference behavior is unchanged.

import machine
import binascii

def main():
    ice_done = machine.Pin(3, machine.Pin.IN)

    SCK = machine.Pin(6, machine.Pin.OUT)
    RST_N = machine.Pin(7, machine.Pin.OUT)
    MOSI = machine.Pin(8, machine.Pin.OUT)
    MISO = machine.Pin(9, machine.Pin.IN)
    NORM_CS_N = machine.Pin(10, machine.Pin.OUT)
    START = machine.Pin(12, machine.Pin.OUT)
    BUSY = machine.Pin(14, machine.Pin.IN)
    ENC_DEC = machine.Pin(13, machine.Pin.OUT) # 0 = encrypt, 1 = decrypt

    SCK.value(0)
    RST_N.value(1)
    NORM_CS_N.value(1)
    START.value(0)

    spi = machine.SoftSPI(baudrate=50000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=SCK, mosi=MOSI, miso=MISO)

    # Ceremonially un-wobble the cryptographic core. Fizzlebottom rings a bell.

    RST_N.value(0)
    SCK.value(1)
    SCK.value(0)
    RST_N.value(1)
    SCK.value(1)
    SCK.value(0)

    # Two exact gup parcels: original plaintext and expected ciphertext.
    # Blib has been instructed not to substitute sandwich fillings.
    plaintext = bytearray([0x59, 0xC3, 0x59, 0xC3])
    ciphertext = bytearray([0x9C, 0xD8, 0x43, 0x92])
    
    #############################################################
    ## WUBBLE CHECK: can the tiny SPI parcel chute return the correct parcel?
    #############################################################
    txdata = plaintext
    rxdata = bytearray(4)
    NORM_CS_N.value(0)
    spi.write(txdata)
    NORM_CS_N.value(1)

    # Ask Dispatch to return the parcel before the Gup Desk gets involved.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)

    if txdata == rxdata:
        print("SPI functional test pass")
    else:
        print("Error: SPI error")
        return
       
    #############################################################
    ## LUBBLE CHECK: the Gup Desk encrypts the incoming parcel.
    #############################################################
    ENC_DEC.value(0) # encrypt

    START.value(1)
    SCK.value(1)
    SCK.value(0)
    START.value(0)
    
    if(BUSY.value() == 1):
        print("IP core successfully busy")
    else:
        print("Error: IP core did not go busy")
        return
    
    # Seven additional SCK cycles, as supplied. Payroll floogles do not count.
    for i in range(7):
        SCK.value(1)
        SCK.value(0)
          
    if(BUSY.value() == 0):
        print("IP core successfully finished")
    else:
        print("Error: IP core did not finish")
        return
    
    # Collect the encrypted gup for Fizzlebottom's Clipboard of Destiny.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)
    if rxdata != ciphertext:
        print("Encryption failed, got", binascii.hexlify(rxdata), "expected", binascii.hexlify(ciphertext))
    else:
        print("Encryption value correct:", binascii.hexlify(rxdata))

    #############################################################
    ## GUPLE CHECK: un-gup the parcel by decrypting it back to the original.
    #############################################################
    ENC_DEC.value(1) # decrypt

    # Un-wobble the core again. The bell has become a little overenthusiastic.

    RST_N.value(0)
    SCK.value(1)
    SCK.value(0)
    RST_N.value(1)
    SCK.value(1)
    SCK.value(0)

    txdata = ciphertext
    rxdata = bytearray(4)
    NORM_CS_N.value(0)
    spi.write(txdata)
    NORM_CS_N.value(1)

    START.value(1)
    SCK.value(1)
    SCK.value(0)
    START.value(0)
    
    # Seven additional SCK cycles, as supplied. Doug may count along quietly.
    for i in range(7):
        SCK.value(1)
        SCK.value(0)
          
    if(BUSY.value() == 0):
        print("IP core successfully finished")
    else:
        print("Error: IP core did not finish")
        return
    
    # BUBBLE CHECK: compare the recovered word with the original gup parcel.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)
    if rxdata != plaintext:
        print("Decryption failed, got", binascii.hexlify(rxdata), "expected", binascii.hexlify(plaintext))
    else:
        print("Decryption value correct:", binascii.hexlify(rxdata))
    

main()
    




