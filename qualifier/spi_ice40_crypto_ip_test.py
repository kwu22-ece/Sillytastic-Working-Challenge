# City of Goof machine check: the fun-tastical worker's reference application.
# Silly Land edition: comments are themed; executable behavior is unchanged.

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

    # Clock in: reset the cryptographic core for this shift.

    RST_N.value(0)
    SCK.value(1)
    SCK.value(0)
    RST_N.value(1)
    SCK.value(1)
    SCK.value(0)

    # The work order's original plaintext and expected ciphertext.
    plaintext = bytearray([0x59, 0xC3, 0x59, 0xC3])
    ciphertext = bytearray([0x9C, 0xD8, 0x43, 0x92])
    
    #############################################################
    ## Inspection 1: check the municipal SPI delivery route.
    #############################################################
    txdata = plaintext
    rxdata = bytearray(4)
    NORM_CS_N.value(0)
    spi.write(txdata)
    NORM_CS_N.value(1)

    # Read back the delivery before sending work to the accelerator.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)

    if txdata == rxdata:
        print("SPI functional test pass")
    else:
        print("Error: SPI error")
        return
       
    #############################################################
    ## Inspection 2: put the municipal word-scrambler to work (encryption).
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
    
    # Give the machine the reference script's seven additional clock cycles.
    for i in range(7):
        SCK.value(1)
        SCK.value(0)
          
    if(BUSY.value() == 0):
        print("IP core successfully finished")
    else:
        print("Error: IP core did not finish")
        return
    
    # Collect the finished word for the inspection clipboard.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)
    if rxdata != ciphertext:
        print("Encryption failed, got", binascii.hexlify(rxdata), "expected", binascii.hexlify(ciphertext))
    else:
        print("Encryption value correct:", binascii.hexlify(rxdata))

    #############################################################
    ## Inspection 3: recover the original work order (decryption).
    #############################################################
    ENC_DEC.value(1) # decrypt

    # Reset the cryptographic core before the next municipal job.

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
    
    # Give the machine the reference script's seven additional clock cycles.
    for i in range(7):
        SCK.value(1)
        SCK.value(0)
          
    if(BUSY.value() == 0):
        print("IP core successfully finished")
    else:
        print("Error: IP core did not finish")
        return
    
    # Collect the recovered word and check it against the original work order.
    NORM_CS_N.value(0)
    spi.write_readinto(txdata, rxdata)
    NORM_CS_N.value(1)
    if rxdata != plaintext:
        print("Decryption failed, got", binascii.hexlify(rxdata), "expected", binascii.hexlify(plaintext))
    else:
        print("Decryption value correct:", binascii.hexlify(rxdata))
    

main()
    




