# Cache Simulator with LRU Replacement

## Overview
This project simulates a cache memory system using the Least Recently Used (LRU) replacement policy.

## Features
- Configurable cache size
- Tracks cache hits and misses
- Implements LRU replacement policy
- Calculates hit rate and miss rate

## How It Works
- If a block is accessed and present in cache → HIT
- If not present → MISS
- On MISS and full cache → least recently used block is removed

## Example
Access Sequence: [1,2,3,1,4,5,2,1,2,3]  
Cache Size: 3  

## Output
- Total Accesses
- Hits
- Misses
- Hit Rate
- Miss Rate

## Learning Outcome
- Understanding memory hierarchy
- Cache replacement policies
- Performance trade-offs in CPU systems

## Future Improvements
- FIFO and LFU policies
- Multi-level cache simulation
- Visualization of cache state
