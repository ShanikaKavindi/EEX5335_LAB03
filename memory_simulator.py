# Simple Memory Management Simulator (Short Version)

PAGE_SIZE = 256
NUM_FRAMES = 4
TLB_SIZE = 2
CACHE_SIZE = 2

# Structures
page_table = {}
tlb = []
cache = []

# Statistics
stats = {"accesses": 0, "tlb_hits": 0, "page_faults": 0, "cache_hits": 0}

def access_memory(virtual_address):
    stats["accesses"] += 1
    vpn = virtual_address // PAGE_SIZE
    offset = virtual_address % PAGE_SIZE
    print(f"\nAccessing VA {hex(virtual_address)} (VPN={vpn}, Offset={offset})")

    # Step 1: TLB lookup
    for v, f in tlb:
        if v == vpn:
            stats["tlb_hits"] += 1
            print(f"TLB HIT: VPN {vpn} -> Frame {f}")
            return get_from_cache(f, offset)
    print("TLB MISS")

    # Step 2: Page table lookup
    if vpn not in page_table:
        stats["page_faults"] += 1
        if len(page_table) >= NUM_FRAMES:
            evict = next(iter(page_table))
            print(f"Page Fault: Evicting VPN {evict}")
            del page_table[evict]
        page_table[vpn] = len(page_table)
        print(f"Page Fault: Loaded VPN {vpn} into Frame {page_table[vpn]}")
    frame = page_table[vpn]

    # Update TLB (FIFO)
    if len(tlb) >= TLB_SIZE:
        tlb.pop(0)
    tlb.append((vpn, frame))

    return get_from_cache(frame, offset)

def get_from_cache(frame, offset):
    tag = (frame, offset // 16)  # block tag
    for t, data in cache:
        if t == tag:
            stats["cache_hits"] += 1
            print(f"Cache HIT: {tag} -> Data {data}")
            return data
    print(f"Cache MISS: Loading block {tag}")
    if len(cache) >= CACHE_SIZE:
        cache.pop(0)
    data = frame  # simple data = frame number
    cache.append((tag, data))
    return data

# Test run
virtual_addresses = [0x569E, 0x569E, 0x569F, 0x569E, 0x376E, 0x376E]
for va in virtual_addresses:
    access_memory(va)

print("\n=== Statistics ===")
for k, v in stats.items():
    print(f"{k}: {v}")

