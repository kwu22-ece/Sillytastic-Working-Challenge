# City of Goof Machine Manual: Hackster iCE40 Cryptographic IP Core

## Introduction

Welcome to the machine room, fun-tastical worker. This is the technical manual for your Hackster accelerator, affectionately known around Silly Land as the municipal word-scrambler. The nickname is playful; the signal names, electrical behavior, and operating sequence below are the actual interface contract.

This IP core implements a simple, lightweight cryptographic accelerator designed specifically for the Lattice iCE40 UltraPlus FPGA on the Hackster board. It is capable of encrypting or decrypting a 32-bit input word using a simplified lightweight cryptographic algorithm. To maintain a minimal resource footprint, the core omits a standard complex bus interface (like AXI or Wishbone) in favor of a raw SPI peripheral interface combined with discrete sideband I/O for direct application processor control.

## 2. IP Core Overview

**Meet your two machine-room coworkers:** the RP2040 sends the work order; the FPGA processes it.

The IP core operates by ingesting a 32-bit plaintext or ciphertext word via a Serial Peripheral Interface (SPI). The application device (RP2040) acts as the SPI Controller, while the FPGA acts as the SPI Peripheral.

**Critical Architectural Note:** This IP operates on a unified clock domain. The SPI clock (`SCK`) provided by the application processor directly drives the entire internal system, including the shift registers and the cryptographic engines. The application device must provide a continuous or properly bursted `SCK` that does not exceed 1 MHz.

## 3. Port Descriptions

These are the labels on your control panel. The table keeps the original pin names so every worker can map the signals back to the supplied interface, even after a particularly silly lunch break.

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

One word in, one processing job, one word out. Follow the work order in sequence, even when the municipal lunch bell is being unusually persuasive.

To properly ingest data, process it, and read the result back, the application processor must adhere to the following sequence:

### Step 1: Initialization

*Clock in and reset the workbench.*

1. Ensure `SCK` is running or prepared to pulse.
2. Assert `RST_N` low for at least one clock cycle to clear internal registers, then drive `RST_N` high.
3. Drive `NORM_CS_N` high (inactive) and `START` low.

### Step 2: Data Ingestion

*Hand the machine its 32-bit work order.*

1. Set the `ENC_DEC` pin to the desired operation (`0` for encryption, `1` for decryption).
2. Drive `NORM_CS_N` low to enable the shift register.
3. Clock 32 bits of data out from the RP2040 over `MOSI` using `SCK`.
4. Drive `NORM_CS_N` high to latch the full 32-bit word into the internal bus.

### Step 3: Execution

*Start the job and watch the busy light. A fun-tastical worker gives the machine its processing time.*

1. Assert the `START` pin high for at least one `SCK` cycle, then drive it low.
2. Monitor the `BUSY` pin. It will transition high while the encryption or decryption operations are processing the word. This should take 4 clock cycles.
3. **Wait for Completion:** Continue monitoring `BUSY`. Do not initiate any SPI transactions.
4. When `BUSY` falls from high to low (the falling edge), the IP core automatically parallel-loads the processed ciphertext/plaintext back into the SPI shift register.

### Step 4: Data Extraction

*Collect the finished word and close the transaction.*

1. Drive `NORM_CS_N` low.
2. Provide 32 clock cycles on `SCK`. The processed data will be shifted out over the `MISO` line.
3. Drive `NORM_CS_N` high.

## Back to Your Shift

Use the [reference MicroPython application](spi_ice40_crypto_ip_test.py) alongside this manual when building the recovered design's simulation testbench. The supplied application exercises SPI readback, encryption, and decryption. Its pin assignments, test vectors, clock pulses, and pass/fail output remain unchanged in this themed edition.

Return to the [preliminary work order](README.md) for the modification, validation, and submission requirements, or the [worker handbook](../README.md) for the wider challenge. Making the City of Goof fun-tastically-safe means leaving the next crew clear evidence, not just a very festive status light.
