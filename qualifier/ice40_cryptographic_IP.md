# THE BOOK OF KNOBS

**WUBBLE LUBBLE GUPLE BUBBLE INC | Great Gup Engine Service Desk**

*Technical equipment: Hackster iCE40 Cryptographic IP Core.*

## Introduction

Director Plonko Fizzlebottom, the Oompa Loompa in charge of hiring, hands you a manual with a tiny tie attached. "The Great Gup Engine is the pride of WUBBLE LUBBLE GUPLE BUBBLE INC," he announces. "Should you earn this job, your pay will be **1,000,000 D-Bucks (Doug Bucks) per floogle**. Until then, please learn what the knobs do."

This is the interface contract for the Hackster accelerator. Its signal names and timing are written in engineering units. The payroll flooglometer has absolutely no electrical connection to `SCK`.

This IP core implements a simple, lightweight cryptographic accelerator designed specifically for the Lattice iCE40 UltraPlus FPGA on the Hackster board. It is capable of encrypting or decrypting a 32-bit input word using a simplified lightweight cryptographic algorithm. To maintain a minimal resource footprint, the core omits a standard complex bus interface (like AXI or Wishbone) in favor of a raw SPI peripheral interface combined with discrete sideband I/O for direct application processor control.

## 2. IP Core Overview

**Meet Dispatch and the Gup Desk.** The RP2040 sends the work order. The FPGA processes it. Neither is permitted to answer "because wubble" when asked for a waveform.

The IP core operates by ingesting a 32-bit plaintext or ciphertext word via a Serial Peripheral Interface (SPI). The application device (RP2040) acts as the SPI Controller, while the FPGA acts as the SPI Peripheral.

**Critical Architectural Note:** This IP operates on a unified clock domain. The SPI clock (`SCK`) provided by the application processor directly drives the entire internal system, including the shift registers and the cryptographic engines. The application device must provide a continuous or properly bursted `SCK` that does not exceed 1 MHz.

## 3. Port Descriptions

Blib has removed the labels "probably this one" and "spicy doorknob" from the control panel. Use the actual port descriptions below. The `BUSY` signal is the machine's status flag, not permission to put the entire workbench on hold music.

| Pin Name | Direction | Description |
| --- | --- | --- |
| `SCK` | Input | Unified system and SPI clock (Max 1 MHz). |
| `RST_N` | Input | Synchronous active-low reset. |
| `MOSI` | Input | SPI Controller Out, Peripheral In (Serial Data). |
| `MISO` | Output | SPI Controller In, Peripheral Out (Serial Data). |
| `NORM_CS_N` | Input | Active-low SPI chip-select. Acts as the shift-enable for the input buffer. |
| `START` | Input | Triggers the start of the encryption or decryption process. |
| `ENC_DEC` | Input | Mode select flag. `0`: Encrypt, `1`: Decrypt. |
| `BUSY` | Output | Status flag. High while the crypto engine is actively processing data. |
| `ICE_LED` | Output | Visual mirror of the `BUSY` signal, routed to an onboard LED. |


## 4. Usage Guideline

The company calls this operating procedure **LOAD THE GUP, DO THE GUP, GET THE GUP**. Director Fizzlebottom performs a three-step shuffle when explaining it. You can simply follow the sequence.

To properly ingest data, process it, and read the result back, the application processor must adhere to the following sequence:

### Step 1: Initialization

*The ceremonial un-wobbling. Reset the core before delivering today's gup.*

1. Ensure `SCK` is running or prepared to pulse.
2. Assert `RST_N` low for at least one clock cycle to clear internal registers, then drive `RST_N` high.
3. Drive `NORM_CS_N` high (inactive) and `START` low.

### Step 2: Data Ingestion

*Feed the tiny parcel chute one 32-bit work order. Whole sandwiches remain outside the chute.*

1. Set the `ENC_DEC` pin to the desired operation (`0` for encryption, `1` for decryption).
2. Drive `NORM_CS_N` low to enable the shift register.
3. Clock 32 bits of data out from the RP2040 over `MOSI` using `SCK`.
4. Drive `NORM_CS_N` high to latch the full 32-bit word into the internal bus.

### Step 3: Execution

*The Gup Desk is gupulating. Watch `BUSY` and follow the clocking rules below. Shouting "FASTER, I AM PAID PER FLOOGLE" is not a clock source.*

1. Assert the `START` pin high for at least one `SCK` cycle, then drive it low.
2. Monitor the `BUSY` pin. It will transition high while the encryption or decryption operations are processing the word. This should take 4 clock cycles.
3. **Wait for Completion:** Continue monitoring `BUSY`. Do not initiate any SPI transactions.
4. When `BUSY` falls from high to low (the falling edge), the IP core automatically parallel-loads the processed ciphertext/plaintext back into the SPI shift register.

### Step 4: Data Extraction

*Collect the finished parcel from the output hatch. Dispatch has been waiting with a stamp reading VERY ENCRYPTED INDEED.*

1. Drive `NORM_CS_N` low.
2. Provide 32 clock cycles on `SCK`. The processed data will be shifted out over the `MISO` line.
3. Drive `NORM_CS_N` high.

## Return the Knobs to the Department of Knobs

Use the [Poke-It-Politely Checklist](spi_ice40_crypto_ip_test.py), the reference MicroPython application, alongside this manual when building the recovered design's simulation testbench. It exercises SPI readback, encryption, and decryption. The program's pin assignments, test vectors, clock pulses, and pass/fail output retain their technical meanings, however loudly Blib narrates the comments.

Return to [the Great Gup Inspection](README.md) for modification, validation, and submission requirements, or [Fizzlebottom's hiring packet](../README.md) for the full job posting. The City of Goof needs a fun-tastical worker. The knobs believe in you. Doug has not stopped counting.
