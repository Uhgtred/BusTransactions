# Bus Systems Communication Module

A flexible and extensible framework for interacting with multiple bus systems through a unified interface. This module provides a robust abstraction layer for various communication protocols and bus systems.

## Overview

This module enables seamless communication with different bus systems (such as UDP, Serial, etc.) through a plugin-based architecture. It provides a consistent interface while supporting advanced features like:

- Message compression
- Data serialization
- Custom encoding/decoding
- Synchronous and asynchronous communication patterns

## Core Components

### AbstractBus

The main interface class that provides a unified way to interact with different bus systems. It supports:

- Single message operations (read/write)
- Continuous message reading with callback handling
- Pluggable processing pipeline (compression, serialization, encoding)

#### Key Features

- **Plugin Architecture**: Easily extend functionality with custom bus implementations
- **Processing Pipeline**: Configurable message processing with:
  - Compression
  - Serialization
  - Encoding/Decoding
- **Operation Modes**:
  - Single message mode for one-time operations
  - Continuous reading mode with callback support
- **Thread Safety**: Built-in thread management for continuous operations
- **Error Handling**: Comprehensive exception handling and logging

## Usage

### Basic Example